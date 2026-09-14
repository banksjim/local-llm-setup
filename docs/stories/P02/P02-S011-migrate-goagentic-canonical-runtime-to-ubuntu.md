# P02-S011: Migrate goagentic canonical runtime to Ubuntu

| Property | Value |
|---|---|
| Story ID | P02-S011 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P02-S010 |
| Unlocks | P02-S012 |
| Preferred route | Interface: Codex CLI across Windows and the dedicated Ubuntu distribution; Provider: OpenAI; Model class: architecture-capable migration; Effort: high; Fallback: Claude Code with an Anthropic architecture-capable model at high effort; cross-provider review and rollback rehearsal are required. |
| Research freshness | Current WSL invocation behavior checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to move the canonical controller runtime into Ubuntu and leave a Windows forwarding wrapper, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Move the canonical controller runtime into Ubuntu and leave a Windows forwarding wrapper.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current WSL invocation behavior checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S010. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Implement a Windows forwarding wrapper plus Ubuntu installation, state-path, and verification operations that run the accepted controller modules under PowerShell 7 in `AI-Workbench`; migrate runtime state through a schema-validated export/import; retain accepted Git evidence; and test command parity, interruption, fallback, and rollback.

## 7. Out of scope and prohibited changes

Rewriting controller policy, changing story/evidence schemas without a design-change story, copying Windows credentials into Ubuntu, mounting the repository through a Windows drive, deleting the Windows Controller Core before acceptance, or marking Cross-Interface Trusted before P05 live adapter tests.

## 8. Privilege and human approval

No new approval for unchanged scope — the state migration and wrapper authority switch are included in the P02 phase authorization. Schema drift, lost evidence, changed target, or an unproven rollback blocks the operation.

## 9. Risk rationale

The story is High risk because it moves canonical control state across an OS boundary; state loss or behavioral drift could misroute future privileged work. Schema validation, export backup, command-by-command parity, crash injection, reversible authority switch, and cross-provider review are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Cross-interface tests return identical state and fail safely when Ubuntu is stopped.

## 11. Automated acceptance tests

Cross-interface tests return identical state and fail safely when Ubuntu is stopped. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — schema identity, command parity, interruption, wrapper failure, rerun, and rollback are automated and cross-provider reviewed. The owner validates post-reboot use in P02-S012.

## 13. Idempotency and rollback

An unchanged rerun finds the same installed controller version, state identity, and wrapper target and performs no migration. Before switching authority, preserve validated Windows and exported controller state. Rollback repoints the wrapper to the accepted Windows core and restores the pre-switch state; it does not delete Ubuntu evidence or event history.

## 14. Required evidence

Controller and schema revisions; Windows/Ubuntu PowerShell versions; operation and wrapper hashes; pre-migration state/event/lease inventory; export hash and import validation; command/fixture parity table; interruption and unavailable-WSL results; first and second apply; authority proof; rollback rehearsal; and cross-provider verdict.

## 15. Definition of done

Windows and Ubuntu runs produce equivalent normalized results for every P01 fixture; accepted state and event identity survive migration; the wrapper fails safely when WSL is unavailable; rerun is a no-op; rollback restores Windows authority; and P02-S012 is unblocked without claiming Cross-Interface Trusted.

## 16. Pause-safe boundaries

Pause after source-state export, after Ubuntu import validation, after parity tests, before wrapper authority changes, and after authority verification. Never leave both runtimes believing they are authoritative.
