$ErrorActionPreference = "Stop"

$SessionRoot = if ($env:WAVE42_SESSION_ROOT) { $env:WAVE42_SESSION_ROOT } else { "C:\Comfy_UI_Lora\5_sessions" }
$requiredFiles = @(
  "README.md",
  "Main\GLOBAL_INSTRUCTIONS.md",
  "Main\LANE_BOUNDARIES.md",
  "Main\MODEL_EFFORT_ASSIGNMENTS.md",
  "Main\EC2_LEASE_PROTOCOL.md",
  "Main\SELF_HOSTED_LLM_POLICY.md",
  "Main\CLEANUP_POLICY.md",
  "Main\GIT_WORKTREE_SETUP.md",
  "Main\schemas\evidence_record.schema.json",
  "Main\shared_state\lane_registry.json",
  "Main\scripts\ec2_lease.ps1",
  "Main\scripts\safe_cleanup.ps1"
)

$failures = @()

foreach ($file in $requiredFiles) {
  $path = Join-Path $SessionRoot $file
  if (-not (Test-Path -Path $path -PathType Leaf)) {
    $failures += "Missing file: $path"
  }
}

foreach ($i in 1..7) {
  $laneDir = Join-Path $SessionRoot "Lane_$i"
  $laneFile = Join-Path $laneDir "LANE_INSTRUCTIONS.md"
  if (-not (Test-Path -Path $laneDir -PathType Container)) {
    $failures += "Missing lane dir: $laneDir"
  }
  if (-not (Test-Path -Path $laneFile -PathType Leaf)) {
    $failures += "Missing lane instructions: $laneFile"
  }
}

$jsonFiles = @(
  "Main\schemas\evidence_record.schema.json",
  "Main\templates\evidence_record.template.json",
  "Main\shared_state\lane_registry.json",
  "Main\shared_state\ec2_lease.template.json",
  "Main\shared_state\ec2_lease.json"
)

foreach ($file in $jsonFiles) {
  $path = Join-Path $SessionRoot $file
  if (Test-Path -Path $path -PathType Leaf) {
    try {
      Get-Content -Path $path -Raw | ConvertFrom-Json | Out-Null
    } catch {
      $failures += "Invalid JSON: $path"
    }
  }
}

if ($failures.Count -gt 0) {
  $failures | ForEach-Object { Write-Error $_ }
  exit 1
}

Write-Host "Lane session system verified."
