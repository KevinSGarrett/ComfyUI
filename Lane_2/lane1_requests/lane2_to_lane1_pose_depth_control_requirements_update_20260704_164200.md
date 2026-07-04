# Lane 2 — Pose/Depth Control Requirements Update (2026-07-04T16:42:00Z)

Lane 1 request: keep strict body-contact pose/depth assumptions explicit for current hash until runtime and visual evidence lands.

## Current state

- `WAVE42_MAIN_FLOW_20260702.json` hash: `5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`
- Pixel QA confirms current depth/soft-body contact maps are non-empty for local geometry checks, but does not validate depth ordering as foreground/background.
- Depth luma numbers used were sampled locally and should be treated as relative geometry signals only:
  - fallback actor-hand to receiver butt: actor mean `9.767588`, receiver mean `57.814341`, contact mean `35.891546`, pressure mean `38.059780`
  - fallback actor-hand to receiver breast: actor mean `9.767588`, receiver mean `102.583984`, contact mean `35.891546`, pressure mean `38.059780`

## Wiring request to Main Flow control semantics

- Keep strict visual/contact acceptance decisions out of local pose/depth checks.
- Use local pose/depth checks only for preflight thresholds:
  - actor-contact overlap over actor `>= 0.06`
  - contact-zone containment by dilated actor/receiver/shadow `>= 0.92`
  - pressure + indentation receiver containment `>= 0.97` on selected receiver surface for provisional pass only
- Preserve node `1009` actor-body zero/off only as an intentional fallback path (`actor_hand_only_contact_v1`) and not as validated full-body collision proof.
- Preserve named per-hand edges as blocked unless a same-scene nonzero left/right split source exists.

## Expected acceptance mapping

- Provisional geometry pass is currently available for fallback butt/breast actor-hand edges.
- Runtime handoff remains required for lane-level acceptance of:
  - per-hand named edge quality
  - occlusion/depth foreground ordering
  - final anatomical correctness.

## Evidence references

- Depth/contact artifact: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\contact_mask_pixel_qa\20260704_163800\lane2_contact_mask_pixel_qa_20260704_163800.json`
- Evidence record: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\evidence_records\lane2_contact_mask_pixel_qa_evidence_20260704_163800.json`
- Lane 1 proof of placeholder status: `C:\Comfy_UI_Lora\5_sessions\Lane_1\responses\lane1_to_lane2_per_hand_provenance_ack_20260704_164031.json`
