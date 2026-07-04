# Lane 2 - Contact Runtime Control Contract (2026-07-04T18:15:00Z, refreshed 2026-07-04T18:15:00Z)

## Scope
- Contract for strict body-contact runtime semantics in
  `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
  at hash `5C67A23D1F70A6E7A5687E99E58F73EA475A172B4736F32D192AB3929BC35EC9`.

## Current authoritative state (local preflight, 181500)
- `main_flow` strict body-contact slots resolve and load; runtime acceptance is still pending.
- Per-hand left/right split masks remain zero/off placeholders:
  - nodes `1051-1054` (`character_a_left_hand_mask`, `character_a_right_hand_mask`, `character_b_left_hand_mask`, `character_b_right_hand_mask`)
- Actor-body collision source remains zero/off:
  - node `1009` (`character_b_body_mask`)
- Local contact geometry preflight shows:
  - pass: fallback actor-hand edges
  - blocked: named per-hand edges
- Strict visual hand/contact and depth-order acceptance has not been executed by Lane 2.

## Wiring contract
1. Keep named per-hand edges explicitly blocked until same-scene nonzero split masks are supplied:
   - `B.left_to_A.left_breast_side_push`
   - `B.right_to_A.right_breast_side_push`
   - `B.left_to_A.left_butt_squeeze`
   - `B.right_to_A.right_butt_squeeze`
2. Keep node `1009` actor-body path (`character_b_body_mask.png`) in explicit off/placeholder semantics for `actor_hand_only_contact_v1` unless a trustworthy same-scene actor-body mask is supplied.
3. Keep all named strict-body contact hand/contact/pose/depth runtime claims gated behind:
   - Lane 4 runtime capture with current hash
   - Lane 5 strict visual acceptance
4. Preserve `strict_hand_detail_input.png` reference binding (existing source remains present at
   `C:\Comfy_UI\Input_References\main_flow\strict_hand_detail_input.png`).

## Required runtime evidence before any claim upgrade
- `main_flow` current-hash load check (all strict body-contact references resolve).
- Runtime output artifacts for nodes:
  - per-hand edge nodes (`1051-1054`) showing either intentional zeros or valid nonzero splits.
  - node `1009` actor-body handling behavior under current wiring.
- Depth/occlusion sanity checks with generated strict preview(s) and hand anatomy continuity.

## Direct Next Action for Lane 1
- Preserve a strict placeholder/blocked state for named per-hand edges and actor-body full-collision unless the two conditions above are both satisfied.
- If trusted same-scene replacements for all required masks arrive later, un-block only the exact edges enabled by the replacement coverage and re-run hash-aware Main Flow validation.
