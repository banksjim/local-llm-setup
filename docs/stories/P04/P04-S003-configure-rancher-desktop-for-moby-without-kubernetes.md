# P04-S003: Configure Rancher Desktop for Moby without Kubernetes

| Property | Value |
|---|---|
| Story ID | P04-S003 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P04-S002 |
| Unlocks | P04-S004 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: qualified local Ollama worker or OpenAI or Anthropic cloud; Model class: current implementation model; Effort: medium; Fallback: current Terra or Sonnet-class cloud route, then Sol or Sonnet-class diagnosis if verification fails. |
| Research freshness | Current Rancher Desktop preferences and API documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to place Rancher's growing data on `H:` and apply the runtime settings needed for loopback Compose services, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Move Rancher's growing data and snapshots to their exact `H:\ai\containers` targets and apply the runtime settings needed for loopback Compose services.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P04-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Rancher Desktop preferences, volume-location, snapshot, factory-reset, and API documentation plus current Microsoft WSL move/export documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts. Select a relocation method only when the current installed WSL and Rancher versions support it; otherwise block rather than improvising an unregister/import sequence.

## 5. Preconditions and unlock conditions

P04-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify: exact current/target WSL distribution inventory; free-space and collision checks; a tested `rancher-desktop-data` export; activation-supported move to `H:\ai\containers\rancher-desktop-data`; documented snapshot-directory link to `H:\ai\containers\rancher-desktop-snapshots`; actual-path and restart verification; Rancher settings backup; rdctl apply/verify operations; Moby and Kubernetes/Wasm state probes; AI-Workbench Docker-socket probe; resource report; and recovery/rollback operation. Store versioned implementation or guidance at the story-owned output path and sanitized run evidence under evidence/P04-S003/. Reusable operation: operations/windows/p04/P04-S003-configure-rancher-desktop-for-moby-without-kubernetes.

## 7. Out of scope and prohibited changes

Do not move or unregister the `AI-Workbench` distribution; relocate live database files through Windows bind mounts; delete the verified export before final acceptance; enable Kubernetes or Wasm; publish database ports; bind host services beyond loopback; store secrets in Git or evidence; ingest a real knowledge base; enable cloud APIs; or alter Ollama model selection. Do not use an undocumented filesystem junction for the WSL data distribution.

## 8. Privilege and human approval

Before mutation, present the complete revision-bound P04 phase preview and obtain the single phase authorization defined by the phase gate. The owner separately handles any elevation, GUI, microphone, or private-corpus action; these are participation, not additional approvals.

## 9. Risk rationale

This story is Critical because relocating Rancher's WSL data distribution can make every local image and volume unavailable if interrupted or targeted incorrectly; it also changes the runtime, WSL integration, and Docker socket. Exact target resolution, a verified export, current supported-method evidence, restart verification, delayed export deletion, and a rehearsed recovery path are mandatory.

## 10. Execution contract

Create an activation packet; inventory exact distribution, snapshot, target, collision, free-space, and service state; prove a restorable export; preview the supported move and settings change; confirm the revision-bound P04 authorization; acquire the controller lease; stop Rancher cleanly; move only `rancher-desktop-data`; relocate snapshots through the documented link method; restart and verify actual paths before changing runtime settings; apply and verify Moby/resource/integration settings; run positive and negative checks; retain the export through owner acceptance; record sanitized evidence; release the lease. Acceptance criterion: the data distribution and snapshot target resolve beneath the exact `H:` paths, existing Rancher inventory survives, rdctl and Docker report Moby active, Kubernetes and Wasm disabled, only AI-Workbench integrated, localhost publishing works, and a second apply is unchanged.

## 11. Automated acceptance tests

Assert nonzero expected distributions, inventory objects, and negative fixtures. Verify exact resolved WSL and snapshot locations beneath the approved `H:` targets; export hash and test-import/recovery proof; unchanged pre/post image-volume inventory; clean Rancher restart; Moby active; Kubernetes and Wasm disabled; only AI-Workbench integrated; resource settings match; localhost publishing works; and second apply is unchanged. Fail on a missing or extra distribution, path collision, insufficient space, unverified export, deleted recovery copy, inventory loss, unexpected mount, undocumented method, stale source, secret, or zero-match validator.

## 12. Human validation

The owner handles any elevation, confirms Rancher is stopped before relocation, compares the displayed source/target paths and pre/post image-volume inventory, observes the successful restart, and records the retained export location in evidence/P04-S003/human-validation.md. No credential or microphone action is required. The LLM cannot supply the owner's path, inventory, or restart observations.

## 13. Idempotency and rollback

The operation implements preview, export, apply, verify, and story-owned recovery. A second apply is a no-op after confirming the actual locations. Before later services create durable data, rollback may use the verified export to restore only `rancher-desktop-data` to its recorded pre-story location and restore the snapshot link/settings. After P04-S004 begins, relocation is a fixed architecture boundary and rollback must restore configuration without moving or deleting live volumes. Never delete an unknown distribution, model, database, document, repository, or unrelated setting.

## 14. Required evidence

Commit the reusable operation plus evidence/P04-S003/activation.json, source-and-method-decision.md, distribution-inventory.json, export-verification.json, change-inventory.json, test-results.json, rollback.json, and review.md. Include exact versions, resolved paths, sanitized commands/observations, timestamps, pre/post inventory hashes, retained-export disposition, and genuine owner-authored validation; never commit the export itself.

## 15. Definition of done

P04-S003 is Done only when Rancher's growing data and snapshots resolve beneath the exact approved `H:` targets, the retained verified export and recovery proof exist outside Git, prior inventory survives, Moby is active, Kubernetes and Wasm are disabled, only AI-Workbench is integrated, localhost publishing and second-apply checks pass, the required evidence exists, and independent review has no unresolved material finding.

## 16. Pause-safe boundaries

Pause after the activation packet, after the export verifies, before the move, after move/restart verification, after snapshot relocation, after settings/tests, and after evidence is committed. Do not pause while Rancher is stopped with a move incomplete or while the distribution is unregistered. Before pausing, finish or recover the atomic unit and record exact distribution state, retained export, next command, model, and provider in evidence/P04-S003/checkpoint.json.
