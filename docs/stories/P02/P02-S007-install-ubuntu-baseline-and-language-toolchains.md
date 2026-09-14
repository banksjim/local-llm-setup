# P02-S007: Install Ubuntu baseline and language toolchains

| Property | Value |
|---|---|
| Story ID | P02-S007 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 7 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P02-S006 |
| Unlocks | P02-S008 |
| Preferred route | Interface: Codex CLI operating inside the dedicated Ubuntu distribution; Provider: OpenAI; Model class: systems implementation; Effort: medium; Fallback: Claude Code inside the same distribution with an Anthropic coding model at medium effort; cross-provider review is required. |
| Research freshness | Current official language/toolchain installation sources checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to install pinned Python, Go, Node.js, TypeScript, build, lint, test, and package-management tooling inside Ubuntu, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Install pinned Python, Go, Node.js, TypeScript, build, lint, test, and package-management tooling inside Ubuntu.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current official language/toolchain installation sources checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S006. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Implement idempotent Ubuntu operations under `operations/ubuntu/p02/` for the P02-S001-selected package/version strategy; install baseline build tools, PowerShell 7, Python, Go, Node.js, npm-compatible package tooling, and TypeScript; create version manifests and smoke projects; and add verification/rollback tests under `tests/p02/`.

## 7. Out of scope and prohibited changes

Using Windows-host language runtimes from Ubuntu, installing editors or AI services, changing shell dotfiles beyond managed marked blocks, global unpinned npm packages other than the approved baseline, replacing user-created environments, and installing versions not resolved in the activation packet.

## 8. Privilege and human approval

No new approval for unchanged scope — the pinned Ubuntu package and runtime operations are included in the P02 phase authorization. Repository/key or package-plan drift invalidates that authorization.

## 9. Risk rationale

The story is High risk because it changes Ubuntu packages, repositories, PATH, and four development ecosystems and can destabilize the canonical environment. All changes remain inside `AI-Workbench`, but require a package plan, version pins, smoke builds, idempotency, rollback/export recovery, and cross-provider review.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Version checks and hello-world tests pass for every language; repeat run is no-op.

## 11. Automated acceptance tests

Version checks and hello-world tests pass for every language; repeat run is no-op. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — version, path, build, lint, test, repeat, and recovery checks are automated and independently reviewed. The owner validates daily tool use in P02-S012.

## 13. Idempotency and rollback

The second apply installs or edits nothing and every version remains identical. Capture package, repository, PATH, and managed-dotfile state plus a WSL export checkpoint before apply. Rollback removes only manifest-owned packages/blocks where safe; if system package reversal is unsafe, restore the verified export rather than approximate prior state.

## 14. Required evidence

Selected strategy and official sources; exact package/runtime versions and repositories; operation hashes; pre-change package/PATH/export inventory; P02 authorization; first and second apply logs; Python, Go, Node.js, TypeScript, PowerShell, lint, test, and build smoke results; rollback decision and rehearsal; and cross-provider verdict.

## 15. Definition of done

Each runtime resolves from inside `AI-Workbench`, the four smoke projects build and test, the manifest matches installed versions, no Windows executable or host runtime is used, the second apply is a no-op, recovery is proven, and P02-S008 is unblocked.

## 16. Pause-safe boundaries

Pause after repository or key setup, after each package group, after each runtime installation, and after each smoke project. Do not pause during package-manager transactions; allow completion or invoke the documented recovery path.
