# Lane 2 Contact-Control Package

This package defines the reusable spatial truth layer for strict body contact and soft-body controls. It is structural evidence, not a live runtime pass.

Files:

- `lane2_contact_control_artifact_20260704_154905.json`: canonical mask, pose, depth, normal, occlusion, contact-pair, soft-body, and QA requirements.
- `..\..\lane1_requests\lane2_to_lane1_contact_control_wiring_request_20260704_154905.md`: request for Lane 1 graph wiring.

Source state:

- Main Flow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- SHA256: `B8D0899CE45845F97F8540DFB379D9E8FD8987B42A65A123D67A249880E72E13`
- Nodes reviewed: 991-1050
- EC2: not started or stopped

Key result:

The current workflow already has a strict contact group with combined masks and soft-body controls. Lane 2 adds an explicit contract for per-character masks, per-hand masks, active contact-zone masks, depth/normal/occlusion inputs, contact-pair graph edges, and collision/deformation QA. Lane 1 still needs to wire left/right per-hand slots and expose the soft-body controls for runtime/API use.
