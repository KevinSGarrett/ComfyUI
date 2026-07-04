# Lane 7 Usage-Limit Resume Packet - 2026-07-04T16:24:42Z

## Current Usage-Limit Finding

No lane thread is currently observed as stopped or blocked by Codex Desktop 5-hour or weekly usage limits.

All seven Wave42 lane threads are accessible and active through local Codex thread metadata.

## Why This Packet Exists

This packet is a ready resume scaffold in case usage limits interrupt an active lane after this snapshot. Usage reset is manual. A usage stop is not project completion.

## Highest-Risk Mid-Flight Resume Points

### Lane 4: EC2 stop/release/storage cleanup

Use if Lane 4 is interrupted during the active live window or cleanup follow-up.

Resume prompt:

```text
Resume Lane 4 from usage-limit interruption. First read the current EC2 lease file at C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_lease.json and verify AWS EC2 state for i-0560bf8d143f93bb1 without printing secrets. If the lease is still held by Lane 4 or EC2 is running/stopping, prioritize stopping verification, no public IP/DNS proof, and lease release. Do not run cleanup apply until lease is released. Then process storage pressure through CLEANUP_POLICY.md with dry-run first, cleanup evidence required, and only stale date-stamped snapshot candidates under allowed roots.
```

Last known active task:

- Lane 4 reported a 768x768 PNG candidate was generated for Lane 6 v1 request.
- Lane 4 issued EC2 stop and the local lease file later showed `free`.
- Lane 4 reported AWS `RequestExpired`/expired credentials prevented final EC2 terminal-state proof.
- Lane 4 reported the cleanup dry-run was in progress.

### Lane 3: model-root hash reconciliation

Resume prompt:

```text
Resume Lane 3 from usage-limit interruption. Continue the compact reconciliation against the canonical Main Flow and model roots. Preserve the Main Flow hash used, finish hashing or file-id validation for large hardlinked assets, then publish evidence and any Lane 4 runtime visibility request. Do not start or stop EC2, do not print secrets, and do not claim final visibility until the evidence file is written and pushed.
```

Last known active task:

- Hashing large Flux/Z-Image/Qwen assets after targeted model-root hardlink placement.

### Lane 5: evidence audit

Resume prompt:

```text
Resume Lane 5 from usage-limit interruption. Poll for evidence newer than the last Lane 5 audit timestamp, especially Lane 6 v1.1 preset evidence and any Lane 4 candidate evidence. Apply strict direct-evidence and hand-review rules. Do not create tracker snapshots unless exact row-level acceptance criteria are directly proven.
```

Last known active task:

- Auditing Lane 6 v1.1 evidence and preserving no-promotion boundary because no candidate media exists in that evidence.

### Lane 6: candidate ingestion and hand review

Resume prompt:

```text
Resume Lane 6 from usage-limit interruption. Check whether Lane 4 has returned candidate evidence for the v1 or v1.1 SDXL safe adult clothed request. If candidate media exists, run strict adult/clothed and hand/anatomy visual review before any QA claim. If only v1 exists and v1.1 supersedes it, record whether a fresh current-hash v1.1 candidate is needed.
```

Last known active task:

- v1.1 preset/request is created and schema-valid.
- Local ComfyUI remains unavailable.

## Stable References

- Main Flow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- Current observed Main Flow SHA256: `273158B6B84CEFC67A706AC1C4656D90CFBEBF04F0890A9230DD526475D5B96D`
- Storage report: `Lane_7\storage_reports\20260704_162442_lane7_storage_pressure_report.md`
- Dashboard: `Lane_7\reports\20260704_162442_lane7_end_to_end_dashboard.md`
