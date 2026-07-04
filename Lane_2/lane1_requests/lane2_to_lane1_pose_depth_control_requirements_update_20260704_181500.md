# Lane 2 - Pose/Depth + Contact-Pair Control Update (2026-07-04T16:58:00Z)

## Scope
- Scope: strict body-contact pose/depth preflight and contact-pair graph gating for
  `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`.
- Workflow SHA: `5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`

## Source artifacts (run 20260704_181500)
- Spatial asset audit: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\main_flow_spatial_asset_audit\20260704_181500\lane2_main_flow_spatial_asset_audit_20260704_181500.json`
- Contact pixel QA: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\contact_mask_pixel_qa\20260704_181500\lane2_contact_mask_pixel_qa_20260704_181500.json`
- Contact pair graph: `C:\Comfy_UI\Implementation\evidence\contact_physics\20260704_175000_lane2_contact_pair_graph\lane2_contact_pair_graph_20260704_175000.json`

## Updated contact-state matrix
| Edge | Suggested state | Why |
| --- | --- | --- |
| fallback_actor_hand_to_receiver_butt | PASS_LOCAL | Actor/receiver overlap and containment pass local geometry checks; depth ordering remains non-authoritative without runtime |
| fallback_actor_hand_to_receiver_breast | PASS_LOCAL | Actor/receiver overlap and containment pass local geometry checks; depth ordering remains non-authoritative without runtime |
| B.left_to_A.left_breast_side_push | BLOCKED_SOURCE | Per-hand placeholder (`1051`) is zero/off |
| B.right_to_A.right_breast_side_push | BLOCKED_SOURCE | Per-hand placeholder (`1052`) is zero/off |
| B.left_to_A.left_butt_squeeze | BLOCKED_SOURCE | Per-hand placeholder (`1053`) is zero/off |
| B.right_to_A.right_butt_squeeze | BLOCKED_SOURCE | Per-hand placeholder (`1054`) is zero/off |

## Pose/depth thresholds (local preflight only)
- `actor_contact_overlap_over_actor_min >= 0.06`
- `contact_zone_containment_min >= 0.92` (actor receiver contact-shadow dilate)
- `pressure_indent_receiver_min >= 0.97`
- `runtime_visual_required = true`

## Control semantics that remain in effect
- Keep node `1009` actor-body zero-off behavior explicit for `actor_hand_only_contact_v1` until trusted `character_b_body_mask.png` exists.
- Keep strict per-hand edges blocked in runtime activation until same-scene nonzero left/right split masks arrive.
- Keep strict hand/depth/occlusion final acceptance out of local geometry checks.

## Strict-hand dependency status
- `C:\Comfy_UI\Input_References\main_flow\strict_hand_detail_input.png` exists and matches prior provenance-based copy work.
- SHA256: `72FF596F5492A7876130F0BCA5677BEBB66DE08B92304D6B1F7ECB70A6534A0D`.
- Does not itself close strict visual acceptance.

## Direct next action for Main Flow wiring
1. Keep fallback actor-hand edges runtime-gated in active graph state.
2. Preserve node-1009 actor-body optional semantics.
3. Unblock named edges only after same-scene nonzero sources for nodes 1051-1054 are available.
4. Preserve blocker annotations for per-hand and actor-body collision dependencies in any active graph edit notes.

## Evidence record
- `C:\Comfy_UI\Implementation\evidence\contact_physics\20260704_181500_lane2_pose_depth_requirements\lane2_pose_depth_requirements_update_evidence_20260704_181500.json`