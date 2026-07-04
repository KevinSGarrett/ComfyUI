# Git And Worktree Setup

This coordination root is designed to become a small Git repository separate from heavy ComfyUI models, generated media, and credentials.

GitHub target:

`https://github.com/KevinSGarrett/ComfyUI.git`

Do not put `GITHUB_TOKEN` in the remote URL. If GitHub authentication is needed, use `gh auth login`, `GITHUB_TOKEN`, or a credential manager without printing the token.

## Local Layout

- Main coordination checkout: `C:\Comfy_UI_Lora\5_sessions`
- Lane worktrees: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_1` through `Lane_6`
- Branches:
  - `main`
  - `lane/lane-1-main-flow`
  - `lane/lane-2-spatial-contact`
  - `lane/lane-3-model-assets`
  - `lane/lane-4-runtime-ec2`
  - `lane/lane-5-qa-tracker`
  - `lane/lane-6-generation-presets`

## Setup Commands

Run:

```powershell
C:\Comfy_UI_Lora\5_sessions\Main\scripts\setup_worktrees.ps1
```

That script initializes the coordination Git repo if needed, installs local hooks, creates an initial commit when there is no history, configures the GitHub remote, and creates the six lane worktrees.

## Important Boundary

These worktrees track the coordination system, not the entire raw `C:\Comfy_UI` runtime workspace. The raw workspace contains credentials, large models, generated media, EC2 mirrors, and other files that must not be bulk-added to Git.

If the project source itself later needs a full Git migration, create a curated project repo plan first with a strict `.gitignore`, secret scan, model/media exclusion, and a staged commit strategy.

