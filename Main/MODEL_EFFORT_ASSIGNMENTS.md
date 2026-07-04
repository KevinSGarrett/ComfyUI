# Model And Effort Assignments

These are the intended Codex Desktop model and reasoning effort settings for the Wave42 lanes.

Use the strongest model for lanes where mistakes can corrupt shared architecture, QA status, runtime state, or evidence claims. When usage is low, follow `USAGE_BUDGET_POLICY.md` and reserve the strongest settings for high-risk decisions.

## Current Mode

Current mode is **emergency budget mode**.

Reason: the user reported usage dropping from about 60 percent to about 10 percent on 2026-07-04, then reported the system had already reached about 91 percent used after the first budget update. All lanes should use standard speed, finish only current atomic slices, write compact PM status, and pause for supervisor triggers until usage is reset or the user explicitly authorizes higher burn.

## Emergency-Budget Defaults

| Lane | Mission | Default model | Default effort | Escalation |
| --- | --- | --- | --- | --- |
| Lane_1 | Main Flow architecture and workflow graph wiring | `gpt-5.4` | `medium` | Escalate only for actual Main Flow edit or graph repair. |
| Lane_2 | Spatial, pose, mask, contact, depth, and soft-body controls | `gpt-5.4` | `medium` | Escalate only for strict visual hand/contact validity or irreversible asset decision. |
| Lane_3 | Models, LoRAs, Civitai assets, and self-hosted LLM route | `gpt-5.4` | `low` | Use `medium` for taxonomy; escalate only before EC2 model-ingest launch decisions or risky compatibility claims. |
| Lane_4 | EC2 runtime, deployment, sync, live validation, and cost control | `gpt-5.5` | `medium` | Escalate for active EC2 lease, cleanup apply, stop-state ambiguity, or EC2-only model-download execution. |
| Lane_5 | QA, evidence ingestion, tracker promotion, and re-blocking | `gpt-5.4` | `medium` | Escalate only for tracker mutation, re-block/promotion dispute, or visual QA acceptance. |
| Lane_6 | Candidate generation, presets, tuning, and AI_Front self-hosted LLM integration | `gpt-5.4` | `medium` | Escalate only for candidate/media QA, hand review, or runtime-readiness acceptance. |
| Lane_7 | Cross-lane integration, release history, usage/storage monitoring, and end-to-end dashboarding | `gpt-5.4` | `low` | Escalate only for release-critical contradiction, storage crisis, or usage-limit resume planning. |

## Critical-Budget Defaults

| Lane | Mission | Default model | Default effort | Escalation |
| --- | --- | --- | --- | --- |
| Lane_1 | Main Flow architecture and workflow graph wiring | `gpt-5.4` | `high` | `gpt-5.5/xhigh` for Main Flow edits, graph repair, contradictory workflow evidence. |
| Lane_2 | Spatial, pose, mask, contact, depth, and soft-body controls | `gpt-5.4` | `high` | `gpt-5.5/xhigh` for strict hand/contact visual validity or irreversible asset decisions. |
| Lane_3 | Models, LoRAs, Civitai assets, and self-hosted LLM route | `gpt-5.4` | `medium` | `gpt-5.4/high` for taxonomy; `gpt-5.5/xhigh` before EC2 model-ingest launch requests or risky compatibility claims. |
| Lane_4 | EC2 runtime, deployment, sync, live validation, and cost control | `gpt-5.5` | `high` | `gpt-5.5/xhigh` for EC2 live windows, cleanup apply, stop-state ambiguity, or model-download execution. |
| Lane_5 | QA, evidence ingestion, tracker promotion, and re-blocking | `gpt-5.4` | `high` | `gpt-5.5/xhigh` for tracker mutations, re-blocks, promotion disputes, or strict visual QA acceptance. |
| Lane_6 | Candidate generation, presets, tuning, and AI_Front self-hosted LLM integration | `gpt-5.4` | `high` | `gpt-5.5/xhigh` for candidate/media QA, hand review, or runtime-readiness acceptance. |
| Lane_7 | Cross-lane integration, release history, usage/storage monitoring, and end-to-end dashboarding | `gpt-5.4` | `medium` | `gpt-5.5/high` or `xhigh` only for release-critical contradiction, storage crisis, or usage-limit resume planning. |

## Normal-Budget Maximums

When usage is safely above 40 percent or the user explicitly authorizes higher usage, these are the maximum defaults:

| Lane | Model | Reasoning effort |
| --- | --- | --- |
| Lane_1 | `gpt-5.5` | `xhigh` |
| Lane_2 | `gpt-5.5` | `xhigh` |
| Lane_3 | `gpt-5.5` | `xhigh` |
| Lane_4 | `gpt-5.5` | `xhigh` |
| Lane_5 | `gpt-5.5` | `xhigh` |
| Lane_6 | `gpt-5.5` | `xhigh` |
| Lane_7 | `gpt-5.5` | `xhigh` |

## Dynamic Adjustment Policy

The emergency-budget table above is the current baseline. The supervisor must watch lane progress and adjust model/effort when the work changes shape.

Escalate to `xhigh` when a lane is doing any of the following:

- editing or validating `C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`
- deciding whether evidence justifies a tracker promotion or re-block
- opening, extending, or closing an EC2 live runtime window
- approving or applying EC2 mirror cleanup
- launching EC2-only Civitai/model download batches
- resolving cross-lane conflicts, shared claims, or contradictory evidence
- making model/runtime visibility decisions that affect Main Flow readiness
- making a safety, content, privacy, credential, or cost-control decision
- performing strict hand/anatomy/candidate-media QA

Strict autonomous QA still applies, but it no longer means blanket `xhigh` while usage is critical. It means every claim needs evidence, and risky decisions must escalate. Bounded inventory, formatting, manifest writing, model-card generation, and non-destructive evidence packaging should use lower effort.

Do not downgrade below the critical-budget table unless the user explicitly authorizes it. If a lane was initially created with higher settings, send a budget update before allowing low-value autonomous loops to continue.

## Current Supervisor Defaults

- Current mode is emergency budget mode.
- All lanes should run at standard speed.
- Lanes should finish current atomic slices, write compact PM status, then pause for a supervisor trigger.
- Hand review, candidate/media QA, Main Flow edits, EC2 live-window work, tracker truth decisions, cleanup apply, and model-ingest launch decisions must escalate to `xhigh`.
- Routine polling, inventory, report formatting, model-card generation, and no-op status reports should not use `xhigh`.
- The supervisor should record any intentional temporary escalation in a lane report or coordination summary.
