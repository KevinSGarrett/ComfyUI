$ErrorActionPreference = "Stop"

$blockedNamePatterns = @(
  '(^|/)\.env$',
  '\.pem$',
  '\.key$',
  '\.p12$',
  '\.pfx$',
  '\.safetensors$',
  '\.ckpt$',
  '\.pt$',
  '\.pth$',
  '\.onnx$',
  '\.bin$',
  '\.gguf$',
  '\.zip$',
  '\.7z$',
  '\.rar$',
  '\.png$',
  '\.jpg$',
  '\.jpeg$',
  '\.webp$',
  '\.gif$',
  '\.mp4$',
  '\.mov$',
  '\.avi$',
  '\.mkv$',
  '\.wav$',
  '\.mp3$',
  '\.flac$',
  '^Main/shared_state/ec2_lease\.json$'
)

$secretPatterns = @(
  'GITHUB_TOKEN\s*=',
  'CIVITAI_TOKEN\s*=',
  'AWS_ACCESS_KEY_ID\s*=',
  'AWS_SECRET_ACCESS_KEY\s*=',
  'AWS_SESSION_TOKEN\s*=',
  'ghp_[A-Za-z0-9_]{20,}',
  'github_pat_[A-Za-z0-9_]{20,}',
  'AKIA[0-9A-Z]{16}',
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'
)

$staged = git diff --cached --name-only
if (-not $staged) {
  exit 0
}

$failed = $false
foreach ($file in $staged) {
  $normalized = $file -replace '\\', '/'
  foreach ($pattern in $blockedNamePatterns) {
    if ($normalized -match $pattern) {
      Write-Error "Blocked staged file: $file"
      $failed = $true
    }
  }

  if (Test-Path -Path $file -PathType Leaf) {
    $ext = [System.IO.Path]::GetExtension($file).ToLowerInvariant()
    if ($ext -in @(".md", ".json", ".ps1", ".psm1", ".txt", ".yml", ".yaml", ".gitignore", "")) {
      $text = Get-Content -Path $file -Raw -ErrorAction SilentlyContinue
      foreach ($pattern in $secretPatterns) {
        if ($text -match $pattern) {
          Write-Error "Potential secret pattern found in staged file: $file"
          $failed = $true
        }
      }
    }
  }
}

if ($failed) {
  Write-Error "Pre-commit check failed. Remove blocked files or secrets from the index."
  exit 1
}

exit 0

