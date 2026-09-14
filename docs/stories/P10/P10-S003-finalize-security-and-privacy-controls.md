# P10-S003: Finalize security and privacy controls

| Property | Value |
|---|---|
| Story ID | P10-S003 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S002 |
| Unlocks | P10-S004 |
| Preferred route | Controller-selected quality route with cross-provider review; local use only under current qualification policy. |
| Research freshness | Current platform and component security guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to audit listeners, firewall, credentials, permissions, secrets, repositories, telemetry, agent tools, and private data paths, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Audit listeners, firewall, credentials, permissions, secrets, repositories, telemetry, agent tools, and private data paths.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current platform and component security guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P10-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the mutation must be covered by the active bounded privileged-phase approval; no separate approval is needed unless scope changes.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Automated scans and cross-provider review find no unexplained exposure; rollback exists.

## 11. Automated acceptance tests

Automated scans and cross-provider review find no unexplained exposure; rollback exists. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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
