# P02-S009: Install and configure VS Code WSL development

| Property | Value |
|---|---|
| Story ID | P02-S009 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P02-S008 |
| Unlocks | P02-S010 |
| Preferred route | Interface: interactive Codex CLI plus Windows VS Code; Provider: OpenAI; Model class: systems integration; Effort: medium; Fallback: Claude Code with an Anthropic coding model while the owner performs GUI actions; live owner validation is mandatory. |
| Research freshness | Current VS Code WSL documentation and extension requirements checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to configure Windows VS Code to open Linux-filesystem repositories and keep workspace tools inside Ubuntu, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Configure Windows VS Code to open Linux-filesystem repositories and keep workspace tools inside Ubuntu.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current VS Code WSL documentation and extension requirements checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S008. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Create versioned preview/apply/verify/rollback operations under `operations/windows/p02/` for the automatable VS Code WSL extension and managed-setting changes; configure the current Microsoft-supported integration from Windows to `AI-Workbench`; create a disposable repository beneath the Linux user's home; prove terminal, Git, debugging, tasks, source control, and file operations execute in Ubuntu; and document the exact owner workflow and trust-boundary indicators. Initial trust prompts and experiential confirmation remain manual.

## 7. Out of scope and prohibited changes

Placing repositories on Windows-mounted filesystems; enabling Windows executable interoperability solely for `code .`; installing the full extension baseline from P02-S010; configuring local AI clients; opening private repositories for the test; and weakening workspace-trust or telemetry choices without owner direction.

## 8. Privilege and human approval

Required human participation — the owner performs GUI-only VS Code actions and confirms the remote indicators and developer experience. The P02 phase authorization covers the declared configuration; material boundary or extension changes require reauthorization.

## 9. Risk rationale

The story is High risk because VS Code bridges the Windows UI into the protected Ubuntu environment and incorrect placement or extension execution can defeat the boundary. Owner-driven GUI validation, Linux-path/process proof, integration tests, and cross-provider review are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. A test workspace proves terminal, Git, debugger, and extension host run in Ubuntu.

## 11. Automated acceptance tests

A test workspace proves terminal, Git, debugger, and extension host run in Ubuntu. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner opens the Linux workspace in Windows VS Code, identifies the remote indicators, runs the guided terminal/task/debug/source-control checks, and confirms the workflow is usable.

## 13. Idempotency and rollback

Reopening the same Linux workspace reuses the remote server and settings without duplicate entries or changed files. Rollback removes only story-created workspace settings, disposable repository, and story-owned remote-server artifacts if safely identifiable; it does not reset global VS Code or delete user repositories.

## 14. Required evidence

Current VS Code/WSL source versions; installed extension identity/version; `AI-Workbench` target proof; Linux path, kernel, process, runtime, Git, task, debug, and file-operation outputs; owner screenshots or confirmations of remote indicators; reopen result; cleanup/rollback evidence; and cross-provider verdict.

## 15. Definition of done

Windows VS Code opens a Linux-home repository in `AI-Workbench`; integrated terminal, Git, task, test, and debugger processes all run in Ubuntu; no Windows drive or executable is needed; reopening is stable; the owner can repeat the workflow; and P02-S010 is unblocked.

## 16. Pause-safe boundaries

Pause after WSL extension verification, after remote-server connection, after disposable workspace creation, and after each terminal, Git, task, debug, and file test. Never delete an ambiguous workspace during cleanup.
