# Lane 2 Main Flow Contact Wiring Revalidation (2026-07-04T16:52:20Z)

- Evidence: C:/Comfy_UI_Lora/5_session_worktrees/Lane_2/Lane_2/evidence_records/lane2_spatial_contact_revalidation_evidence_20260704_180500.json
- Contact QA source: C:/Comfy_UI_Lora/5_session_worktrees/Lane_2/Lane_2/contact_mask_pixel_qa/20260704_180500/lane2_contact_mask_pixel_qa_20260704_180500.json
- Audit source: C:/Comfy_UI_Lora/5_session_worktrees/Lane_2/Lane_2/main_flow_spatial_asset_audit/20260704_180500/lane2_main_flow_spatial_asset_audit_20260704_180500.json
- Snapshot hash: 5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9

## Actioning Matrix
| Edge | Suggested state | Why | Next action |
| --- | --- | --- | --- |
| fallback_actor_hand_to_receiver_butt | PASS_LOCAL | Local geometry preflight remains pass; depth/occlusion is geometry-only and still requires runtime visual | Keep gated to runtime acceptance while unchanged |
| fallback_actor_hand_to_receiver_breast | PASS_LOCAL | Local geometry preflight remains pass; depth/occlusion is geometry-only and still requires runtime visual | Keep gated to runtime acceptance while unchanged |
| B.left_to_A.left_breast_side_push | BLOCKED_SOURCE | Still blocked: zero/off per-hand placeholders (node 1052) | Do not enable until nonzero same-scene left/right split source is supplied |
| B.right_to_A.right_breast_side_push | BLOCKED_SOURCE | Still blocked: zero/off per-hand placeholders (node 1053) | Do not enable until nonzero same-scene right split source is supplied |
| B.left_to_A.left_butt_squeeze | BLOCKED_SOURCE | Still blocked: zero/off per-hand placeholders (node 1051) | Do not enable until nonzero same-scene left split source is supplied |
| B.right_to_A.right_butt_squeeze | BLOCKED_SOURCE | Still blocked: zero/off per-hand placeholders (node 1054) | Do not enable until nonzero same-scene right split source is supplied |

## Runtime Gate
- Current hash remains unchanged; Lane 4 + Lane 5 strict runtime/hand/contact visual acceptance required before final claim.

## Actor Body / Full Collision
- Keep node-1009 path in disabled/full-body mode until trusted `character_b_body_mask.png` source is provided.