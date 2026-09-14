# P01-S003: Define machine-readable program and story schemas

| Property | Value |
|---|---|
| Story ID | P01-S003 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P01-S002 |
| Unlocks | P01-S004 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: standard implementation; Effort: medium; Fallback: Claude Code with an Anthropic coding model at medium effort; local execution is prohibited before P03 qualification. |
| Research freshness | Current schema-library documentation checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement schemas for phases, stories, model routes, risk, evidence, approvals, and references, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement schemas for phases, stories, model routes, risk, evidence, approvals, and references.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current schema-library documentation checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S002. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Create versioned JSON Schemas under `goagentic/schemas/` for program, phase, story, activation packet, model route, risk derivation, approval, runtime state, event, lease, and evidence records; add valid and invalid fixtures under `goagentic/fixtures/schema/`; and add dependency-free PowerShell validation tests under `goagentic/tests/schema/`.

## 7. Out of scope and prohibited changes

Command behavior, state persistence, GitHub synchronization, workstation configuration, permissive unknown-field handling that hides typos, silently coercing invalid values, and schema changes that broaden an approved story objective.

## 8. Privilege and human approval

Not applicable — repository-only schema and fixture changes are covered by the P01 phase authorization and require no elevation, login, external mutation, or owner judgment.

## 9. Risk rationale

The story is Medium risk because these schemas become the validation boundary for every later story; an overly permissive or incompatible schema could allow invalid work to advance. Changes are repository-only and reversible, but require unit tests, backward-compatibility fixtures, and fresh-session review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Positive fixtures validate; blank, placeholder, unexplained not-applicable, invalid-risk, cyclic, and missing-section fixtures fail.

## 11. Automated acceptance tests

Positive fixtures validate; blank, placeholder, unexplained not-applicable, invalid-risk, cyclic, and missing-section fixtures fail. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — schema behavior is deterministically verified with positive and negative fixtures and a fresh-session review. Owner validation is reserved for later controller behavior and cannot improve a failing schema result.

## 13. Idempotency and rollback

Schema generation is deterministic from committed definitions; a second run yields no diff. Rollback reverts `goagentic/schemas/`, `goagentic/fixtures/schema/`, and `goagentic/tests/schema/` together so schema and fixtures cannot drift.

## 14. Required evidence

Schema-library source and version; schema file inventory and hashes; contract-to-schema field mapping; positive and negative fixture list; test output proving each invalid class is rejected; compatibility result; second-run diff; secret scan; rollback rehearsal; and fresh-session reviewer verdict.

## 15. Definition of done

Every contract property and section has a machine-checkable representation; all valid fixtures pass; each declared invalid class fails for the expected reason; no schema relies on an unimplemented service; rerun is clean; and P01-S004 is unblocked.

## 16. Pause-safe boundaries

Pause after each schema is syntactically valid, after the fixture set is complete, after positive tests, after negative tests, and after compatibility review. Never publish a schema without its matching fixtures and tests.
