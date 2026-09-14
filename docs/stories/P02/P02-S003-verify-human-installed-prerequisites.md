# P02-S003: Verify human-installed prerequisites

| Property | Value |
|---|---|
| Story ID | P02-S003 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | Human + LLM |
| Dependencies | P02-S002 |
| Unlocks | P02-S004 |
| Preferred route | Interface: interactive Codex CLI plus Windows PowerShell; Provider: OpenAI; Model class: general-purpose diagnostic; Effort: low; Fallback: Claude Code with an Anthropic general-purpose model while running the same read-only checks; owner confirms GUI-only facts. |
| Research freshness | Current prerequisite requirements from P02 research. |

## 1. User story

As the workstation owner, I want this story to verify Windows updates, WSL2, Rancher Desktop, Git, virtualization, NVIDIA driver, H drive, and available space without installing them, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Verify Windows updates, WSL2, Rancher Desktop, Git, virtualization, NVIDIA driver, H drive, and available space without installing them.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current prerequisite requirements from P02 research. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S002. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Run and document read-only checks for Windows build and update state, WSL version/features, virtualization, NVIDIA driver and RTX 4090 visibility, Rancher Desktop installation and stopped/running state, Git and GitHub CLI, VS Code, `H:` filesystem and free space, and whether an `AI-Workbench` distribution or target directory already exists.

## 7. Out of scope and prohibited changes

Installing, upgrading, starting, stopping, logging in, relocating, deleting, or reconfiguring prerequisites; displaying tokens or private repository data; accepting a failed requirement; and treating the absence of `AI-Workbench` as an error rather than expected pre-provision state.

## 8. Privilege and human approval

Required human validation — the owner confirms GUI-only and physical-device facts. Checks remain read-only and precede the P02 mutation preview; this is not permission to repair a failed prerequisite.

## 9. Risk rationale

The story is Medium risk because most checks are read-only but they inspect system, storage, GPU, and authenticated-tool state, and incorrect interpretation could authorize unsafe installation. No machine mutation is allowed; owner-confirmed GUI state and a fresh review are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. A sanitized preflight report records versions, health, free space, and exact remediations. It estimates initial and growth storage for models, containers, WSL, source versions, Git knowledge output, indexes, logs, and backup retention; insufficient headroom blocks the next story.

## 11. Automated acceptance tests

A sanitized preflight report records versions, health, free space, and exact remediations. It estimates initial and growth storage for models, containers, WSL, immutable sources, Git knowledge output, indexes, logs, and at least one restorable backup generation; insufficient headroom blocks the next story. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

## 12. Human validation

The owner confirms physical hardware, GUI-only health, update/restart readiness, and whether any observed existing distribution or H-drive content is expected. A failed prerequisite remains blocked rather than being repaired in this story.

## 13. Idempotency and rollback

Repeated checks do not change service state or authentication and should differ only in timestamp and legitimate system drift. Rollback reverts only `evidence/P02-S003/`; there is no workstation rollback because workstation mutation is prohibited.

## 14. Required evidence

Story revision; check commands; sanitized outputs and GUI confirmations; required-versus-observed table; `H:` filesystem/free-space result; existing distro/path collision scan; authentication status without secrets; failures and owner actions; before/after service-state comparison; and reviewer verdict.

## 15. Definition of done

Every prerequisite is Pass or an explicit blocking owner action; `H:` has the approved filesystem and sufficient measured capacity for the next phase; no name/path collision is unresolved; no service or account state changed; and P02-S004 is unblocked only when all required checks pass.

## 16. Pause-safe boundaries

Pause between read-only checks, before any prompt that could alter state, and after the owner confirms GUI-only facts. Record legitimate drift and rerun the affected check; never repair during this story.
