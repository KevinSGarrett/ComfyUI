# Lane 2 Main Flow Contact Pair Graph Update (2026-07-04T17:00:00Z)

- Source evidence: C:/Comfy_UI_Lora/5_session_worktrees/Lane_2/Lane_2/evidence_records/lane2_contact_pair_graph_evidence_20260704_180500.json
- Contact QA source: C:/Comfy_UI_Lora/5_session_worktrees/Lane_2/Lane_2/contact_mask_pixel_qa/20260704_180500/lane2_contact_mask_pixel_qa_20260704_180500.json
- Snapshot hash: 5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9

## Actioning Matrix
| Edge | Suggested state | Why | Next action |
| --- | --- | --- | --- |
| fallback_actor_hand_to_receiver_butt | PASS_LOCAL | Local geometry remains provisional pass; runtime/visual gate still required | Keep gated to runtime/visual acceptance in Lane 4+Lane 5 before full claim |
| fallback_actor_hand_to_receiver_breast | PASS_LOCAL | Local geometry remains provisional pass; runtime/visual gate still required | Keep gated to runtime/visual acceptance in Lane 4+Lane 5 before full claim |
| B.left_to_A.left_breast_side_push | BLOCKED_SOURCE | Still blocked: per-hand split mask still zero/off (node 1052) | Keep blocked until same-scene nonzero left/right split arrives |
| B.right_to_A.right_breast_side_push | BLOCKED_SOURCE | Still blocked: per-hand split mask still zero/off (node 1053) | Keep blocked until same-scene nonzero right split arrives |
| B.left_to_A.left_butt_squeeze | BLOCKED_SOURCE | Still blocked: per-hand split mask still zero/off (node 1051) | Keep blocked until same-scene nonzero left split arrives |
| B.right_to_A.right_butt_squeeze | BLOCKED_SOURCE | Still blocked: per-hand split mask still zero/off (node 1054) | Keep blocked until same-scene nonzero right split arrives |
