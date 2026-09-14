# P07-S007: Implement deterministic YAML frontmatter and filing

| Property | Value |
|---|---|
| Story ID | P07-S007 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P07-S006 |
| Unlocks | P07-S008 |
| Preferred route | Controller-selected value route; qualified local model allowed after P03; cloud fallback per SYS-CTL. |
| Research freshness | Current serializer documentation checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to prepend safe canonical frontmatter, choose stable paths, count content, and reproduce unchanged output byte-for-byte, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Prepend safe canonical frontmatter, choose stable paths, count content, and reproduce unchanged output byte-for-byte.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P07-S003; this story introduces no separate learning objective.

## 4. Current research requirements

Current serializer documentation checked within 30 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P07-S006. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work changes bounded repository or user-level configuration and is directly reversible. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Schema, YAML escaping, hashes, idempotency, and path-collision tests pass without LLM calls.

## 11. Automated acceptance tests

Schema, YAML escaping, hashes, idempotency, and path-collision tests pass without LLM calls. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Not applicable — automated evidence and independent review suffice.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
