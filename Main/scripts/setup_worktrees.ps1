param(
  [string]$SessionRoot = $(if ($env:WAVE42_SESSION_ROOT) { $env:WAVE42_SESSION_ROOT } else { "C:\Comfy_UI_Lora\5_sessions" }),
  [string]$WorktreeRoot = $(if ($env:WAVE42_WORKTREE_ROOT) { $env:WAVE42_WORKTREE_ROOT } else { "C:\Comfy_UI_Lora\5_session_worktrees" }),
  [string]$RemoteUrl = "https://github.com/KevinSGarrett/ComfyUI.git"
)

$ErrorActionPreference = "Stop"

[System.IO.Directory]::CreateDirectory($SessionRoot) | Out-Null
[System.IO.Directory]::CreateDirectory($WorktreeRoot) | Out-Null

Push-Location $SessionRoot
try {
  if (-not (Test-Path -Path ".git")) {
    git init -b main
  }

  git config core.hooksPath .githooks

  $remote = git remote 2>$null
  if ($remote -notcontains "origin") {
    git remote add origin $RemoteUrl
  } else {
    git remote set-url origin $RemoteUrl
  }

  cmd /c "git rev-parse --verify HEAD >NUL 2>NUL"
  $hasHead = ($LASTEXITCODE -eq 0)

  if (-not $hasHead) {
    git add README.md .gitignore .githooks Main Lane_1 Lane_2 Lane_3 Lane_4 Lane_5 Lane_6
    git commit -m "Add six-lane Codex coordination scaffold"
  }

  $lanes = @(
    @{ Path = "Lane_1"; Branch = "lane/lane-1-main-flow" },
    @{ Path = "Lane_2"; Branch = "lane/lane-2-spatial-contact" },
    @{ Path = "Lane_3"; Branch = "lane/lane-3-model-assets" },
    @{ Path = "Lane_4"; Branch = "lane/lane-4-runtime-ec2" },
    @{ Path = "Lane_5"; Branch = "lane/lane-5-qa-tracker" },
    @{ Path = "Lane_6"; Branch = "lane/lane-6-generation-presets" }
  )

  foreach ($lane in $lanes) {
    $target = Join-Path $WorktreeRoot $lane.Path
    $branch = $lane.Branch
    $existing = git worktree list --porcelain | Select-String -SimpleMatch $target
    if ($existing) {
      Write-Host "Worktree already exists: $target"
      continue
    }

    cmd /c "git show-ref --verify --quiet refs/heads/$branch"
    if ($LASTEXITCODE -eq 0) {
      git worktree add $target $branch
    } else {
      git worktree add -b $branch $target main
    }
  }
} finally {
  Pop-Location
}

Write-Host "Worktree setup complete."
