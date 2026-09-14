# P09-S002: Select memory architecture through an ADR

| Property | Value |
|---|---|
| Story ID | P09-S002 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 2 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P09-S001 |
| Unlocks | P09-S003 |
| Preferred route | Human through a goagentic-guided checklist with the controller-selected assistant; no unattended substitution. |
| Research freshness | P09 framework research must be current. |

## 1. User story

As the workstation owner, I want this story to choose a framework or composable design based on evidence and document migration and fallback consequences, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Choose a framework or composable design based on evidence and document migration and fallback consequences.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

P09 framework research must be current. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P09-S001. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Required — the human performs or validates the work; an LLM cannot create completion evidence.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Owner approves the ADR and no SaaS-only feature is misrepresented as OSS.

## 11. Automated acceptance tests

Owner approves the ADR and no SaaS-only feature is misrepresented as OSS. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

## 12. Human validation

Owner completes the story checklist and records it through the controller.

## 13. Idempotency and rollback

Repeat updates or reproduces evidence without changing accepted implementation; rollback reverts the story record.

## 14. Required evidence

Story revision; actor and model; dated sources; changes; sanitized output; tests; approvals; idempotency; rollback; review; and human records.

## 15. Definition of done

Objective and tests pass; evidence and review are accepted; genuine human evidence exists when required; state agrees; next story unlocks.

## 16. Pause-safe boundaries

Pause before mutation and after each reversible unit, tests, and durable evidence. Finish or roll back atomic replacement before pausing.

