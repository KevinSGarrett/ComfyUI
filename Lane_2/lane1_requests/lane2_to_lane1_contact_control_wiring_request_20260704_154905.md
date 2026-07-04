# Lane 2 To Lane 1 Wiring Request: Strict Contact Control

Created: 2026-07-04T15:49:05Z
Requesting lane: Lane_2
Target owner: Lane_1
Workflow reviewed: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
Workflow SHA256: `B8D0899CE45845F97F8540DFB379D9E8FD8987B42A65A123D67A249880E72E13`

## Current Finding

Main Flow already has a dormant strict body contact and soft-physics group at nodes 991-1050. It includes base image, pose reference, depth reference, normal reference, receiver/actor body masks, combined hand masks, contact-zone masks, pressure/indentation/shadow masks, DWPose/OpenPose, depth ControlNet, masked inpaint conditioning, and save nodes.

Lane 2 did not edit Main Flow and did not run EC2. The structural contact artifact is:

`C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\contact_control\20260704_154905\lane2_contact_control_artifact_20260704_154905.json`

## Requested Lane 1 Work

1. Add per-hand mask inputs, or wire an equivalent upstream split, for:
   - `main_flow/body_contact_slots/character_a_left_hand_mask.png`
   - `main_flow/body_contact_slots/character_a_right_hand_mask.png`
   - `main_flow/body_contact_slots/character_b_left_hand_mask.png`
   - `main_flow/body_contact_slots/character_b_right_hand_mask.png`

2. Preserve existing combined slots:
   - `character_a_hand_mask`
   - `character_b_hand_mask`
   - `character_b_actor_hand_mask`
   - `hand_contact_mask`

3. Add QA previews/saves for:
   - each per-hand mask
   - each active contact-pair edge
   - `soft_body_pressure_map`
   - `soft_body_indentation_mask`
   - `contact_shadow_mask`
   - `interaction_occlusion_order_mask`

4. Expose soft-body controls as graph widgets/reroutes mapped to the current nodes:
   - node 1036, `Strict Body Contact SDXL Hand LoRA`
   - node 1042, `Strict Body Contact OpenPose Apply`
   - node 1044, `Strict Body Contact Depth/Volume Apply`
   - node 1045, `Strict Body Contact Detail Sampler`

5. Add a note or metadata node near the strict body contact group that points to the Lane 2 contact-pair graph and records the active edge id in generation metadata.

6. Produce an API/runtime binding template that accepts:
   - base image
   - pose reference
   - depth reference
   - normal reference
   - per-character masks
   - per-hand masks
   - active contact-zone, pressure, indentation, shadow, and occlusion masks
   - selected contact-pair edge id
   - soft-body slider values

## Acceptance Criteria

Lane 1 completion should produce a backed-up Main Flow edit or an exact blocker. It should not claim runtime proof unless Lane 4 runs the graph and returns endpoint/output evidence. Required graph validation is structural import/open plus node/link integrity for the new slots.
