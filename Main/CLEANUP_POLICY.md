# Cleanup Policy

Cleanup must be conservative. Disk pressure is real, but model files, evidence, trackers, workflows, credentials, and generated proof must not be deleted casually.

## Allowed Cleanup Roots

Cleanup scripts may operate only inside these roots unless a lane-specific claim explicitly expands the scope:

- `C:\Comfy_UI\_tmp`
- `C:\Comfy_UI\Runtime\temp`
- `C:\Comfy_UI\outputs\temp`
- `C:\Comfy_UI\EC2_Mirror\stale`
- `C:\Comfy_UI\_ec2sd\stale`
- `C:\Comfy_UI_Lora\5_sessions\Lane_1\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_2\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_3\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_4\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_5\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_6\scratch`
- `C:\Comfy_UI_Lora\5_sessions\Lane_7\scratch`
- `C:\Comfy_UI_Lora\5_session_worktrees\*\tmp`

Under storage pressure, Lane 4 may also clean old date-stamped EC2 mirror snapshots only through `safe_cleanup.ps1 -IncludeEc2MirrorSnapshots`:

- `C:\Comfy_UI\EC2_Mirror\YYYYMMDD_HHMMSS`
- `C:\Comfy_UI\_ec2sd\YYYYMMDD_HHMMSS`

These snapshots are cleanup candidates only if they are older than the selected cutoff, are not part of an active EC2 lease/live sync, and Lane 4 records a cleanup evidence manifest.

## Protected Roots

Never delete from these roots via automated cleanup:

- `C:\Comfy_UI\.env`
- `C:\Comfy_UI\*.pem`
- `C:\Comfy_UI\Implementation\workflows`
- `C:\Comfy_UI\Implementation\trackers`
- `C:\Comfy_UI\Implementation\evidence`
- `C:\Comfy_UI\Runtime_Data\models`
- `C:\Comfy_UI\models`
- `C:\Comfy_UI_Lora\models`
- `C:\Comfy_UI_Lora\Reference_Images`
- `C:\Comfy_UI_Lora\Reference_Images_002`
- `C:\Comfy_UI_Lora\Reference_Images_Organized`

## Required Cleanup Procedure

1. Run cleanup in dry-run mode.
2. Record candidate paths, sizes, and age.
3. Confirm all candidates are under allowed roots.
4. Confirm no candidate path is under a protected root.
5. For EC2 mirror snapshots, confirm the shared EC2 lease is not held before applying cleanup.
6. Delete only with an explicit `-Apply` run.
7. Save a cleanup evidence record.

Use:

```powershell
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 7
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 7 -Apply
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 1 -IncludeEc2MirrorSnapshots -SummaryOnly
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 1 -IncludeEc2MirrorSnapshots -SummaryOnly -Apply
```

## Usage Limit Awareness

Codex Desktop usage limits can pause or stop lane progress. If a lane stops because the 5-hour or weekly usage window is exhausted, record a blocker with:

- lane id
- active task
- last evidence/report path
- exact next prompt to send after the user resets usage
- whether EC2 or local runtime is still active

Usage reset is manual. Do not treat a usage stop as completed project work.
