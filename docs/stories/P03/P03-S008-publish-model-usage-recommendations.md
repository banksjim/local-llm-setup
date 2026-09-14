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
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | P03 benchmark evidence; external sources refreshed if recommendations change. |

## 1. User story

As the workstation owner, I want this story to create task-to-model guidance for chat, vision, coding, agents, RAG, enrichment, and constrained multitasking, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create task-to-model guidance for chat, vision, coding, agents, RAG, enrichment, and constrained multitasking.

## 3. Learning objective

Not applicable — a separate learning story covers the major concept, or no new owner-operated concept is introduced.

## 4. Current research requirements

P03 benchmark evidence; external sources refreshed if recommendations change. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S007. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — active phase authorization is sufficient.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible from versioned backup. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and route to review. The guide maps every model to context, temperature or thinking, concurrency, and when not to use it.

## 11. Automated acceptance tests

The guide maps every model to context, temperature or thinking, concurrency, and when not to use it. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; justified exclusions are recorded.

## 12. Human validation

Not applicable — automated evidence and independent review are sufficient.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores only story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; change inventory; sanitized output; test, approval, idempotency, rollback, review, and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; human evidence is genuine; no prohibited change occurred; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back any atomic replacement before pausing.

