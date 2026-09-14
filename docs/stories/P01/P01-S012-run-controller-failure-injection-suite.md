# P01-S012: Run controller failure-injection suite

| Property | Value |
|---|---|
| Story ID | P01-S012 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 13 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S011 |
| Unlocks | P01-S013 |
| Preferred route | Interface: Codex CLI in an isolated fixture workspace; Provider: OpenAI; Model class: test and diagnosis; Effort: medium; Fallback: Claude Code with an Anthropic diagnostic model at medium effort; the reviewer must use the other provider. |
| Research freshness | Not applicable — this story tests the implemented contract rather than selecting a tool. |

## 1. User story

As the workstation owner, I want this story to exercise interruption, corrupt state, stale lease, dirty Git, outage, stopped dependencies, wrong model, missing approval, and duplicate writers, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Exercise interruption, corrupt state, stale lease, dirty Git, outage, stopped dependencies, wrong model, missing approval, and duplicate writers.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Not applicable — this story tests the accepted controller contract and pinned test environment rather than selecting or recommending a changeable tool.

## 5. Preconditions and unlock conditions

P01-S011. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Create `goagentic/tests/failure-injection/` scenarios and an isolated disposable-workspace harness for process interruption, partial state write, altered event, stale/live lease, duplicate writer, dirty Git, GitHub outage, stopped WSL, wrong route, missing approval, scope drift, and failed rollback.

## 7. Out of scope and prohibited changes

Injecting failures into the real repository state, real Project records, actual WSL distributions, or user data; hiding flaky runs; weakening a gate to make a scenario pass; and treating an expected stop as successful recovery without checking its next action.

## 8. Privilege and human approval

Not applicable — all faults run in disposable fixtures under the P01 phase authorization. Any need to touch real GitHub, WSL, repository runtime, or user data is a scope failure, not an implied approval request.

## 9. Risk rationale

The story is High risk because it tests safety mechanisms by simulating destructive conditions and can produce false confidence if fixtures touch real state or assertions are weak. Isolation proof, repeatability, complete failure coverage, and cross-provider review are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. All declared failures stop safely, retain evidence, and identify one recovery action.

## 11. Automated acceptance tests

All declared failures stop safely, retain evidence, and identify one recovery action. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — execution is confined to disposable fixtures and independently reviewed. Any evidence of contact with real Project, repository runtime, WSL, or user data fails the story automatically.

## 13. Idempotency and rollback

Each scenario starts from a new disposable fixture and leaves the real repository, Project, and workstation unchanged. Repeated seeded runs produce the same classification. Cleanup removes only the recorded disposable root; failed cleanup preserves the path and reports it rather than widening deletion.

## 14. Required evidence

Story revision; harness and scenario hashes; isolation-root proof; one result per declared failure; expected stop classification and next action; before/after real-state comparison; seeded rerun comparison; cleanup inventory; residual artifact report; and cross-provider verdict.

## 15. Definition of done

Every declared failure is injected, detected, and mapped to a fail-closed state with exactly one recovery action; no scenario mutates real project or workstation state; two complete seeded runs agree; and P01-S013 is unblocked.

## 16. Pause-safe boundaries

Pause only between fully cleaned scenarios and after results are durably recorded. Never pause while a fault is active or cleanup ownership is ambiguous; preserve the disposable root and report it for inspection.
