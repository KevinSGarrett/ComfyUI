param(
  [ValidateSet("acquire", "release", "status", "heartbeat")]
  [string]$Action = "status",

  [ValidatePattern("^Lane_[1-6]$")]
  [string]$Lane,

  [string]$Purpose = "",

  [int]$LeaseMinutes = 60,

  [switch]$Force
)

$ErrorActionPreference = "Stop"

$SessionRoot = if ($env:WAVE42_SESSION_ROOT) { $env:WAVE42_SESSION_ROOT } else { "C:\Comfy_UI_Lora\5_sessions" }
$StateDir = Join-Path $SessionRoot "Main\shared_state"
$LeasePath = Join-Path $StateDir "ec2_lease.json"
$LockPath = Join-Path $StateDir "ec2_lease.lock"

[System.IO.Directory]::CreateDirectory($StateDir) | Out-Null

function New-EmptyLease {
  [pscustomobject]@{
    schema_version = "1.0"
    lease_state = "free"
    owner_lane = $null
    purpose = $null
    acquired_at_utc = $null
    expires_at_utc = $null
    last_heartbeat_utc = $null
    ec2_instance_id = if ($env:WAVE42_EC2_INSTANCE_ID) { $env:WAVE42_EC2_INSTANCE_ID } else { "i-0560bf8d143f93bb1" }
    notes = "Live lease state. This file is intentionally ignored by Git."
  }
}

function Read-Lease {
  if (-not (Test-Path -Path $LeasePath)) {
    return New-EmptyLease
  }
  $raw = Get-Content -Path $LeasePath -Raw
  if ([string]::IsNullOrWhiteSpace($raw)) {
    return New-EmptyLease
  }
  return ($raw | ConvertFrom-Json)
}

function Write-Lease($Lease) {
  $temp = "$LeasePath.tmp"
  $Lease | ConvertTo-Json -Depth 8 | Set-Content -Path $temp -Encoding UTF8
  Move-Item -Path $temp -Destination $LeasePath -Force
}

function Invoke-WithLeaseLock([scriptblock]$Body) {
  $deadline = (Get-Date).ToUniversalTime().AddSeconds(20)
  while ($true) {
    try {
      $stream = [System.IO.File]::Open($LockPath, [System.IO.FileMode]::CreateNew, [System.IO.FileAccess]::Write, [System.IO.FileShare]::None)
      try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes("pid=$PID created=$((Get-Date).ToUniversalTime().ToString("o"))")
        $stream.Write($bytes, 0, $bytes.Length)
      } finally {
        $stream.Close()
      }
      break
    } catch {
      if ((Get-Date).ToUniversalTime() -gt $deadline) {
        throw "Could not acquire local EC2 lease file lock: $LockPath"
      }
      Start-Sleep -Milliseconds 250
    }
  }

  try {
    & $Body
  } finally {
    if (Test-Path -Path $LockPath) {
      Remove-Item -Path $LockPath -Force
    }
  }
}

function Lease-IsExpired($Lease) {
  if ($Lease.lease_state -ne "held") {
    return $true
  }
  if (-not $Lease.expires_at_utc) {
    return $true
  }
  $expires = [DateTime]::Parse($Lease.expires_at_utc).ToUniversalTime()
  return ((Get-Date).ToUniversalTime() -ge $expires)
}

Invoke-WithLeaseLock {
  $lease = Read-Lease
  $now = (Get-Date).ToUniversalTime()

  if ($Action -eq "status") {
    $lease | ConvertTo-Json -Depth 8
    return
  }

  if (-not $Lane) {
    throw "-Lane is required for $Action"
  }

  if ($Action -eq "acquire") {
    if (($lease.lease_state -eq "held") -and (-not (Lease-IsExpired $lease)) -and (-not $Force)) {
      throw "EC2 lease is already held by $($lease.owner_lane) until $($lease.expires_at_utc): $($lease.purpose)"
    }

    if ($Lane -ne "Lane_4" -and (-not $Force)) {
      throw "Only Lane_4 may acquire the EC2 lease by policy. Other lanes must create EC2 request files."
    }

    $lease.lease_state = "held"
    $lease.owner_lane = $Lane
    $lease.purpose = $Purpose
    $lease.acquired_at_utc = $now.ToString("o")
    $lease.expires_at_utc = $now.AddMinutes($LeaseMinutes).ToString("o")
    $lease.last_heartbeat_utc = $now.ToString("o")
    Write-Lease $lease
    $lease | ConvertTo-Json -Depth 8
    return
  }

  if ($Action -eq "heartbeat") {
    if ($lease.owner_lane -ne $Lane -and (-not $Force)) {
      throw "Cannot heartbeat lease owned by $($lease.owner_lane)"
    }
    $lease.last_heartbeat_utc = $now.ToString("o")
    if ($LeaseMinutes -gt 0) {
      $lease.expires_at_utc = $now.AddMinutes($LeaseMinutes).ToString("o")
    }
    Write-Lease $lease
    $lease | ConvertTo-Json -Depth 8
    return
  }

  if ($Action -eq "release") {
    if ($lease.owner_lane -ne $Lane -and (-not $Force)) {
      throw "Cannot release lease owned by $($lease.owner_lane)"
    }
    $lease = New-EmptyLease
    Write-Lease $lease
    $lease | ConvertTo-Json -Depth 8
    return
  }
}

