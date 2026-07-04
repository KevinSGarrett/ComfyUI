param(
  [ValidateSet("preflight", "status", "start", "stop")]
  [string]$Action = "preflight",

  [ValidatePattern("^Lane_[1-6]$")]
  [string]$Lane = "Lane_4",

  [string]$InstanceId = $(if ($env:WAVE42_EC2_INSTANCE_ID) { $env:WAVE42_EC2_INSTANCE_ID } else { "i-0560bf8d143f93bb1" }),

  [switch]$ReleaseLeaseAfterStop
)

$ErrorActionPreference = "Stop"

$SessionRoot = if ($env:WAVE42_SESSION_ROOT) { $env:WAVE42_SESSION_ROOT } else { "C:\Comfy_UI_Lora\5_sessions" }
$LeaseScript = Join-Path $SessionRoot "Main\scripts\ec2_lease.ps1"

function Get-Lease {
  $json = & $LeaseScript -Action status
  return ($json | ConvertFrom-Json)
}

function Assert-LeaseOwner {
  $lease = Get-Lease
  if ($lease.lease_state -ne "held" -or $lease.owner_lane -ne $Lane) {
    throw "Lane $Lane does not hold the EC2 lease. Acquire it before live EC2 actions."
  }
}

function Invoke-Aws($Args) {
  & aws @Args
  if ($LASTEXITCODE -ne 0) {
    throw "AWS command failed: aws $($Args -join ' ')"
  }
}

if ($Action -in @("start", "stop")) {
  Assert-LeaseOwner
}

Write-Host "Checking AWS identity..."
Invoke-Aws @("sts", "get-caller-identity")

Write-Host "Checking AWS region..."
Invoke-Aws @("configure", "get", "region")

Write-Host "Checking EC2 state for $InstanceId..."
Invoke-Aws @("ec2", "describe-instances", "--instance-ids", $InstanceId)

if ($Action -eq "start") {
  Write-Host "Starting EC2 instance $InstanceId under lease owner $Lane..."
  Invoke-Aws @("ec2", "start-instances", "--instance-ids", $InstanceId)
  return
}

if ($Action -eq "stop") {
  Write-Host "Stopping EC2 instance $InstanceId under lease owner $Lane..."
  Invoke-Aws @("ec2", "stop-instances", "--instance-ids", $InstanceId)
  if ($ReleaseLeaseAfterStop) {
    & $LeaseScript -Action release -Lane $Lane | Out-Host
  }
  return
}

Write-Host "Preflight/status complete. No EC2 state was changed."

