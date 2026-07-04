# Usage Budget Policy

## Purpose

The lane system must stay autonomous without burning the Codex usage budget through unnecessary polling, repeated deep reads, high-speed execution, or blanket `xhigh` reasoning.

The user reported usage dropping from about 60 percent to about 10 percent on 2026-07-04, and then reported usage had already reached about 91 percent used after the first budget update. Until the user resets usage or approves a larger budget, the system is in **emergency budget mode**.

## Standard Speed Requirement

All Codex Desktop lane sessions should run at **standard speed**, not accelerated/1.5x speed.

If a tool or UI exposes a speed control, set it to standard. If no speed control is exposed to the agent, apply the practical equivalent:

- lower default reasoning effort
- fewer autonomous follow-up prompts
- fewer simultaneous lane wakeups
- compact status artifacts only when state changes
- script-driven mechanical work instead of repeated LLM reasoning
- longer supervisor heartbeat cadence

## Budget Modes

| Mode | Remaining usage | Supervisor behavior |
| --- | ---: | --- |
| Normal | Above 40 percent | Use baseline lane settings, poll normally, keep reports current. |
| Conservation | 15-40 percent | Reduce polling, avoid broad reads, use lower effort for mechanical work, escalate only for risky decisions. |
| Critical | 15 percent or below | Poll lightly, wake only owner lanes for concrete next actions, stop no-op loops, prefer scripts over LLM reasoning, reserve `xhigh` for high-risk work. |
| Emergency | About 90 percent used or higher | Lanes finish current atomic slices, write compact PM status, then pause for supervisor triggers. Heartbeat becomes PM checkpoint only. |

## Emergency Budget Rules

While in emergency budget mode:

- Lanes must not recursively choose new work after finishing an atomic slice.
- Each lane should write one compact PM status: Done, In Progress, Blocked, Next owner action, evidence/commit.
- Supervisor follow-ups should be rare and targeted.
- Prefer no-op monitoring over lane wakeups when there is no safety risk.
- Do not spend LLM usage trying to overcome known external blockers such as expired AWS authentication.
- Pause EC2/model-ingest/candidate-runtime expansion until the external blocker is cleared and a concrete owner-lane trigger exists.

## Critical Budget Rules

While in critical budget mode:

- Do not send broad “continue autonomously” prompts to every lane on every heartbeat.
- Do not deep-read every lane thread unless status changed, EC2/storage risk exists, or a lane has gone idle without a blocker.
- Do not ask lanes to rewrite reports when no material state changed.
- Do not use `xhigh` for formatting, inventory listing, CSV parsing, manifest generation, model-card generation, or routine status summaries.
- Prefer deterministic scripts for CSV parsing, model-card generation, hash checks, JSON validation, table generation, and report assembly.
- Have lanes finish the current atomic slice, commit/push useful text artifacts, then wait for a concrete owner-lane trigger instead of recursively choosing low-value next tasks.
- Keep EC2/storage safety ahead of usage savings. Cost-control and deletion/download decisions may still use `xhigh`.
- Keep strict hand/media QA ahead of usage savings. Visual hand/anatomy/candidate acceptance decisions may still use `xhigh`.

## Escalation Matrix

Use `xhigh` only for:

- editing or structurally validating the canonical Main Flow workflow
- approving or applying EC2 mirror cleanup
- opening, extending, or closing EC2 live windows
- launching EC2-only Civitai/model download batches
- tracker promotion or re-block decisions
- resolving contradictory evidence across lanes
- strict visual hand/anatomy/contact/candidate QA
- safety, content, credential, privacy, or cost-control decisions

Use `high` for:

- normal Lane 1/Lane 2 graph or spatial reasoning that is not actively editing the workflow
- Lane 3 compatibility and target taxonomy decisions
- Lane 4 non-live runtime planning
- Lane 5 no-promotion evidence audits
- Lane 6 AI_Front code and preset contract work

Use `medium` or lower for:

- Lane 7 dashboard refreshes
- branch/status polling
- inventory summaries
- model-card generation from structured CSV data
- report formatting
- manifest sorting

## Current Critical-Budget Lane Defaults

| Lane | Default while critical | Escalate when |
| --- | --- | --- |
| Lane_1 | `gpt-5.4/high` | `gpt-5.5/xhigh` for Main Flow edits, graph repair, contradictory workflow evidence. |
| Lane_2 | `gpt-5.4/high` | `gpt-5.5/xhigh` for hand/contact visual validity or irreversible asset decisions. |
| Lane_3 | `gpt-5.4/medium` for CSV/manifest/card generation; `gpt-5.4/high` for taxonomy | `gpt-5.5/xhigh` before EC2 model-ingest launch requests or risky compatibility claims. |
| Lane_4 | `gpt-5.5/high` | `gpt-5.5/xhigh` for EC2 live windows, cleanup apply, stop-state ambiguity, or model-download execution. |
| Lane_5 | `gpt-5.4/high` | `gpt-5.5/xhigh` for tracker mutations, re-blocks, promotion disputes, or strict visual QA acceptance. |
| Lane_6 | `gpt-5.4/high` | `gpt-5.5/xhigh` for candidate/media QA, hand review, or runtime-readiness acceptance. |
| Lane_7 | `gpt-5.4/medium` | `gpt-5.5/high` or `xhigh` only for release-critical contradiction, storage crisis, or usage-limit resume planning. |

## Current Emergency-Budget Lane Defaults

| Lane | Default while emergency | Escalate when |
| --- | --- | --- |
| Lane_1 | `gpt-5.4/medium` | Actual Main Flow edit or graph repair. |
| Lane_2 | `gpt-5.4/medium` | Strict visual hand/contact validity or irreversible asset decision. |
| Lane_3 | `gpt-5.4/low` for CSV/model-card/manifest scripts; `medium` for taxonomy | EC2 model-ingest launch decision or risky compatibility claim. |
| Lane_4 | `gpt-5.5/medium` | Active EC2 lease, cleanup apply, stop-state ambiguity, or EC2-only model-download execution. |
| Lane_5 | `gpt-5.4/medium` | Tracker mutation, re-block/promotion dispute, or visual QA acceptance. |
| Lane_6 | `gpt-5.4/medium` | Candidate/media QA, hand review, or runtime-readiness acceptance. |
| Lane_7 | `gpt-5.4/low` | Release-critical contradiction, storage crisis, or usage-limit resume planning. |

## Polling Rules

- In critical mode, the supervisor heartbeat should run about every 15 minutes, not every 5 minutes.
- In emergency mode, the supervisor heartbeat should run about every 30 minutes and act as a PM checkpoint, not a work generator.
- A heartbeat should first inspect `list_threads`, the EC2 lease file, disk free space, and git branch status.
- Deep thread reads should be targeted to changed, idle, failed, or high-risk lanes.
- Send a follow-up prompt only to lanes that need an owner-lane action.
- If a lane is active and not risking EC2 cost, storage loss, or secret leakage, let it finish its current slice.

## Model Ingestion Usage Controls

For the Civitai/CSV ingestion work:

- Generate dry manifests and model cards with scripts from CSV data instead of one LLM pass per model.
- Batch model-card creation in groups, with compact templates and no prose expansion unless Lane 5 flags missing information.
- Do not ask Lane 3 to deeply reason over all 5530 models at once.
- First target the 500-row curated file, then stage smaller batches ranked by Main Flow need and storage fit.
- Lane 4 should not open EC2 just to inspect CSV metadata; it should wait for a Lane 3 dry manifest and storage projection.

## Resume After Usage Reset

If usage is reset or the user approves more spending:

1. Return from critical to conservation or normal mode.
2. Restore higher effort only for lanes with concrete pending work.
3. Avoid restarting all lanes at once; wake them in owner-lane order: Lane 4 storage/EC2, Lane 3 manifest, Lane 5 audit, Lane 1/2 workflow dependencies, Lane 6 candidates, Lane 7 dashboard.
