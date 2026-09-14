# P08-S007: Build the financial-education agent

| Property | Value |
|---|---|
| Story ID | P08-S007 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S006 |
| Unlocks | P08-S008 |
| Preferred route | Controller-selected quality route with cross-provider review; local use only under current qualification policy. |
| Research freshness | Current authoritative consumer and financial safety guidance checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to create an educational budgeting and decision-support agent that executes no trades and claims no fiduciary role, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create an educational budgeting and decision-support agent that executes no trades and claims no fiduciary role.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P08-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current authoritative consumer and financial safety guidance checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P08-S006. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Scenarios cover uncertainty, suitability limits, referral, privacy, and prohibited transactions.

## 11. Automated acceptance tests

Scenarios cover uncertainty, suitability limits, referral, privacy, and prohibited transactions. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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
