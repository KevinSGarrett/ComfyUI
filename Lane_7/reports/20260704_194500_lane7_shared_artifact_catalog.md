# Lane 7 Shared Artifact Catalog - 2026-07-04T19:45:00Z

## Inventory scope

This pass catalogs untracked or new shared artifacts in `C:\Comfy_UI_Lora\5_sessions` from current `git status --short` output, without any deletions/rewrites.

## Counts
- Total untracked entries in `C:\Comfy_UI_Lora\5_sessions`: `85`
- Top directory buckets:
  - `Lane_1\evidence`: `18`
  - `Main\reports`: `17`
  - `Lane_2`: `11`
  - `Lane_1\requests`: `8`
  - `Lane_2\evidence_records`: `6`
  - `Lane_7`: `6`
  - `Lane_1`: `5`
  - `Lane_6`: `4`
  - `Lane_2\lane1_requests`: `4`
  - `Main\shared_state`: `3`
  - `Lane_5`: `3`

## Notable newly visible examples (latest slice)

- `Lane_1/requests/lane1_to_lane2_actor_body_segmentation_source_20260704_161725.json`
- `Lane_1/requests/lane1_to_lane4_current_hash_runtime_validation_20260704_163216.json`
- `Lane_1/evidence/lane1_body_contact_actor_body_optional_20260704_161725.evidence.json`
- `Lane_2/evidence_records/lane2_main_flow_spatial_asset_audit_evidence_20260704_162200.json`
- `Lane_6/reports/20260704_181300_lane6_status.md`
- `Main/reports/20260704_194500_lane7_compact_end_to_end_dashboard.md`
- `Main/reports/20260704_193500_lane7_compact_end_to_end_dashboard.md`
- `Main/shared_state/storage_reports/20260704_194500_lane7_storage_pressure_report.md`
- `Main/shared_state/resume_packets/20260704_194500_usage_limit_resume_packet.md`

## Handling

- No shared artifacts were deleted, moved, or modified by cleanup.
- No generated media, models, credentials, or tracker files were touched.
- Cleanup and EC2 operations remain owner-only via Lane 4 (`lane4_*` evidence and request records).
