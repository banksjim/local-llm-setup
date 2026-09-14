# P07-S005: Implement private source intake and immutable snapshots

| Property | Value |
|---|---|
| Story ID | P07-S005 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P07-S004 |
| Unlocks | P07-S006 |
| Preferred route | Controller-selected quality route with cross-provider review; local use only under current qualification policy. |
| Research freshness | Current secure copy and hashing guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to copy authorized inputs into managed non-Git storage with hashes, provenance, duplicate handling, quarantine, and atomic manifests, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Copy authorized inputs into managed non-Git storage with hashes, provenance, duplicate handling, quarantine, and atomic manifests.

## 3. Learning objective

Not applicable — a separate learning story covers the concept, or no owner-operated concept is introduced.

## 4. Current research requirements

Current secure copy and hashing guidance checked within 30 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P07-S004. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

The objective, declared files or services, tests, documentation, evidence, and minimum safe supporting changes.

## 7. Out of scope and prohibited changes

Unrelated phase work, unapproved redesign, public exposure, secret disclosure, destructive cleanup, and unnamed actions.

## 8. Privilege and human approval

Not applicable — phase authorization is sufficient.

## 9. Risk rationale

Work affects services, private data, credentials, networking, or several components; integration evidence and rollback are mandatory. New facts may raise risk; an LLM cannot lower it.

## 10. Execution contract

Preview, validate, lease, execute reversible units, stop on drift, test, record sanitized evidence, release, and review. Originals never enter Git; duplicate and interruption tests pass; no automatic deletion exists.

## 11. Automated acceptance tests

Originals never enter Git; duplicate and interruption tests pass; no automatic deletion exists. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks pass; exclusions are justified.

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

