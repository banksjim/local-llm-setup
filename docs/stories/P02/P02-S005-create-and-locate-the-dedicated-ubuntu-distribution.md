# P02-S005: Create and locate the dedicated Ubuntu distribution

| Property | Value |
|---|---|
| Story ID | P02-S005 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P02-S004 |
| Unlocks | P02-S006 |
| Preferred route | Interface: interactive Codex CLI plus elevated Windows PowerShell; Provider: OpenAI; Model class: architecture and systems implementation; Effort: high; Fallback: Claude Code with an Anthropic architecture model using the same preview and checklist; P02 phase authorization and isolated rehearsal are mandatory. |
| Research freshness | Current Microsoft WSL import/export/move documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provision the named Ubuntu WSL2 distribution and place its VHDX under the approved H drive location using a previewed reversible procedure, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Provision the named Ubuntu WSL2 distribution and place its VHDX under the approved H drive location using a previewed reversible procedure.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Microsoft WSL import/export/move documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S004. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Implement a current Microsoft-supported, preview/apply/verify/rollback operation under `operations/windows/p02/` that creates the approved Ubuntu release as WSL distribution `AI-Workbench` with its storage beneath `H:\ai\wsl\AI-Workbench`; create one owner-named non-root Linux account as the default user; record only its username in the managed manifest; and include collision detection, export backup, registration verification, and isolated rehearsal.

## 7. Out of scope and prohibited changes

Unregistering or moving an existing distribution without a verified export and owner-directed design change; modifying the user's default distribution; deleting a VHDX; reusing a nonempty target; enabling broad Windows mounts; installing development tools; hardcoding, logging, or storing the Linux password; creating additional login users; and relying on an undocumented VHDX move.

## 8. Privilege and human approval

Required human participation — the existing P02 phase authorization covers the previewed operation. The owner chooses the Linux username, enters its password directly into the trusted prompt, handles elevation prompts, and validates the registered distribution and storage location; no new approval is required unless the operation or target changes materially.

## 9. Risk rationale

The story is Critical because WSL registration and storage relocation can destroy a distribution if interrupted or reversed incorrectly and may require elevation. The named target is new, but collision detection, one P02 phase authorization, isolated rehearsal, export verification, owner-performed prompts, and recovery proof are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. The distribution boots, location is verified, export backup succeeds, and no other distribution changes.

## 11. Automated acceptance tests

The distribution boots, location is verified, export backup succeeds, and no other distribution changes. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

The owner chooses the Linux username, enters the password only in the trusted prompt, handles elevation, and confirms the displayed distribution identity and H-drive storage location.

## 13. Idempotency and rollback

If the correct registered distribution already exists at the verified target, rerun reports no change. Before any unregister or relocation step, produce and validate an export. Rollback removes only a newly created empty/test registration or restores the verified export under the original recorded identity; never delete an unverified VHDX.

## 14. Required evidence

Official procedure and selected Ubuntu release; operation revision; resolved target; preflight collision inventory; P02 authorization; isolated-rehearsal transcript; export path/hash and import validation when applicable; registration and actual storage proof; recorded non-root username and default-user check without password material; first and second run; rollback rehearsal; owner-performed prompt evidence; and cross-provider verdict.

## 15. Definition of done

Exactly one healthy `AI-Workbench` distribution is registered, its actual storage is verified beneath the approved H-drive parent, its default user is the recorded non-root account, no password appears in logs or Git, other distributions and defaults are unchanged, a repeat is a no-op, recovery is proven, and P02-S006 is unblocked.

## 16. Pause-safe boundaries

Pause before any registration or relocation mutation, after a required export verifies, after registration, after default-user setup, and after storage verification. Never pause between unregister and a verified replacement registration.
