# P01 revision-bound phase mutation preview

Preview ID: **ACT-P01-S015-2026-10-25-r1**. Specification baseline: **ef2833a8fce8bbb11262b7890883c07ea9e73b31**. Prepared 2026-10-25. Authorization: **not granted**. Execution: **not started**.

The containing preparation commit and packet-manifest.json bind this preview's exact bytes. The owner approves this phase scope once. SYS-CTL still requires explicit story-by-story direction until the controller is trusted. Approval of this preview plus P01-S015 execution does not authorize automatic execution of P01-S001 or the rest of P01.

## External mutations

| Target | Exact proposed scope |
|---|---|
| Personal GitHub Project | Create one Project owned by banksjim, titled **Local AI Workstation Playbook (LAW-WIN)**. Keep PRIVATE; add no collaborators, teams, or organization ownership. Do not reuse a pre-existing Project. Record Project ID, number, and URL returned by GitHub. |
| Metadata | Configure the 13 canonical visible fields and exact options in project-plan.json: reuse Title and built-in Status; create 11 custom fields. Preserve unrelated built-in fields but hide them from the required views. Do not alter account or repository permissions. |
| Views | Exactly **All stories** (table, Phase then Sequence ascending) and **Workflow** (board, Status columns, same sort). Reconcile only default views proved created with this Project. |
| Backlog | Import **137 draft items** keyed by Story ID and linked to the pinned specification revision. Then convert **P01-S015 only** into its repository issue, retaining its Project item and values. Final bootstrap inventory: **137 items = 136 drafts + 1 public repository issue**. |
| Public issue | Repository banksjim/local-llm-setup; title and complete body are fixed in project-plan.json. Content contains only existing public specification metadata and a pinned story URL. No private Project URL/IDs, local filesystem paths, credentials, or knowledge content. No assignees, labels, mentions, or comment messages are added. |
| Later P01 synchronization | After separate activation of each story, reconcile this same Project and create/convert at most one issue for each Ready P01 story, up to **15 P01 issues total**, including P01-S015. Update only the fields/items recorded as program-owned. No future-phase issue creation in P01. Preview every synchronization batch; preserve conflicting manual edits for owner reconciliation. |
| Publication boundary | Local commits are included. **No git push, pull request, release, remote tag, or publication of local evidence** is included. Pinned public story links already resolve at the baseline commit. Any later publication needs its own concrete authorization. |

Create the shell and immediately explicitly set PRIVATE; verify `public == false` before adding fields, views, or items. The creation API has no explicit visibility input. Do not assume its default or import content before privacy is confirmed. The sanitized title itself contains only already-public project information. A failure to obtain private visibility stops the story.

There are no existing Projects or issues in the inspected account/repository. Recheck immediately before apply and stop on any drift. Unknown resources are never adopted, overwritten, or removed by this authorization.

## Local repository and runtime mutations by story

All paths are relative to C:\Users\banksjim\projects\local-llm-setup. Modules are Windows PowerShell 5.1 compatible; tests have no newly installed dependencies. The table fixes file/directory ownership; it does not permit unrelated refactoring, architecture changes, or additional services. Each later story requires its own current activation packet within these bounds.

| Sequence / story | Authorized deliverables when that story is separately activated |
|---|---|
| 1 / P01-S015 | `goagentic/bootstrap/ProjectBootstrap.ps1` with Preview/Apply/Verify/Rollback modes; `goagentic/bootstrap/BootstrapLedger.md`; `goagentic/bootstrap/project-mapping.json`; `goagentic/tests/bootstrap/` and `goagentic/fixtures/bootstrap/`; `evidence/P01-S015/` execution, approval, snapshots, research, review and genuine owner-validation records. No controller modules in this story. |
| 2 / P01-S001 | `evidence/P01-S001/compatibility.md` and `compatibility.json`; read-only product/CLI research and capability checks. No upgrades, login changes, or model-setting changes. |
| 3 / P01-S002 | `evidence/P01-S002/lesson.md`, `scenarios.json`, and `owner-learning.md`; record the owner's original answers, never generate them. |
| 4 / P01-S003 | `goagentic/schemas/{program,phase,story,activation-packet,model-route,risk,approval,state,event,lease,evidence}.schema.json`; valid/invalid fixtures under `goagentic/fixtures/schema/`; dependency-free validation under `goagentic/tests/schema/`. |
| 5 / P01-S004 | `START-HERE.md`, `goagentic/goagentic.ps1`, `goagentic/src/Commands.psm1`, `Orientation.psm1`, `goagentic/fixtures/orientation/`, and `goagentic/tests/orientation/`; implement bare entry, status, next, and model as read-only operations. |
| 6 / P01-S005 | `goagentic/src/State.psm1`, `EventLog.psm1`, state/event schemas, `goagentic/fixtures/state/`, `goagentic/tests/state/`; ignored `.goagentic/state.json`, checkpoint files, and `events.jsonl`. Atomic state and tamper-evident append-only history. |
| 7 / P01-S006 | `goagentic/src/Lease.psm1`, lease/state schemas, `goagentic/fixtures/lease/`, `goagentic/tests/lease/`; ignored `.goagentic/lease.json`. Prove ownership/concurrency handling before replacing the manual bootstrap lock. |
| 8 / P01-S007 | `goagentic/src/Recovery.psm1`, command dispatch changes, recovery fixtures/tests, `.goagentic/` pause/checkpoint records. Resume inspects and reconciles; it never executes pending story work. |
| 9 / P01-S008 | `goagentic/src/Authorization.psm1`, go/human-complete handlers in Commands.psm1, approval schema, authorization fixtures/tests, `.goagentic/` authorization/consumption records. Bind authority to scope, revision, actor, story, risk and checkpoints. |
| 10 / P01-S009 | `goagentic/src/Quality.psm1`, `Evidence.psm1`, verify/review/audit dispatch, applicable schema changes and quality fixtures/tests. Enforce evidence, freshness, scope, risk and independent review; do not fake a review. |
| 11 / P01-S010 | `goagentic/adapters/codex/`, `goagentic/adapters/claude/`, per-adapter manifests/instructions, and adapter conformance fixtures/tests. Installation tests only in isolated fixture targets. No global configuration/credential changes or claims of live P05 integration. |
| 12 / P01-S011 | `goagentic/src/GitHubProject.psm1`, versioned `goagentic/bootstrap/project-mapping.json`, Project fixtures/tests, approved previews and live synchronization evidence for the one Project. Replace manual maintenance only after accepted parity tests. |
| 13 / P01-S012 | `goagentic/tests/failure-injection/`, scenario fixtures under `goagentic/fixtures/failure-injection/`, isolated harness and evidence. Simulate missing WSL/services; do not start, stop, install or configure real services. |
| 14 / P01-S013 | `evidence/P01-S013/review.md`, reviewer handoff, findings and dispositions from a genuine fresh cross-provider review. Corrections stay within the owning story's approved paths and rerun its checks. Scope changes require a revised preview. |
| 15 / P01-S014 | Owner-drill scripts/tests under `goagentic/tests/owner-acceptance/`, disposable fixtures, `evidence/P01-S014/` original owner results and acceptance baseline. Owner controls application restart/reboot. Record Controller Core Trusted only after the real drill passes; a local trust-baseline Git tag may be created then, never a remote tag. |

For every activated P01 story, sanitized evidence lives in `evidence/<story-id>/`. Lifecycle metadata updates may touch only the corresponding story's Status/Step/Hold/risk fields and machine-readable state; preserve immutable IDs, Sequence, objectives, and acceptance requirements. Phase/README status can be updated only when supported by accepted evidence. No blanket authorization to rewrite specifications is requested.

Bootstrap lock: ignored `.goagentic/bootstrap-lock.json`, with actor, story, start time, operation and checkpoint; manual ledger and append-only execution journal retained in Git. Preserve a stale lock until inspection establishes ownership and a safe recovery decision. Releasing a lock only after proving ownership is included; arbitrary removal is excluded.

## Risk, gates, and cost

P01 as a whole is Critical because P01-S008 and P01-S014 are Critical. P01-S015's written baseline is High; effective risk is **raised to Critical for this packet**, because its Ready-state issue conversion publishes a record in the existing public repository. This applies the canonical risk table's public-publication dimension; it is not a risk downgrade or an architecture change. Record both the source and derived risk in execution evidence and show the effective value on the board.

Required before P01-S015 live writes: owner authorization of this preview, clean committed packet, manual lock/ledger, a named local rollback commit, current research/preflight, nonzero synthetic acceptance and failure/rollback rehearsal, and fresh cross-provider review of the implemented bootstrap operation. Required for Done: live readback/idempotency evidence and genuine owner inspection. A model cannot supply the owner's approval or validation.

P01-S015 route: Codex, OpenAI **gpt-6.1-sol**, Medium, Standard. Fallback and fresh implementation reviewer: Claude Code, Anthropic **claude-sonnet-5-5**, Medium. An explicit provider handoff records actor/model/effort and releases/reacquires the guard at a safe boundary. No silent mid-operation switch. Reviewer CLI authentication is verified by a sanitized read-only status check; specific model entitlement must still pass before the review gate. No Astra, Opus-family defaults, Fable, maximum reasoning, bought credits, or unbounded background agents.

Budget class: **Normal** for P01-S015. No subscription allowance is observable from the checked tools; do not invent its percentage. Follow SYS-CTL's 70% warning/85% new-story stop if a real allowance meter becomes available. No extra subscription or paid resource purchase is authorized. Other stories retain their prescribed routes and resolve exact models/budgets only on activation.

## Rollback and scope expiration

Before each story, commit accepted evidence and record the exact pre-story commit. Roll back tracked implementation through a targeted `git revert <recorded-story-commit>` after checking for intervening changes; never use hard reset or broad cleanup. Keep event, approval and finding history. Runtime recovery uses the owning operation's recorded checkpoint, not deletion of the whole `.goagentic/` tree.

Remote rollback removes only IDs created by the recorded operation, or restores exact prior values after comparison with the before/after snapshots. Closing the new S015 issue is allowed rollback; public issue creation cannot be fully undone by closing it. Do not delete the issue or erase its history. New Project deletion requires a **separate explicit owner approval**, as P01-S015 section 13 requires. Never delete a pre-existing Project. Detailed command contract and sequence are in activation.md.

Authorization expires on completion of P01, owner revocation, material scope/risk/target/architecture change, changed Project identity/visibility, or changed approved specifications/packet content. Routine checkpoint commits, GitHub-assigned IDs, documented exact model refresh at later activation, and evidence additions do not silently expand the allowed operations. Expired research blocks execution until refreshed; a material research finding requires a new preview.

## Exact requested authorization

After inspecting the packet and its containing commit, the requested statement is:

> I approve P01 phase scope preview ACT-P01-S015-2026-10-25-r1 at the preparation commit shown in the handoff, including one private banksjim Project, the specified fields and two views, 137 initial drafts, conversion of P01-S015 into one public repository issue, and the listed bounded local P01 operations and gates. I authorize execution of P01-S015 only, subject to its pre-write tests and independent review. Later stories still require explicit activation. No git push or whole-Project deletion is authorized.

This preparation document is a request for that statement, not a record that it was supplied.
