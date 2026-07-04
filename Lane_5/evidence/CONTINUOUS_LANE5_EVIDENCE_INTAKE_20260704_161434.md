# Continuous Lane 5 Evidence Intake - 20260704_161434

- Created UTC: 2026-07-04T16:14:34.250419Z
- Canonical Main Flow: `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- Current Main Flow SHA256: `44f366f162a937b10c2d7157c5f0b668e1d27bdfdb93698a6181981ce4a3dd22`
- Latest tracker audited: `C:\Comfy_UI\Implementation\trackers\wave42_working_tracker_20260704_105253.csv`
- Tracker snapshot created: no
- Reason: new direct evidence is structural/provisional and does not prove exact tracker row completion.

## Verdict

No tracker rows were promoted or re-blocked in this intake slice. Lane 1 produced valid structural Main Flow contact-control wiring evidence, but its own QA blocks runtime readiness on missing per-hand mask files, remaining model visibility, and no live validation. Lane 6 produced valid preset/provider-schema evidence, but the preset references the previous Main Flow hash and has no generated candidate media.

## Counts

- Reviewed artifacts: 10
- Schema-valid evidence records: 4
- Non-schema/support artifacts: 6
- Tracker status counts: {'Verified Complete': 12082, 'Blocked - Model Asset': 744, 'Blocked - External API': 61}

## Preserved Rows

- `ART-0914`, `WFLOW-00053`, and `IMPL-00079` remain blocked because structural wiring/contact assets do not prove workflow import/runtime smoke evidence.
- `ART-0890` remains unchanged: it was already verified for LOW_VRAM API artifact binding only; Lane 6 did not prove a live low-VRAM render or current-hash candidate.

## Evidence Mapping

| Evidence | Lane | Schema | Lane 5 verdict | Rows | Next action |
| --- | --- | --- | --- | --- | --- |
| `lane1_contact_control_wiring` | Lane_1 | valid | main_flow_structural_candidate_preserve_runtime_blockers | ART-0914;WFLOW-00053;IMPL-00079 | Lane 2 must provide four per-hand masks; Lane 3 must resolve 10 unique model references; Lane 4 must live-validate current Main Flow before runtime/import rows can move. |
| `lane1_contact_runtime_binding_template` | Lane_1 | support/non-schema | support_only_not_promotable | none | Use as support for Lane 4 runtime request after per-hand masks and model visibility are resolved. |
| `lane1_request_per_hand_masks` | Lane_1 | support/non-schema | blocker_request_not_promotable | none | Lane 2 creates the four PNGs or gives exact substitute paths for Lane 1 to bind. |
| `lane1_request_post_contact_model_visibility` | Lane_1 | support/non-schema | blocker_request_not_promotable | none | Lane 3 returns direct file/catalog visibility evidence or corrected dropdown-relative filenames. |
| `lane2_strict_hand_reference_evidence` | Lane_2 | valid | dependency_resolved_no_runtime_or_tracker_promotion | none | Lane 1 reruns structural validation and Lane 4 validates strict-hand runtime only after a justified request. |
| `lane2_body_contact_slot_validation` | Lane_2 | support/non-schema | partial_asset_support_with_remaining_mask_blocker | none | Lane 1 either makes node 1009 optional for actor-hand-only mode or Lane 2 receives/provides actor body segmentation; Lane 2 still owes per-hand masks for nodes 1051-1054. |
| `lane2_body_contact_slot_request` | Lane_2 | support/non-schema | coordination_only_not_promotable | none | Lane 1 decides optional actor-hand-only mode or supplies actor body segmentation source. |
| `lane6_sdxl_low_vram_preset` | Lane_6 | valid | preset_exists_but_runtime_and_current_hash_not_proven | ART-0890 | Lane 6 should rebase/regenerate preset trace against current Main Flow hash or Lane 4 should return live candidate evidence/blocker for the exact workflow version. |
| `lane6_provider_trace_schema` | Lane_6 | valid | advisory_schema_pass_no_tracker_promotion | none | Use schema for future LLM advisory provenance; require downstream Main Flow/runtime evidence for promotions. |
| `lane6_to_lane5_handoff` | Lane_6 | support/non-schema | handoff_support_preserve_provisional_status | none | Lane 5 records no tracker promotion and waits for Lane 4/Lane 3 direct evidence. |

## Main Flow Convergence Notes

- Current canonical workflow hash is `44f366f162a937b10c2d7157c5f0b668e1d27bdfdb93698a6181981ce4a3dd22` after Lane 1 contact-control wiring.
- Lane 6 preset evidence references prior hash `eee910f1d00a6858abc67a27ea783c43c8ad876fd60f6b26865bced39bc647c0`; treat it as stale for current-canonical candidate readiness until rebased or validated.
- Missing per-hand mask files and model references are direct blockers, not paperwork blockers.
- Self-hosted LLM/provider-schema evidence remains advisory unless downstream runtime/candidate evidence proves a row.

## Files

- Candidate CSV: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\continuous_lane_evidence_intake_20260704_161434.csv`
- Manifest: `C:\Comfy_UI\Implementation\manifests\promotion_quality_audit\continuous_lane_evidence_intake_20260704_161434.json`
- Evidence record: `C:\Comfy_UI\Implementation\evidence\promotion_quality_audit\lane5_continuous_evidence_intake_evidence_20260704_161434.json`
