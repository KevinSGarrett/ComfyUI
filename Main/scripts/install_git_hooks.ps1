$ErrorActionPreference = "Stop"

$SessionRoot = if ($env:WAVE42_SESSION_ROOT) { $env:WAVE42_SESSION_ROOT } else { "C:\Comfy_UI_Lora\5_sessions" }
Push-Location $SessionRoot
try {
  git config core.hooksPath .githooks
  Write-Host "Installed Git hooks from .githooks"
} finally {
  Pop-Location
}

