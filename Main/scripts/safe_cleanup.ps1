param(
  [ValidatePattern("^Lane_[1-6]$")]
  [string]$Lane = "Lane_4",

  [int]$OlderThanDays = 7,

  [switch]$Apply
)

$ErrorActionPreference = "Stop"

$allowedRoots = @(
  "C:\Comfy_UI\_tmp",
  "C:\Comfy_UI\Runtime\temp",
  "C:\Comfy_UI\outputs\temp",
  "C:\Comfy_UI\EC2_Mirror\stale",
  "C:\Comfy_UI\_ec2sd\stale",
  "C:\Comfy_UI_Lora\5_sessions\$Lane\scratch"
)

$protectedRoots = @(
  "C:\Comfy_UI\Implementation\workflows",
  "C:\Comfy_UI\Implementation\trackers",
  "C:\Comfy_UI\Implementation\evidence",
  "C:\Comfy_UI\Runtime_Data\models",
  "C:\Comfy_UI\models",
  "C:\Comfy_UI_Lora\models",
  "C:\Comfy_UI_Lora\Reference_Images",
  "C:\Comfy_UI_Lora\Reference_Images_002",
  "C:\Comfy_UI_Lora\Reference_Images_Organized"
)

function Get-FullPath($Path) {
  return [System.IO.Path]::GetFullPath($Path)
}

function Is-Under($Path, $Root) {
  $fullPath = (Get-FullPath $Path).TrimEnd('\')
  $fullRoot = (Get-FullPath $Root).TrimEnd('\')
  return $fullPath.StartsWith($fullRoot, [System.StringComparison]::OrdinalIgnoreCase)
}

function Is-Protected($Path) {
  foreach ($root in $protectedRoots) {
    if (Is-Under $Path $root) {
      return $true
    }
  }
  return $false
}

$cutoff = (Get-Date).AddDays(-1 * $OlderThanDays)
$candidates = @()

foreach ($root in $allowedRoots) {
  if (-not (Test-Path -Path $root)) {
    continue
  }
  $rootFull = Get-FullPath $root
  Get-ChildItem -Path $rootFull -Force -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.LastWriteTime -lt $cutoff } |
    ForEach-Object {
      $path = $_.FullName
      if (-not (Is-Under $path $rootFull)) {
        throw "Refusing cleanup candidate outside allowed root: $path"
      }
      if (Is-Protected $path) {
        throw "Refusing protected cleanup candidate: $path"
      }
      $candidates += $_
    }
}

$summary = $candidates | Select-Object FullName, Length, LastWriteTime, PSIsContainer
$summary | Format-Table -AutoSize

if (-not $Apply) {
  Write-Host "Dry run only. Re-run with -Apply to delete these candidates."
  return
}

foreach ($candidate in $candidates) {
  $path = $candidate.FullName
  $insideAllowed = $false
  foreach ($root in $allowedRoots) {
    if ((Test-Path -Path $root) -and (Is-Under $path $root)) {
      $insideAllowed = $true
      break
    }
  }
  if (-not $insideAllowed) {
    throw "Refusing delete outside allowed roots: $path"
  }
  if (Is-Protected $path) {
    throw "Refusing delete under protected root: $path"
  }
  Remove-Item -Path $path -Recurse -Force
}

Write-Host "Cleanup complete."

