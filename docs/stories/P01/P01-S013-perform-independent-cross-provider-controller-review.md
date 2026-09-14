# P01-S013: Perform independent cross-provider controller review

| Property | Value |
|---|---|
| Story ID | P01-S013 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 14 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S012 |
| Unlocks | P01-S014 |
| Preferred route | Interface: fresh Codex CLI or Claude Code session; Provider: different from the implementation provider; Model class: architecture/security review; Effort: high; Fallback: another fresh cloud-provider session that preserves provider independence; local review is prohibited in P01. |
| Research freshness | Current provider availability checked at activation. |

## 1. User story

As the workstation owner, I want this story to review the controller design, implementation, tests, and threat boundaries in a fresh provider context, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Review the controller design, implementation, tests, and threat boundaries in a fresh provider context.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current provider availability checked at activation. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S012. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Provide a fresh reviewer with the approved authority chain, controller diff, threat model, tests, failure-injection results, and no author conclusions; record findings in `evidence/P01-S013/review.md` with severity, file or operation location, exploit or failure path, required correction, and disposition.

## 7. Out of scope and prohibited changes

Using the implementation provider as the only reviewer, asking the reviewer to fix findings silently, omitting failed tests or known limitations, reviewing workstation phases, or accepting unresolved Critical or High findings without an explicit owner decision and follow-up validation.

## 8. Privilege and human approval

Not applicable for the read-only review. An owner decision is required only for a disputed finding, risk acceptance, or proposed scope change and is recorded separately.

## 9. Risk rationale

The review is High risk because it is the principal independent check on the controller that will later authorize system changes. It is read-only, but an incomplete or non-independent review could expose the full future blast radius; provider independence and finding traceability are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Every finding is resolved or explicitly accepted by the owner with evidence.

## 11. Automated acceptance tests

Every finding is resolved or explicitly accepted by the owner with evidence. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner is required only if a finding needs risk acceptance, a disputed disposition, or a scope decision. The reviewer cannot manufacture that decision or close an unresolved owner item.

## 13. Idempotency and rollback

Review execution is read-only. A repeat creates a separately identified verdict or appends a new review round; it never overwrites the original findings. Rollback reverts only the review-record commit and cannot erase a finding from Git history.

## 14. Required evidence

Reviewer provider, model class, and effort plus proof it differs from the implementer; reviewed commit; supplied evidence inventory; complete findings table including categories with no finding; author responses; correction commits; rerun results; residual risks; and final reviewer verdict.

## 15. Definition of done

The reviewer inspected every controller trust boundary and failure category; all Critical and High findings are corrected and retested or explicitly rejected by the owner with rationale; Medium findings have dispositions; reviewer independence is proven; and P01-S014 is unblocked.

## 16. Pause-safe boundaries

Pause after the evidence inventory is accepted, after the initial findings table, after each correction round, and before final verdict. Never overwrite or silently close an unresolved finding across a pause.
