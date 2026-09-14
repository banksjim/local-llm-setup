# P03-S008: Publish model usage recommendations

| Property | Value |
|---|---|
| Story ID | P03-S008 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P03-S007 |
| Unlocks | P03-S009 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic; Model class: current implementation model; Effort: medium; Fallback: current Sol or Sonnet-class route; no local implementation route before P03-S009 qualifies it. |
| Research freshness | P03 benchmark evidence; external sources refreshed if recommendations change. |

## 1. User story

As the workstation owner, I want this story to create task-to-model guidance for chat, vision, coding, agents, RAG, enrichment, and constrained multitasking, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create task-to-model guidance for chat, vision, coding, agents, RAG, enrichment, and constrained multitasking.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

P03 benchmark evidence; external sources refreshed if recommendations change. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S007. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the task-to-profile model guide, machine-readable profile manifest, unsupported-use table, and operator switching checklist; no model or client setting is changed. Store versioned implementation or guidance at the story-owned output path already named by this contract and sanitized run evidence under evidence/P03-S008/. Reusable operation: operations/windows/p03/P03-S008-publish-model-usage-recommendations.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The LLM may execute only the previewed story-owned operations; any changed target, network boundary, data class, risk, or destructive action stops for a new preview.

## 9. Risk rationale

Usage guidance drives later client and agent routes, so unsupported recommendations could cause broad quality or resource failures.

## 10. Execution contract

Create an activation packet; verify dependencies, freshness, and targets; preview the exact change; confirm revision-bound phase authorization where mutation is privileged; acquire the controller lease; produce operations/windows/p03/P03-S008-publish-model-usage-recommendations; run the named positive and negative checks; record sanitized evidence; release the lease. Acceptance criterion: every supported task maps to a measured model, context, thinking mode, concurrency limit, expected headroom, fallback, and unsupported-use warning.

## 11. Automated acceptance tests

Assert the expected story inventory is nonzero, then verify that every supported task maps to a measured model, context, thinking mode, concurrency limit, expected headroom, fallback, and unsupported-use warning. Fail on missing evidence, unexpected targets, secrets, stale sources, an untested negative boundary, or a validator that matched zero fixtures.

## 12. Human validation

Not applicable — P03-S008 is accepted through deterministic checks plus an independent review; no experiential or credential-bearing action is delegated to the LLM.

## 13. Idempotency and rollback

The operation at operations/windows/p03/P03-S008-publish-model-usage-recommendations must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p03/P03-S008-publish-model-usage-recommendations or its versioned result plus evidence/P03-S008/activation.json, evidence/P03-S008/change-inventory.json, evidence/P03-S008/test-results.json, evidence/P03-S008/rollback.json, and evidence/P03-S008/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and an explicit not-applicable human record.

## 15. Definition of done

P03-S008 is Done only when every supported task maps to a measured model, context, thinking mode, concurrency limit, expected headroom, fallback, and unsupported-use warning; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S008/checkpoint.json.
