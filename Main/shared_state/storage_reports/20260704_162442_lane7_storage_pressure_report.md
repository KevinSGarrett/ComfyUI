# Lane 7 Storage Pressure Report - 2026-07-04T16:24:42Z

## Summary

Storage pressure is a priority integration risk.

- C: free space: 8.99 GB
- C: free percent: 0.94 percent
- Risk level: `critical`
- Cleanup authority: Lane 4 only
- Lane 7 action: report and route, no cleanup

## EC2 Lease Constraint

Earlier lease-file check showed:

- `lease_state`: `held`
- `owner_lane`: `Lane_4`
- `purpose`: `Lane 6 safe adult clothed low-VRAM SDXL candidate request 20260704_160530`
- `last_heartbeat_utc`: `2026-07-04T16:22:40.4659999Z`

No cleanup apply may run while the EC2 lease is held. Lane 4 must first stop EC2, verify stopped/no public network fields or record an exact AWS-state blocker, and release the lease.

Latest lease-file check at `2026-07-04T11:28:57-05:00` showed `lease_state: free`. Lane 4 thread tail then reported AWS `RequestExpired`/expired credentials after the stop request, so final EC2 terminal state still needs owner-lane proof or an explicit blocker. Lane 4 also reported that cleanup dry-run was in progress.

## Mirror Sizes

| Path | Exists | Size |
| --- | --- | --- |
| `C:\Comfy_UI\EC2_Mirror` | yes | 202.351 GB |
| `C:\Comfy_UI\_ec2sd` | yes | 12.479 GB |

## Candidate Date-Stamped Snapshot Cleanup Targets

| Candidate | Size | Last write | Constraint |
| --- | --- | --- | --- |
| `C:\Comfy_UI\EC2_Mirror\20260628_211600` | 202.351 GB | 2026-06-28 16:46:06 local | Lane 4 must confirm stale snapshot and not active live sync. |
| `C:\Comfy_UI\_ec2sd\20260701_125027` | 12.479 GB | 2026-07-01 07:50:27 local | Lane 4 must confirm stale snapshot and not active live sync. |

Estimated reclaim if both are confirmed safe: 214.830 GB.

## Required Cleanup Constraints

Lane 4 must follow `C:\Comfy_UI_Lora\5_sessions\Main\CLEANUP_POLICY.md`.

Mandatory constraints:

- No apply while the EC2 lease is held.
- Dry-run first.
- Record candidate paths, sizes, and ages.
- Confirm every candidate is under an allowed cleanup root.
- Confirm no candidate is under a protected root.
- Confirm no candidate is part of an active EC2 lease/live sync.
- Apply only with explicit apply command after dry-run review.
- Save cleanup evidence manifest/report.
- Do not delete protected roots, model files, workflows, trackers, evidence, generated media, credentials, SSH keys, raw credentials, or secret-bearing files.

Relevant allowed EC2 snapshot roots under storage pressure:

- `C:\Comfy_UI\EC2_Mirror\YYYYMMDD_HHMMSS`
- `C:\Comfy_UI\_ec2sd\YYYYMMDD_HHMMSS`

Protected roots include:

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

## Exact Lane 4 Cleanup Request

After Lane 4 confirms EC2 is stopped, public IP/DNS are absent or records the exact AWS credential blocker, and confirms the lease is free:

1. Run dry-run summary:

```powershell
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 1 -IncludeEc2MirrorSnapshots -SummaryOnly
```

2. Verify the dry-run explicitly lists only safe stale candidates, including the two candidate snapshots above if they are stale:

```text
C:\Comfy_UI\EC2_Mirror\20260628_211600
C:\Comfy_UI\_ec2sd\20260701_125027
```

3. If and only if the dry-run confirms the candidates are safe, not protected, not active, not needed for the current live window, and AWS/runtime state is safe enough to exclude active live sync, run the apply summary:

```powershell
C:\Comfy_UI_Lora\5_sessions\Main\scripts\safe_cleanup.ps1 -Lane Lane_4 -OlderThanDays 1 -IncludeEc2MirrorSnapshots -SummaryOnly -Apply
```

4. Save cleanup evidence under Lane 4-owned evidence/report paths and report final C: free space.

Lane 7 did not run cleanup dry-run and did not delete anything.
