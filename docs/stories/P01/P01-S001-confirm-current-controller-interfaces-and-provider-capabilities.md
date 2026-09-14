# P01-S001: Confirm current controller interfaces and provider capabilities

| Property | Value |
|---|---|
| Story ID | P01-S001 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 2 |
| Status | Planned |
| Step | Research |
| Hold reason | Dependency |
| Risk | Low |
| Actor | LLM |
| Dependencies | P01-S015 |
| Unlocks | P01-S002 |
| Preferred route | Interface: Codex desktop or CLI with web access; Provider: OpenAI; Model class: economical research; Effort: low; Fallback: Claude Code with an Anthropic general-purpose model at low effort, escalating only unresolved synthesis. |
| Research freshness | Official product documentation and live CLI capability checks no older than 7 days. |

## 1. User story

As the workstation owner, I want this story to produce a dated compatibility record for Codex, Claude Code, PowerShell, WSL, GitHub CLI, GitHub Projects, and available model tiers, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Produce a dated compatibility record for Codex, Claude Code, PowerShell, WSL, GitHub CLI, GitHub Projects, and available model tiers.

## 3. Learning objective

Not applicable — this research story prepares the evidence used by the following learning gate and does not teach an owner-operated procedure.

## 4. Current research requirements

Official product documentation and live CLI capability checks no older than 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S015. Applicable specifications, clean Git state, current research, and the P01 bootstrap-protocol checks must pass.

## 6. In scope

Create `evidence/P01-S001/compatibility.md` and a machine-readable companion inventory covering installed command versions, authentication state without credentials, supported invocation modes, model/effort choices, GitHub Project access, and known limitations for Codex, Claude Code, Windows PowerShell, WSL, GitHub CLI, and GitHub Projects.

## 7. Out of scope and prohibited changes

Installing or upgrading tools; changing authentication, GitHub Projects, repositories, model settings, or controller code; exposing tokens or account identifiers not required for compatibility; and claiming support from documentation without a live read-only capability check.

## 8. Privilege and human approval

Not applicable — all product and CLI checks are read-only and any authentication renewal or mutation is explicitly excluded. Writing the research evidence is covered by the P01 phase authorization.

## 9. Risk rationale

The work is Low risk because it performs documentation lookup and read-only version/capability checks, writes only story evidence in Git, and cannot change workstation or remote state. Discovery of a check that requires login renewal or mutation stops the story and raises the route for owner action.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. The record cites current primary documentation, distinguishes verified facts from assumptions, and lists blocking incompatibilities.

## 11. Automated acceptance tests

The record cites current primary documentation, distinguishes verified facts from assumptions, and lists blocking incompatibilities. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — this story changes only research evidence. A fresh reviewer validates the compatibility claims; authentication renewal or any mutating capability check is deferred to an explicit owner-action story.

## 13. Idempotency and rollback

Rerunning updates the dated inventory deterministically and performs no product or account mutation. Rollback removes or reverts only `evidence/P01-S001/`; previously accepted evidence remains available in Git history.

## 14. Required evidence

The story revision; execution interface, provider, model class, and effort; direct official URLs with access dates; sanitized command-version and capability outputs; a supported/unsupported/unknown matrix; authentication-scope result without secrets; conflicts and inferences; rerun comparison; and independent review verdict.

## 15. Definition of done

Both evidence files exist, agree with each other, cover every named interface, distinguish verified facts from inference, contain no secrets, and pass link and schema checks. An independent reviewer finds no unsupported compatibility claim, and P01-S002 is unblocked without any workstation or remote mutation.

## 16. Pause-safe boundaries

Pause between product or source families, before any check that would require mutation or login renewal, after the compatibility matrix is complete, and after sanitized evidence is written. A partially researched product remains `Unknown`, never inferred.
