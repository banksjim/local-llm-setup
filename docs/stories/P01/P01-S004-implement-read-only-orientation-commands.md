# P01-S004: Implement read-only orientation commands

| Property | Value |
|---|---|
| Story ID | P01-S004 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P01-S003 |
| Unlocks | P01-S005 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: standard implementation; Effort: medium; Fallback: Claude Code with an Anthropic coding model at medium effort; local execution is prohibited before P03 qualification. |
| Research freshness | Current PowerShell and CLI conventions checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to implement a static zero-context entry document plus bare goagentic, status, next, and model on Windows without workstation dependencies, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Implement a static `START-HERE.md` plus bare goagentic, status, next, and model on Windows without workstation dependencies. The static document points to the command and never duplicates dynamic status.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current PowerShell and CLI conventions checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S003. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Create root `START-HERE.md`, `goagentic/goagentic.ps1`, read-only command dispatch and rendering modules under `goagentic/src/`, fixtures for each lifecycle and hold state, and dependency-free PowerShell tests for bare `goagentic`, `status`, `next`, and `model`.

## 7. Out of scope and prohibited changes

Mutation commands, state writes other than isolated test output, GitHub API calls, workstation installation, dynamic status copied into `START-HERE.md`, multiple competing next actions, and assumptions that Codex or Claude chat history is available.

## 8. Privilege and human approval

Not applicable — repository code changes are covered by the P01 phase authorization; the implemented commands are read-only and require no external or privileged action.

## 9. Risk rationale

The story is Medium risk because incorrect orientation can direct the owner to unsafe or out-of-order work. It changes repository code only, but requires deterministic unit tests and a fresh zero-context review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Each command returns schema-valid output and exactly one safe next action without mutating project work; `START-HERE.md` stays accurate after state changes.

## 11. Automated acceptance tests

Each command returns schema-valid output and exactly one safe next action without mutating project work. `START-HERE.md` contains no generated status and remains accurate across fixture state changes. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

## 12. Human validation

Not applicable — zero-context fixture tests and fresh-session review verify output semantics. The owner exercises the same commands later in P01-S014 before controller trust is granted.

## 13. Idempotency and rollback

Repeated read-only commands may update neither repository nor runtime state and must return equivalent output for an unchanged fixture. Rollback removes the entry point, orientation modules, fixtures, tests, and `START-HERE.md` as one revision.

## 14. Required evidence

Story revision; interface/provider/model class/effort; file inventory; command output for every fixture; before/after filesystem and Git state proving no mutation; exactly-one-action assertions; static-document drift result; repeated-command comparison; rollback result; and fresh-session review verdict.

## 15. Definition of done

From a fresh shell with no chat context, `START-HERE.md` leads to the entry point; all four commands parse every valid fixture, fail clearly on invalid state, show the complete route, and produce exactly one—or zero when explicitly blocked—next actions without changing state. P01-S005 is unblocked.

## 16. Pause-safe boundaries

Pause after `START-HERE.md`, after command parsing, after each renderer, and after each fixture group. Do not pause between reading one state snapshot and producing its next-action result; discard and reread if interrupted.
