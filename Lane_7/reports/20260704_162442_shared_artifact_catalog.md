# Lane 7 Shared Artifact Catalog - 2026-07-04T16:24:42Z

## Scope

This catalog records current shared/untracked lane artifacts without deleting, reverting, staging, or reclassifying them.

## Git/Worktree Status

All seven lane worktrees were clean against their remotes at the Lane 7 status check:

- `lane/lane-1-main-flow`
- `lane/lane-2-spatial-contact`
- `lane/lane-3-model-assets`
- `lane/lane-4-runtime-ec2`
- `lane/lane-5-qa-tracker`
- `lane/lane-6-generation-presets`
- `lane/lane-7-integration-history`

The shared `C:\Comfy_UI_Lora\5_sessions` main worktree has untracked mirror/live artifacts. Counts by top-level directory:

| Top-level path | Untracked count |
| --- | ---: |
| `Lane_1` | 19 |
| `Lane_2` | 13 |
| `Lane_5` | 3 |
| `Lane_6` | 4 |
| `Main` | 1 |

## Shared Main Worktree Untracked Paths

```text
?? Lane_1/evidence/lane1_body_contact_actor_body_optional_20260704_161725.evidence.json
?? Lane_1/evidence/lane1_body_contact_actor_body_optional_20260704_161725.graph_trace.json
?? Lane_1/evidence/lane1_body_contact_actor_body_optional_20260704_161725.post_validation.json
?? Lane_1/evidence/lane1_lane2_contact_control_wiring_20260704_111053.evidence.json
?? Lane_1/evidence/lane1_lane2_contact_control_wiring_20260704_111053.post_validation.json
?? Lane_1/evidence/lane1_lane2_contact_control_wiring_20260704_111053.pre_validation.json
?? Lane_1/evidence/lane1_lane2_contact_control_wiring_20260704_111053.runtime_binding.json
?? Lane_1/evidence/lane1_main_flow_hash_reconciliation_20260704_162137.evidence.json
?? Lane_1/evidence/lane1_main_flow_hash_reconciliation_20260704_162137.hash_chronology.json
?? Lane_1/hand_reviews/
?? Lane_1/history/
?? Lane_1/issues/
?? Lane_1/reports/
?? Lane_1/requests/lane1_to_lane2_actor_body_segmentation_source_20260704_161725.json
?? Lane_1/requests/lane1_to_lane2_per_hand_mask_assets_20260704_111053.json
?? Lane_1/requests/lane1_to_lane3_post_contact_model_visibility_20260704_111053.json
?? Lane_1/requests/lane1_to_lane3_remaining_main_flow_model_visibility_20260704_161725.json
?? Lane_1/requests/lane1_to_lane5_main_flow_hash_reconciliation_audit_20260704_162137.json
?? Lane_1/responses/
?? Lane_2/body_contact_slot_validation/
?? Lane_2/evidence_records/lane2_body_contact_slot_validation_evidence_20260704_160416.json
?? Lane_2/evidence_records/lane2_main_flow_spatial_asset_audit_evidence_20260704_162200.json
?? Lane_2/evidence_records/lane2_strict_hand_reference_evidence_20260704_160416.json
?? Lane_2/hand_reviews/
?? Lane_2/history/
?? Lane_2/issues/
?? Lane_2/lane1_requests/lane2_to_lane1_body_contact_slot_request_20260704_160416.md
?? Lane_2/lane1_requests/lane2_to_lane1_spatial_asset_audit_request_20260704_162200.md
?? Lane_2/lane1_responses/
?? Lane_2/main_flow_spatial_asset_audit/
?? Lane_2/reports/
?? Lane_2/strict_hand_reference/
?? Lane_5/history/
?? Lane_5/issues/
?? Lane_5/reports/
?? Lane_6/hand_reviews/
?? Lane_6/history/
?? Lane_6/issues/
?? Lane_6/reports/
?? Main/shared_state/ec2_requests/
```

## Pending EC2 Requests

Pending files under `C:\Comfy_UI_Lora\5_sessions\Main\shared_state\ec2_requests`:

- `20260704_160530_Lane_6_sdxl_safe_adult_clothed_low_vram_candidate.json`
- `20260704_162157_Lane_6_sdxl_safe_adult_clothed_low_vram_v1_1_candidate.json`

The v1.1 request states that it supersedes the v1 request and is bound to current Main Flow SHA256 `273158b6b84cefc67a706ac1c4656d90cfbebf04f0890a9230dd526475d5b96d`.

Processed request files:

- `processed\20260704_155047_Lane_3_model_lora_llm_visibility.json`
- `processed\20260704_155047_Lane_3_model_lora_llm_visibility.resolution.json`

Lane 4's processed resolution reports:

- ComfyUI `/system_stats`, `/queue`, and `/object_info`: passed
- Requested LoRAs visible: 22/22
- Remote LoRA paths size matched: 22/22
- EC2-hosted LLM endpoint: blocked, no loopback OpenAI-compatible service on checked ports
- Final state for that earlier window: EC2 stopped and lease free

## Handling Rule

Lane 7 did not stage, delete, revert, or edit owner-lane artifacts. Owner lanes keep authority over their mirrored artifacts and tracker/evidence decisions.
