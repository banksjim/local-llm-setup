# P03-S003: Install native Ollama with H drive model storage

| Property | Value |
|---|---|
| Story ID | P03-S003 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P03-S002 |
| Unlocks | P03-S004 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic; Model class: current implementation model; Effort: medium; Fallback: current Sol or Sonnet-class route; no local implementation route before P03-S009 qualifies it. |
| Research freshness | Current Ollama Windows install and environment documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to install the pinned Windows release and configure persistent models and logs under the H drive AI root without broad network exposure, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Install the pinned Windows release and configure persistent models and logs under the H drive AI root without broad network exposure.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Ollama Windows install and environment documentation checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify Ollama package manifest, Windows environment and service configuration, H:\ai\models\ollama and H:\ai\logs\ollama directories, loopback health probe, and uninstall or restore operation. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S003/. Reusable operation: operations/windows/p03/P03-S003-install-native-ollama-with-h-drive-model-storage.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

Before mutation, present the complete revision-bound P03 phase preview and obtain the single phase authorization defined by the phase gate. The owner separately handles any elevation, GUI, microphone, or private-corpus action; these are participation, not additional approvals.

## 9. Risk rationale

Installing a Windows service and redirecting a large model store changes host software and persistent data, but targets are bounded and recoverable.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p03/P03-S003-install-native-ollama-with-h-drive-model-storage; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: Ollama reports the pinned version, listens only on loopback, writes a test model under H:\ai\models\ollama, survives restart, and a second apply is a no-op.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that Ollama reports the pinned version, listens only on loopback, writes a test model under H:\ai\models\ollama, survives restart, and a second apply is a no-op. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

The owner handles any Windows elevation or Ollama installer prompt, then confirms the displayed Ollama version, `H:\ai\models\ollama` location, and loopback-only listener in evidence/P03-S003/human-validation.md. No credential, microphone, or preference action is required. The LLM may present the checklist but cannot author the owner's observation.

## 13. Idempotency and rollback

The operation at operations/windows/p03/P03-S003-install-native-ollama-with-h-drive-model-storage must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p03/P03-S003-install-native-ollama-with-h-drive-model-storage or its versioned result plus evidence/P03-S003/activation.json, evidence/P03-S003/change-inventory.json, evidence/P03-S003/test-results.json, evidence/P03-S003/rollback.json, and evidence/P03-S003/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P03-S003 is Done only when Ollama reports the pinned version, listens only on loopback, writes a test model under H:\ai\models\ollama, survives restart, and a second apply is a no-op; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S003/checkpoint.json.
