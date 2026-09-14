# P03-S005: Pull candidate models with storage guards

| Property | Value |
|---|---|
| Story ID | P03-S005 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P03-S004 |
| Unlocks | P03-S006 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic; Model class: current implementation model; Effort: medium; Fallback: current Sol or Sonnet-class route; no local implementation route before P03-S009 qualifies it. |
| Research freshness | Model registry and license sources refreshed at execution. |

## 1. User story

As the workstation owner, I want this story to pull only approved explicit tags after capacity and license checks, recording digests and sizes, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Pull only approved explicit tags after capacity and license checks, recording digests and sizes.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Model registry and license sources refreshed at execution. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S004. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify capacity preflight, approved immutable model manifest, guarded pull or resume operation, model inventory probe, and story-owned removal operation under H:\ai\models\ollama. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S005/. Reusable operation: operations/windows/p03/P03-S005-pull-candidate-models-with-storage-guards.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Large downloads consume material H-drive capacity and interrupted or wrong-tag pulls can leave substantial derived data.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p03/P03-S005-pull-candidate-models-with-storage-guards; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: capacity preflight reserves 20 percent free disk, every approved tag and digest matches the research matrix, interrupted download resumes safely, and no floating or unapproved tag is present.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that capacity preflight reserves 20 percent free disk, every approved tag and digest matches the research matrix, interrupted download resumes safely, and no floating or unapproved tag is present. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S005 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p03/P03-S005-pull-candidate-models-with-storage-guards must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p03/P03-S005-pull-candidate-models-with-storage-guards or its versioned result plus evidence/P03-S005/activation.json, evidence/P03-S005/change-inventory.json, evidence/P03-S005/test-results.json, evidence/P03-S005/rollback.json, and evidence/P03-S005/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S005 is Done only when capacity preflight reserves 20 percent free disk, every approved tag and digest matches the research matrix, interrupted download resumes safely, and no floating or unapproved tag is present; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S005/checkpoint.json.
