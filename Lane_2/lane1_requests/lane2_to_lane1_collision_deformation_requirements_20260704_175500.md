# Lane 2 Collision/Deformation Requirements Update (2026-07-04T17:20:00Z)

- Source artifacts:
  - `Lane_2/evidence_records/lane2_collision_deformation_requirements_update_20260704_175500.json`
  - `Lane_2/contact_mask_pixel_qa/20260704_175000/lane2_contact_mask_pixel_qa_20260704_175000.json`
  - `Lane_2/contact_pair_graph/20260704_175000/lane2_contact_pair_graph_20260704_175000.json`

## Local-geometry acceptance rules (non-authoritative without runtime)

- Fallback actor-hand edges may pass preflight when:
  - `actor_contact_overlap_over_actor >= 0.06`
  - `contact_zone_contained_by_dilated_actor_receiver_shadow >= 0.92`
  - `pressure_inside_character_a_body_and_receiver >= 0.97`
  - `indentation_inside_character_a_body_and_receiver >= 0.97`

## Blocked edges (must remain disabled until same-scene masks arrive)

- `B.left_to_A.left_breast_side_push`
- `B.right_to_A.right_breast_side_push`
- `B.left_to_A.left_butt_squeeze`
- `B.right_to_A.right_butt_squeeze`

## Additional blockers

- `character_b_left_hand` / `character_b_right_hand` are still zero/off placeholders.
- `character_b_body_mask` (node 1009 path) remains zero/off; disable full-body collision/deformation as a final condition until a trustworthy source is provided.

## Runtime dependency

- This packet is geometry-only and does not establish final visual, depth, or occlusion correctness.
- Final strict acceptance remains pending:
  - Lane 4 strict body-contact runtime execution for the same Main Flow hash.
  - Lane 5 strict hand/contact visual review.
