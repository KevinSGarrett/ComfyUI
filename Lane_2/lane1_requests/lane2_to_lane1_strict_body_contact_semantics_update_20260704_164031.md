# Lane 2 — Strict Body-Contact Semantics Update (2026-07-04T16:40:31Z)

Lane 1 request: preserve explicit off-control semantics for strict body-contact until trustworthy same-scene masks and runtime acceptance replace them.

## Current truth for this hash

- `WAVE42_MAIN_FLOW_20260702.json` current hash: `5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`
- Nodes `1051-1054` resolve correctly to exact-name files but are all-zero/off placeholders.
- `character_b_body_mask.png` (`node 1009`) remains zero/off and is intentionally optional only for the actor_hand_only contact path.
- New Lane 2 pixel QA is provisional for geometry only: fallback actor-hand-to-butt/breast overlap metrics are present; named per-hand edges are blocked.

## Wiring actions requested

- Keep current graph semantics.
- Do not mark any of these named per-hand edges as proven:
  - `B.left_to_A.left_breast_side_push`
  - `B.right_to_A.right_breast_side_push`
  - `B.left_to_A.left_butt_squeeze`
  - `B.right_to_A.right_butt_squeeze`
- Keep named named per-hand edges blocked unless a trustworthy same-scene nonzero A/B left-right split source arrives.
- Keep node 1009 actor-body blocker behavior explicit:
  - accept only as intentional off-control for actor_hand_only mode, or
  - request replacement only when a same-scene actor-body source is provided.

## Evidence references

- Pixel QA artifact: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\contact_mask_pixel_qa\20260704_163800\lane2_contact_mask_pixel_qa_20260704_163800.json`
- Evidence record: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\evidence_records\lane2_contact_mask_pixel_qa_evidence_20260704_163800.json`
- Lane 1 provenance acknowledgment: `C:\Comfy_UI_Lora\5_sessions\Lane_1\responses\lane1_to_lane2_per_hand_provenance_ack_20260704_164031.json`
