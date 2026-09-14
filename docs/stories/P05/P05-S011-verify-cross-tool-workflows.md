# P05-S011: Verify cross-tool workflows

| Property | Value |
|---|---|
| Story ID | P05-S011 |
| Phase | P05 — Desktop and Development Tool Integrations |
| Sequence | 11 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P05-S010 |
| Unlocks | P05-S012 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Not applicable — tests use the configured integrations. |

## 1. User story

As the workstation owner, I want this story to run representative Git, coding, chat, vision, dictation, and endpoint tests from supported interfaces, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Run representative Git, coding, chat, vision, dictation, and endpoint tests from supported interfaces.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P05-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — tests use the accepted integration versions and make no new current-product recommendation.

## 5. Preconditions and unlock conditions

P05-S010. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify synthetic Git plus Python, Go, Node.js, and TypeScript repositories; fixed chat, code, vision, dictation, and endpoint fixtures; provider identity probes; negative network and credential tests; and a complete cross-tool result matrix. Test LM Studio live only when P05-S010 records opt-in; otherwise verify its guide and record Not installed by owner choice. Store the suite under tests/p05/P05-S011-verify-cross-tool-workflows and evidence under evidence/P05-S011/.

## 7. Out of scope and prohibited changes

Do not weaken WSL isolation, overwrite unrelated editor settings, share Windows and Ubuntu credentials, enable cloud transcription or cleanup, silently replace a hosted model, expose a local endpoint to the LAN, or install an optional integration without owner opt-in.

## 8. Privilege and human approval

No new approval is required while the revision-bound P05 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Tests exercise multiple tools with repository and private-content access; fixtures and negative checks bound effects.

## 10. Execution contract

Assert the required and conditional workflow inventory; create disposable repositories; run VS Code local chat, Codex cloud and local, Claude cloud and local, desktop dictation, Open WebUI, provider identity, network, and credential-boundary fixtures; run LM Studio live only with opt-in; clean every fixture; record the matrix and release the lease.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that the matrix records pass or fail, interface, process boundary, active provider and model, endpoint, credential location, task, negative boundary test, and rollback for every required Windows and WSL workflow. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P05-S011 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

Tests use synthetic or owner-approved fixtures and leave accepted services and configuration unchanged. Rollback removes story-created fixtures and restores the pre-test snapshot recorded in evidence/P05-S011/rollback.json.

## 14. Required evidence

Commit tests/p05/P05-S011-verify-cross-tool-workflows or its versioned result plus evidence/P05-S011/activation.json, evidence/P05-S011/change-inventory.json, evidence/P05-S011/test-results.json, evidence/P05-S011/rollback.json, and evidence/P05-S011/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P05-S011 is Done only when the matrix records pass or fail, interface, process boundary, active provider and model, endpoint, credential location, task, negative boundary test, and rollback for every required Windows and WSL workflow; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P05-S011/checkpoint.json.
