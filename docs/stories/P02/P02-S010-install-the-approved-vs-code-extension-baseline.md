# P02-S010: Install the approved VS Code extension baseline

| Property | Value |
|---|---|
| Story ID | P02-S010 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P02-S009 |
| Unlocks | P02-S011 |
| Preferred route | Interface: Codex CLI plus VS Code command line; Provider: OpenAI; Model class: standard implementation; Effort: low; Fallback: Claude Code with an Anthropic coding model at low effort; local execution is prohibited before P03 qualification. |
| Research freshness | Marketplace and maintainer documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to install and document the minimum extensions for WSL, Git, Python, Go, Node/TypeScript, containers, YAML, Markdown, PowerShell, and later AI work, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Install and document the minimum extensions for WSL, Git, Python, Go, Node/TypeScript, containers, YAML, Markdown, PowerShell, and later AI work.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Marketplace and maintainer documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S009. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Create a versioned extension manifest that records extension ID, publisher, purpose, trust/telemetry notes, Windows-versus-WSL install location, and requirement source; implement preview/apply/verify/rollback operations under `operations/windows/p02/` for the minimum WSL, Git, Python, Go, JavaScript/TypeScript, container, YAML, Markdown, PowerShell, and later-AI baseline; and test it in `AI-Workbench`.

## 7. Out of scope and prohibited changes

Installing overlapping formatters or language servers without a documented choice; optional cosmetic extensions; local autocomplete configuration; extensions with unresolved publisher or license concerns; enabling telemetry without recording the owner's choice; and removing pre-existing extensions.

## 8. Privilege and human approval

No new approval for unchanged scope — the reviewed extension manifest and install locations are included in the P02 phase authorization. Publisher, permission, telemetry, or manifest drift creates an owner decision before apply.

## 9. Risk rationale

The story is Medium risk because extensions execute code and can access workspaces, but the change is confined to a reviewed manifest and user/remote VS Code profiles. Publisher verification, minimality, location checks, idempotency, and fresh-session review are required.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. An extension manifest is versioned; each extension has a purpose; conflicts and deprecated choices are absent.

## 11. Automated acceptance tests

An extension manifest is versioned; each extension has a purpose; conflicts and deprecated choices are absent. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — manifest, publisher, location, feature, overlap, rerun, and rollback checks are deterministic. The owner validates the combined VS Code experience in P02-S012.

## 13. Idempotency and rollback

The second apply installs nothing and reports the same versions/locations. Capture the pre-existing Windows and WSL extension inventories first. Rollback removes only extensions installed by this story that were absent from that inventory; it never downgrades or removes a pre-existing extension.

## 14. Required evidence

Manifest revision; marketplace or official source/access date for every extension; publisher/license/trust review; pre-existing inventories; preview; installed ID/version/location table; language-feature smoke results; overlap and secret scan; second apply; rollback test in a disposable profile or exact safe removal proof; and reviewer verdict.

## 15. Definition of done

Every manifest entry is current, justified, and installed in the correct Windows or WSL location; each language/tool category passes its declared smoke check; no unresolved overlap exists; pre-existing extensions are preserved; rerun is a no-op; and P02-S011 is unblocked.

## 16. Pause-safe boundaries

Pause after the pre-existing inventory, after each small extension category, and after location and feature verification. Never stop during an extension install or update transaction or remove an extension absent from the story manifest.
