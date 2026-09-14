# P09-S012: Perform memory owner acceptance

| Property | Value |
|---|---|
| Story ID | P09-S012 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 12 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P09-S011 |
| Unlocks | P10-S001 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | Not applicable — validation uses the implemented memory system. |

## 1. User story

As the workstation owner, I want this story to have the owner review candidates, promote, edit, reject, correct a memory, test isolation, and recover after restart, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Have the owner review candidates, promote, edit, reject, correct a memory, test isolation, and recover after restart.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

Not applicable — validation uses the implemented memory system. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P09-S011. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work crosses a security, privilege, destructive-data, authentication, or acceptance boundary and requires explicit owner control. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Owner accepts transparency and control; P09 evidence contains no restricted values.

## 11. Automated acceptance tests

Owner accepts transparency and control; P09 evidence contains no restricted values. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Owner completes the story checklist and records it through the controller.

## 13. Idempotency and rollback

Second execution reports no unintended change; rollback restores story-owned changes and preserves user data.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.
