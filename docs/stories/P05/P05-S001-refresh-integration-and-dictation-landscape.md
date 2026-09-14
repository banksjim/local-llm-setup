# P05-S001: Refresh integration and dictation landscape

| Property | Value |
|---|---|
| Story ID | P05-S001 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P04-S014 |
| Unlocks | P05-S002 |
| Preferred route | Interface: goagentic through a web-enabled cloud IDE or CLI; Provider: OpenAI or Anthropic with primary-source web access; Model class: current economical research model; Effort: medium; Fallback: current Sol or Sonnet-class synthesis route when sources conflict. |
| Research freshness | Official product docs and candidate repositories and releases checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to research current official integration paths and current OSS Windows dictation candidates and releases, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Research current official integration paths and current OSS Windows dictation candidates and releases.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official product docs and candidate repositories and releases checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P04-S014. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the official client integration matrix, OSS dictation candidate matrix, release and license evidence, provenance and privacy risk register, and shortlist decision; no client is installed. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P05-S001/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No privileged authorization is required because P05-S001 performs source research and versioned documentation only; discovery of a required mutation creates or reroutes to a separately previewed story.

## 9. Risk rationale

Research and scoring alter recommendations only; provenance or privacy uncertainty blocks candidates.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce docs/research/p05/P05-S001-refresh-integration-and-dictation-landscape-matrix.md; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: the matrix records license, current release and signature, maintenance, telemetry and cloud defaults, local engines, Windows support, hotkey and paste method, uninstall behavior, and primary-source integration contracts.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the matrix records license, current release and signature, maintenance, telemetry and cloud defaults, local engines, Windows support, hotkey and paste method, uninstall behavior, and primary-source integration contracts. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P05-S001 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

A repeat run refreshes docs/research/p05/P05-S001-refresh-integration-and-dictation-landscape-matrix.md without duplicate records. Rollback restores its pre-story Git version and removes only unaccepted evidence/P05-S001/ evidence.

## 14. Required evidence

Commit docs/research/p05/P05-S001-refresh-integration-and-dictation-landscape-matrix.md or its versioned result plus evidence/P05-S001/activation.json, evidence/P05-S001/change-inventory.json, evidence/P05-S001/test-results.json, evidence/P05-S001/rollback.json, and evidence/P05-S001/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P05-S001 is Done only when the matrix records license, current release and signature, maintenance, telemetry and cloud defaults, local engines, Windows support, hotkey and paste method, uninstall behavior, and primary-source integration contracts; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S001/checkpoint.json.
