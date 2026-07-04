# Lane 2 to Lane 1: Current Main Flow Spatial Asset Audit Request

Timestamp: 2026-07-04T16:22:00Z
Requesting lane: Lane_2
Target workflow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
Workflow SHA256 audited: `273158B6B84CEFC67A706AC1C4656D90CFBEBF04F0890A9230DD526475D5B96D`

## Audit Result

Lane 2 audited the current Main Flow spatial assets after the workflow changed from the earlier body-slot evidence hash. The audit covered 90 spatial asset nodes and found:

- 4 missing per-hand mask assets at nodes 1051-1054.
- 1 zero-valued actor body mask at node 1009.
- Depth, normal, pressure, indentation, contact shadow, and occlusion masks/images exist and are nonzero.
- ControlNet model requirements are listed but not model-visibility-proven by Lane 2.

Audit artifact:

`C:\Comfy_UI_Lora\5_session_worktrees\Lane_2\Lane_2\main_flow_spatial_asset_audit\20260704_162200\lane2_main_flow_spatial_asset_audit_20260704_162200.json`

Artifact SHA256:

`5E78529FB1A4E4C64D7380723388114DFD63991BAF895F13616D0BB2EBEED8C4`

## Missing Node Inputs

Please decide the intended source or graph semantics for these current Main Flow nodes:

- Node 1051: `main_flow/body_contact_slots/character_a_left_hand_mask.png`
- Node 1052: `main_flow/body_contact_slots/character_a_right_hand_mask.png`
- Node 1053: `main_flow/body_contact_slots/character_b_left_hand_mask.png`
- Node 1054: `main_flow/body_contact_slots/character_b_right_hand_mask.png`

## Semantic Conflict Found

The active `body_contact_slots\body_contact_base_input.png` hash is:

`8DAD144442821B3AB1E461ADA539A3420C446670FC02A9DAC540726E385DE523`

That active base matches the `lower_hip_contact` preset. The available strict side-push left/right hand masks under `body_contact_presets\clothed_breast_side_push_strict_v1` belong to a different base hash:

`4E76DCAF4DA8BAFD837102B7A17AFB05D734A2B60CD3D2F7B7052BDD0851354B`

Lane 2 did not copy strict side-push left/right masks into the active slot folder because that would mix masks across scenes and create false spatial evidence.

## Requested Lane 1 Decision

Please choose one path:

1. Keep the active `lower_hip_contact` slot set. If so, define whether nodes 1051-1054 should be optional/disabled, zero-placeholder/off masks, or new same-scene left/right masks derived from a provided source.
2. Switch the active strict body-contact slot group to the strict side-push preset. If so, tell Lane 2 the exact mapping from strict-v1 files to Character A/B left/right node names before materialization.
3. Provide/request a new same-scene per-hand segmentation source for the current active base image.

Node 1009 also remains blocked:

- Node 1009: `main_flow/body_contact_slots/character_b_body_mask.png` is present but zero-valued.

After Lane 1 resolves nodes 1009 and 1051-1054 semantics, Lane 2 can materialize non-ambiguous masks or explicit zero/off placeholders, and Lane 4 can runtime-validate the graph during a justified live window.
