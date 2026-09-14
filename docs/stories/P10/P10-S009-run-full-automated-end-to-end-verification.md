# P10-S009: Run full automated end-to-end verification

| Property | Value |
|---|---|
| Story ID | P10-S009 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 9 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S008 |
| Unlocks | P10-S010 |
| Preferred route | Controller-selected quality route with cross-provider review; local use only under current qualification policy. |
| Research freshness | Not applicable — tests use the completed system. |

## 1. User story

As the workstation owner, I want this story to execute static, preflight, service, functional, persistence, idempotency, boundary, agent, RAG, memory, backup, and failure tests, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Execute static, preflight, service, functional, persistence, idempotency, boundary, agent, RAG, memory, backup, and failure tests.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

Not applicable — tests use the completed system. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P10-S008. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the mutation must be covered by the active bounded privileged-phase approval; no separate approval is needed unless scope changes.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. One sanitized report accounts for every criterion as pass, fail, warning, or justified skip.

## 11. Automated acceptance tests

One sanitized report accounts for every criterion as pass, fail, warning, or justified skip. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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

