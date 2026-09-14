# P01-S009: Implement quality, evidence, and review gates

| Property | Value |
|---|---|
| Story ID | P01-S009 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S008 |
| Unlocks | P01-S010 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; independent cross-provider review is required and local execution is prohibited before P03 qualification. |
| Research freshness | Current testing and supply-chain guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to enforce risk-derived tests, scope, rollback, research freshness, reviewer independence, and evidence completeness, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Enforce risk-derived tests, scope, rollback, research freshness, reviewer independence, and evidence completeness.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current testing and supply-chain guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S008. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Implement risk derivation, activation-packet validation, scope checking, evidence completeness, freshness, idempotency, rollback, secret scan, and reviewer-independence gates in `goagentic/src/Quality.psm1` and `goagentic/src/Evidence.psm1`; implement `verify`, `review`, and `audit`; and add fixtures for every required rejection.

## 7. Out of scope and prohibited changes

Judging subjective human experience as automated fact, letting the implementer self-approve, lowering risk without owner evidence, accepting stale sources, redacting only after secret material is committed, or marking a story Done from a generic “tests pass” statement.

## 8. Privilege and human approval

Not applicable — repository implementation and fixtures are covered by the P01 phase authorization. Only a proposed risk reduction or disputed human-only boundary requires owner action.

## 9. Risk rationale

The story is High risk because these gates decide whether every later story is executable and complete. A false positive could propagate unsafe work across the program; comprehensive negative fixtures, failure injection, and cross-provider review are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Stories cannot complete when an applicable gate or independent verdict is absent.

## 11. Automated acceptance tests

Stories cannot complete when an applicable gate or independent verdict is absent. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — positive and negative fixtures prove each machine-enforced gate, and cross-provider review checks the human-only boundaries. The owner resolves only proposed risk reductions or disputed findings.

## 13. Idempotency and rollback

Verification and audit are read-only except for versioned evidence output and produce the same verdict for unchanged inputs. Review records append rather than overwrite. Rollback restores prior modules and schemas while retaining accepted historical evidence and findings.

## 14. Required evidence

Story revision; gate-to-contract trace; module and fixture hashes; positive and every negative result; risk-derivation examples; stale-source, scope-drift, missing-evidence, secret, self-review, and forged-human-evidence denials; repeat result; rollback rehearsal; and cross-provider verdict.

## 15. Definition of done

Every canonical rule has an enforcing check or an explicitly identified human gate; every negative fixture is rejected for the expected reason; no implementer can be sole reviewer; risk cannot be silently lowered; and P01-S010 is unblocked after cross-provider review.

## 16. Pause-safe boundaries

Pause after each gate and its negative-fixture pair, after the contract trace, and after the combined audit. Never accept partial evidence or temporarily disable a gate across a pause.
