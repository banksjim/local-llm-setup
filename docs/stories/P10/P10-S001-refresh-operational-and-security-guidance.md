# P10-S001: Refresh operational and security guidance

| Property | Value |
|---|---|
| Story ID | P10-S001 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P09-S012 |
| Unlocks | P10-S002 |
| Preferred route | Controller-selected economical research route with web access. |
| Research freshness | Official docs, releases, and security advisories checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to review current advisories, upgrade paths, backup guidance, and Windows, WSL, and container hardening, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Review current advisories, upgrade paths, backup guidance, and Windows, WSL, and container hardening.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official docs, releases, and security advisories checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P09-S012. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

No privileged mutation or user-data risk is expected. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. A dated operational risk register maps changes to bounded work.

## 11. Automated acceptance tests

A dated operational risk register maps changes to bounded work. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Not applicable — automated evidence and independent review suffice.

## 13. Idempotency and rollback

Repeat updates or reproduces evidence without changing accepted implementation; rollback reverts the story record.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
