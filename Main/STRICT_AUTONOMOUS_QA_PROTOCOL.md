# Strict Autonomous QA, Hand Review, And History Protocol

## Purpose

All lanes must run in strict autonomous QA mode. A lane is not done merely because it produced an artifact. It must test, review, document, and hand off the artifact with enough evidence for another lane to reproduce or reject the claim.

This protocol applies to every lane and every heartbeat.

## Universal QA Gate

Before a lane claims success, it must record:

- what changed
- why it changed
- files created or modified
- exact validation commands or checks run
- pass/fail results
- known untested areas
- downstream lane requests
- blockers and exact next actions
- commit id and push state when Git-visible artifacts changed

If a lane cannot run a test, it must say why and record the next concrete test owner.

## Main Flow QA Priority

All work must stay tied to the canonical Main Flow:

`C:\Comfy_UI\Implementation\workflows\ui\WAVE42_MAIN_FLOW_20260702.json`

The strongest QA priority is Main Flow readiness:

- workflow graph validity
- node/link/input/output consistency
- model and asset visibility
- mask/control/depth/pose availability
- runtime endpoint behavior
- candidate output provenance
- tracker status truth

Side artifacts are not final unless they produce Main Flow evidence, a Main Flow request, a runtime request, a QA decision, or an exact blocker.

## Strict Hand Review Gate

Any lane touching hands, fingers, contact, body interaction, pose, masks, soft-body controls, generated candidates, or QA evidence must explicitly run the hand review gate.

The hand review gate must inspect or prove:

- hand count and left/right identity
- finger count, continuity, and separation
- thumb orientation and palm orientation
- wrist-to-hand connection
- hand scale relative to body/face
- per-hand mask alignment
- contact-zone mask alignment
- pose/depth/normal consistency around hands
- occlusion ordering at contact points
- collision or impossible interpenetration
- soft-body deformation consistency near hand contact
- absence of fused fingers, missing fingers, extra fingers, broken knuckles, or melted hand edges
- whether the review used actual generated media, input/control images, masks, workflow structure only, or runtime metadata only

If no actual image/media output was reviewed, the verdict must be `not_visually_reviewed` or `manual_visual_review_required`. Do not claim hand quality from workflow structure alone.

## Required Verdicts

Use one of these verdicts in lane reports:

- `pass`
- `pass_with_limitations`
- `manual_review_required`
- `not_visually_reviewed`
- `blocked`
- `fail`

No tracker promotion may use `manual_review_required`, `not_visually_reviewed`, or `blocked` as final proof.

## Continuous History Requirements

Each lane must maintain a continuous history under both its lane worktree and the shared session mirror when practical:

- Worktree journal: `C:\Comfy_UI_Lora\5_session_worktrees\Lane_X\Lane_X\history\YYYYMMDD_laneX_work_journal.md`
- Shared mirror journal: `C:\Comfy_UI_Lora\5_sessions\Lane_X\history\YYYYMMDD_laneX_work_journal.md`
- Status reports: `Lane_X\reports\YYYYMMDD_HHMMSS_laneX_status.md`
- Issue/blocker records: `Lane_X\issues\YYYYMMDD_HHMMSS_laneX_issue_or_blocker.json`
- Hand review records: `Lane_X\hand_reviews\YYYYMMDD_HHMMSS_laneX_hand_review.json`

Append to the journal:

- at the start of each autonomous work slice
- before and after risky edits
- after each meaningful test or validation
- after each blocker
- after each fix
- before any final answer or idle pause

Status reports should summarize what was performed, what was completed, what is in progress, what is about to be completed, issues found, fixes implemented, blockers, evidence paths, and next lane actions.

## Testing Requirements By Lane

Lane 1 must validate workflow JSON, graph links, active-path inputs, model references, LoadImage references, backups, and exact diff scope.

Lane 2 must validate mask/image existence, dimensions when possible, contact graph consistency, hand/contact controls, and Lane 1 request clarity.

Lane 3 must validate model/LoRA presence, hashes when useful, family compatibility, Main Flow filename reconciliation, local/EC2 runtime visibility requests, and self-hosted LLM availability.

Lane 4 must validate lease state, EC2 state, endpoint readiness, runtime visibility, logs without secrets, evidence hashes, and must stop/release live windows when done.

Lane 5 must validate evidence schema, direct-evidence sufficiency, tracker row mapping, hand-review verdicts, promotion/re-block truth, and no overclaiming.

Lane 6 must validate AI_Front contract behavior, self-hosted LLM route, presets, generated candidate provenance, media QA, hand review, and Lane 5 handoff evidence.

Lane 7 must validate cross-lane reports against current lane artifacts, detect stale or missing reports, document usage-limit and storage-pressure risks, and route blockers to owner lanes without taking over their authority.

## Commit And Reporting Rules

Commit and push small text coordination artifacts when useful. Do not commit:

- secrets
- live lease files
- generated media
- model binaries
- raw cache/download files
- credentials

Every pushed commit should be referenced in the lane status report.

## Supervisor Responsibilities

The supervisor must:

- poll all lanes continuously
- escalate lanes to `gpt-5.5/xhigh` for strict QA/review/testing and all hand-review work
- re-prompt idle lanes with the next Main Flow-facing task
- monitor EC2 live windows until stopped and released
- require history/report artifacts, not just chat summaries
- preserve user or lane changes and never revert unrelated work
- watch for Codex Desktop 5-hour or weekly usage exhaustion and record resumable blockers when a lane stops from usage limits
- watch C: drive free space and route stale EC2 mirror cleanup through Lane 4 and `CLEANUP_POLICY.md`
