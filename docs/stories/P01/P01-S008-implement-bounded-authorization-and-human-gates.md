# P01-S008: Implement bounded authorization and human gates

| Property | Value |
|---|---|
| Story ID | P01-S008 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P01-S007 |
| Unlocks | P01-S009 |
| Preferred route | Interface: interactive Codex CLI with the owner; Provider: OpenAI; Model class: architecture and security implementation; Effort: high; Fallback: Claude Code with an Anthropic architecture/security model at high effort; cross-provider review and genuine owner validation are mandatory. |
| Research freshness | Current secure approval and CLI input practices checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement exact goagentic go authorization, one privileged-phase approval, and genuine human evidence recording, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement exact goagentic go authorization, one privileged-phase approval, and genuine human evidence recording.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current secure approval and CLI input practices checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S007. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement authorization records and interval validation in `goagentic/src/Authorization.psm1`; implement `go` and `human-complete` handlers; bind approval to story, revision, actor, risk, operation set, expiry condition, and safe checkpoints; and add bypass, replay, scope-change, wrong-story, expired, and forged-human-evidence tests.

## 7. Out of scope and prohibited changes

Interpreting conversational “go” as authorization, reusable blanket approval across phases, generating owner attestations, lowering risk, continuing after objective or scope drift, storing secrets in approval records, and permitting an adapter to bypass controller validation.

## 8. Privilege and human approval

Required human participation — the P01 phase authorization covers implementation. The owner issues a clearly labeled synthetic test authorization and later validates that genuine human evidence cannot be forged; neither action expands the approved P01 scope.

## 9. Risk rationale

The story is Critical because authorization is the boundary between planning and real mutations, including later privileged and private-data work. A defect could enable the entire workstation blast radius; explicit phase approval, isolated rehearsal, owner validation, failure injection, and cross-provider review are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Conversational go, missing approval, wrong story, and fabricated human evidence are rejected.

## 11. Automated acceptance tests

Conversational go, missing approval, wrong story, and fabricated human evidence are rejected. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner issues one synthetic test authorization and one genuine test attestation, confirms denied replay and conversational-go cases, and verifies that the evidence distinguishes owner input from fixture input.

## 13. Idempotency and rollback

Replaying or reusing a consumed, expired, wrong-revision, or wrong-story authorization is rejected. Rollback disables the new mutating handlers and restores the prior module set without deleting approval or event history; no rollback may fabricate a missing owner decision.

## 14. Required evidence

Story revision; authorization schema and module hashes; exact approved-interval examples; owner-issued test approval; denial outputs for every bypass, replay, and drift case; genuine versus simulated evidence markers; repeat result; rollback rehearsal; owner acceptance; and cross-provider verdict.

## 15. Definition of done

Only exact `goagentic go` with a valid story-bound authorization can enter the approved operation set; every bypass and replay fixture is denied; human evidence remains owner-generated and attributable; scope drift invalidates approval; rollback succeeds; and P01-S009 is unblocked by genuine owner acceptance.

## 16. Pause-safe boundaries

Pause before asking for synthetic authorization, after it is recorded, before consumption, after every denial fixture, and before owner validation. Never pause after authorizing an operation but before recording its bound scope.
