# P02-S004: Create the H drive data layout

| Property | Value |
|---|---|
| Story ID | P02-S004 |
| Phase | P02 — Windows, WSL, Git, and VS Code Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P02-S003 |
| Unlocks | P02-S005 |
| Preferred route | Interface: Codex CLI plus Windows PowerShell; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; cross-provider review is required and local execution is not yet qualified. |
| Research freshness | Current Windows ACL and filesystem guidance checked within 30 days. |

## 1. User story

As the workstation owner, I want this story to create the approved H drive AI directories, permissions, manifests, and non-destructive ownership rules, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Create the approved H drive AI directories, permissions, manifests, and non-destructive ownership rules.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P02-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Windows ACL and filesystem guidance checked within 30 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P02-S003. Applicable specifications, clean Git state, valid controller state, current research, required model route, and lease checks must pass.

## 6. In scope

Implement preview/apply/verify/rollback operations under `operations/windows/p02/` for `H:\ai\models`, `containers`, `wsl\AI-Workbench`, `knowledge-sources`, `knowledge-repos`, `backups`, `logs`, `manifests`, and `tmp`; create a managed-path manifest; apply only explicitly approved ACL changes; and add tests under `tests/p02/`.

## 7. Out of scope and prohibited changes

Formatting or repartitioning `H:`, taking ownership of pre-existing user content, recursive deletion, broad deny ACLs, moving existing files, creating knowledge-base remotes, installing software, and treating an unexpected nonempty path as managed.

## 8. Privilege and human approval

No new approval for unchanged scope — the exact paths and ACL operations are included in the P02 phase authorization. Elevation may require owner presence; any different path, recursive change, or nonempty-target decision requires reauthorization.

## 9. Risk rationale

The story is High risk because it establishes shared storage and ACLs on a real data drive; a path or permission error could affect unrelated files or future private data. Exact path resolution, nonempty-path stops, reversible ACL snapshots, idempotency, and cross-provider review are mandatory.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the lease; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the lease; and route to review or human validation. Dry run, first run, and second run pass; unknown files are preserved; rollback removes only empty managed paths.

## 11. Automated acceptance tests

Dry run, first run, and second run pass; unknown files are preserved; rollback removes only empty managed paths. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass. A justified not-applicable test is recorded rather than omitted.

## 12. Human validation

Not applicable — exact path, content-preservation, ACL, rerun, and fixture-rollback checks are deterministic and independently reviewed. The owner reviews the overall storage layout later in P02-S012.

## 13. Idempotency and rollback

An unchanged second apply reports zero created paths and zero ACL changes. Before apply, capture existence, contents, owner, and ACL for each target. Rollback restores recorded ACLs and removes only empty directories created by this operation; it never removes a nonempty directory or unknown file.

## 14. Required evidence

Story and operation revisions; resolved absolute paths; pre-change existence/content/ACL inventory; phase authorization; preview; created-path and ACL change manifest; first and second apply results; unknown-file preservation test; rollback rehearsal in a fixture and safe real-state verification; and cross-provider verdict.

## 15. Definition of done

All managed directories exist with verified intended ownership; pre-existing and unknown content is unchanged; the manifest exactly matches managed paths; the second apply is a no-op; rollback behavior is proven without data deletion; and P02-S005 is unblocked.

## 16. Pause-safe boundaries

Pause after preflight inventory, after preview authorization is confirmed, after directory creation, after ACL application, and after verification. Never pause during one ACL replacement; finish or restore that path before stopping.
