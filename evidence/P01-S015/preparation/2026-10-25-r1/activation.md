# P01-S015 activation packet

- **Packet:** ACT-P01-S015-2026-10-25-r1
- **Prepared:** 2026-10-25, America/Denver
- **State:** Prepared for owner review; story remains Planned / Implementation / Approval
- **Implementation and external changes:** Not started
- **Execution actor:** Human + LLM
- **Risk:** Baseline High; derived Critical for the explicitly previewed public issue
- **Budget:** Normal; no credit purchase authority

## Authority and revision binding

The specification baseline is `ef2833a8fce8bbb11262b7890883c07ea9e73b31`. `authority-manifest.json` pins every README/docs Markdown file by repository path, Git blob and SHA-256. The controlling documents are:

1. `docs/specifications/program/LOCAL-AI-AGENTIC-WORKSTATION-PROGRAM.md` (phase sequence, Ready-state issue mapping, learning and change control).
2. `docs/specifications/systems/GOAGENTIC-CONTROLLER.md` (SYS-CTL bootstrap protocol, canonical runtime/layout, commands, board mapping, model routing and trust stages).
3. `docs/specifications/phases/P01-program-control-and-quality-foundation.md` (phase preview/authorization and story order).
4. `docs/stories/P01/P01-S015-bootstrap-the-visible-github-project.md` (current story scope, evidence, owner validation and rollback).
5. `docs/specifications/standards/STORY-CONTRACT.md` (required properties/sections, derived risk, controls and activation contents).

The preparation commit containing this file is the packet revision; its parent is the specification baseline. `packet-manifest.json` seals the exact prepared artifact bytes, excluding itself. The directory-local `.gitattributes` preserves these bytes across checkouts; source-document hashes separately use canonical LF text as declared in authority-manifest.json. Approval must identify this packet and that commit. Verify hashes before recording approval. The versioned preparation directory is immutable once approved; a changed packet receives a new revision. Do not overwrite approval or human records.

The master header still says remediation is in progress while README/review describe planning remediation as complete. This is a historical status-description inconsistency, not implementation evidence. This packet relies on the pinned requirements and fresh structural checks, makes no new formal semantic-review claim, and does not change the master header.

## Prepared artifacts and prerequisites

| Artifact | Purpose |
|---|---|
| `phase-mutation-preview.md` | Complete P01 scope, exact external operations, per-story local ownership, approval text and exclusions. |
| `project-plan.json` | Exact Project title/owner/privacy, 13 fields and option values, two views, import count/body rules, lifecycle overlays, public issue text and transport. |
| `story-inventory.json` | All 137 stories sorted by Phase and Sequence, original workflow metadata, prescribed route, dependencies, pinned links and hashes. |
| `authority-manifest.json` | Exact specification revisions and content hashes. |
| `sources.md` | Dated current primary sources, verified facts, limitations and freshness window. |
| `prerequisites.json` | Sanitized live identity/scopes, empty remote inventory, repository permissions, origin/refs and installed versions. |
| `issue-inventory.json`, `provider-auth.json` | Empty repository issue inventory and whitelisted read-only reviewer authentication status; no credential values or account email retained. |
| `github-api-schema.json` | Read-only live GraphQL input/object schema for selected operations. |
| `prepare.py`, `validation.json` | Rerunnable preparation-only structural validator/collector and observed verdict. Uses the already installed Python 3.13.5, without dependencies; this is not the future PowerShell controller. |
| `review-handoff.md` | Narrow, fresh cross-provider review request to use after the bootstrap implementation exists. No review verdict is fabricated now. |
| `packet-manifest.json` | SHA-256 seal for the preparation bundle. |

Observed: 137 unique Planned stories; contiguous per-phase sequences; all 137 graph nodes visited without a cycle; reciprocal dependency/unlock links; 16 required sections per story; prescribed five-part model routes; phase tables agree; 184 local links resolve. The initial worktree was clean; local workspace exclusion works. Origin and remote main/HEAD match the specification baseline. Current branch is main. Git, gh, Python, Codex and Claude Code are installed; Windows PowerShell 5.1 is available. The exact versions are in prerequisites.json.

Live GitHub account is personal user banksjim (numeric ID 7800938). Granted project and repo scopes and ADMIN repository access are verified without retaining credential values. Existing Project count is zero with pagination exhausted; repository issue count is zero. Repository is PUBLIC. No write operation, token renewal, installation, account permission change, Project creation, issue creation, or controller implementation has run.

## Resolved target and paths

Project: **Local AI Workstation Playbook (LAW-WIN)**, banksjim, PRIVATE. The Project number/ID/URL do not exist yet; capture them from the successful create response and persist them before continuing. Never invent a future number or choose a Project by title alone after creation. Exact fields and view specifications are in project-plan.json.

Repository content remains under the existing Windows repository. No H-drive, WSL, container, registry, firewall, service or global tool configuration target belongs to this story. User filesystem, credentials and private knowledge outside the repository are excluded.

After approval, implementation outputs are fixed as:

- `goagentic/bootstrap/ProjectBootstrap.ps1` (dependency-free Windows PowerShell 5.1-compatible operation).
- `goagentic/bootstrap/BootstrapLedger.md` (one active story, revision, actor, authorization reference, checkpoint and append-only entries).
- `goagentic/bootstrap/project-mapping.json` (captured owner/Project identity and owned field/view/Story ID mappings; local commits only).
- `goagentic/tests/bootstrap/Run-Tests.ps1` and fixtures under `goagentic/fixtures/bootstrap/`.
- `evidence/P01-S015/execution/approval.md`, `research.md`, `test-results.json`, `review.md`, `owner-validation.md`, `project-before.json`, `project-after.json`, `reconciliation.json`, `rollback-plan.md` and append-only `journal.jsonl` (sanitized).
- Ignored `.goagentic/bootstrap-lock.json` and `.goagentic/P01-S015/` request/response/checkpoint files. Persist only sanitized state, never OAuth tokens or complete authentication output.

These paths are planned; the bootstrap operation and tests do **not** exist now. Their creation is the first post-authorization implementation work. Their absence is not silently treated as a passing test.

## Operation and command contract

The following are **planned invocation contracts**, not commands to run before authorization:

```powershell
# Synthetic tests: no network writes; use isolated repository-owned fixtures.
& .\goagentic\tests\bootstrap\Run-Tests.ps1 -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1

# Preview reads remote state and writes only sanitized evidence.
& .\goagentic\bootstrap\ProjectBootstrap.ps1 -Mode Preview -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1

# Apply requires the genuine approval record, exact packet hashes and owned lock.
& .\goagentic\bootstrap\ProjectBootstrap.ps1 -Mode Apply -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1 -ApprovalPath .\evidence\P01-S015\execution\approval.md

# Verify performs readback and writes sanitized evidence only.
& .\goagentic\bootstrap\ProjectBootstrap.ps1 -Mode Verify -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1

# Rollback previews by default; ApplyRollback requires the original approved scope.
& .\goagentic\bootstrap\ProjectBootstrap.ps1 -Mode Rollback -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1
& .\goagentic\bootstrap\ProjectBootstrap.ps1 -Mode Rollback -ApplyRollback -PacketPath .\evidence\P01-S015\preparation\2026-10-25-r1 -ApprovalPath .\evidence\P01-S015\execution\approval.md
```

Implementation sequence, with one operation owner:

1. Confirm exact packet/specification hashes, fresh official sources, identity, scopes, clean worktree, empty target inventory and absence of another live writer. Record actual owner authorization verbatim; commit it. Establish the bootstrap ledger and owned lock with host/process identity and safe checkpoint. Record the pre-implementation commit as the local rollback point.
2. Implement only the bootstrap operation, fixtures and tests; implement request serialization through JSON files and `gh api --input` to avoid Windows native-argument quoting problems. Use `gh project` primitives where their installed flags cover the operation; use supported GraphQL/REST through the same authenticated CLI for the rest. Never expose token values.
3. Run all synthetic cases below, rehearse rollback in a disposable fixture, and obtain a genuine fresh cross-provider implementation review. Resolve findings and rerun affected cases. Commit the reviewed operation. No external writes before these gates pass.
4. Save the pre-change Project and issue inventories. Create one shell under the pinned owner, record the returned identity, explicitly set PRIVATE, read privacy back, and stop if it is not false. No item import occurs before privacy passes. This shell checkpoint must be durable before further writes.
5. Reuse Title/Status, configure canonical Status options before assigning any items, and create the 11 approved custom fields. Record each successful response's owned IDs before the next write. Create/configure the two exact views with the documented REST endpoint; verify layouts, ordered visible fields, sort and status columns through readback. Stop on capability mismatch; do not substitute a third layout or silently omit fields.
6. Import all 137 source stories in Phase/Sequence order in 14 batches of at most 10 items. Before each creation, reconcile every paginated item by Project ID plus the Story ID in its body/field. After create, journal the item ID before setting fields. A response lost after a mutation requires remote inventory reconciliation, never an unkeyed retry. Duplicate keys or unknown edits stop execution.
7. Apply only the explicit active-story overlay. Convert P01-S015's existing draft into its single public issue using `convertProjectV2DraftIssueItemToIssue` and the pinned repository node ID. Its draft body must equal the approved publicIssueBody **before conversion**, so private Project data cannot be published. Preserve the Project item identity and field values, verify one linked issue, and never create another issue to repair an ambiguous conversion. The other 136 items remain drafts.
8. Verify all live acceptance assertions, take after snapshots, and run Preview again. An unchanged rerun must propose zero creation, updates, conversion or deletion. Retain actual and expected counts, field/view/item ID mapping, before/after values and API results. Do not equate successful API exit codes with acceptance.
9. Ask the owner to open the private Project and validate the backlog, fields, views and one next action; record the owner's own confirmation. Until then, P01-S015 remains Waiting / Human Validation / Approval. After real acceptance/review/evidence, record Done, close its public issue as completed, and show P01-S001 as the only eligible story awaiting explicit story activation. Commit accepted evidence, reconcile the board, release only the owned lock, and stop.

No program controller command exists yet. This story uses the SYS-CTL manual bootstrap protocol, not a fictitious `goagentic go`. Known provider/model/effort are recorded per checkpoint. API throttling/outages pause safely and honor Retry-After; no unbounded retry loops, purchases or parallel writers. Any uncertain mutation is inventoried before retry. If executing scripts needs a host execution-policy change, stop; a global policy change is not authorized. Scripts must run under the current session's permitted execution mechanism.

## Test matrix and evidence

Every case is required and must report a nonzero assertion count. These tests are specified here and will be implemented after authorization; only the preparation checks have run now.

| ID | Executable check after implementation | Expected result / fixture |
|---|---|---|
| B01 | Run-Tests.ps1: packet manifest/specification verification | Approved hashes pass; changed packet, unknown story, stale research, wrong owner, missing/forged approval and dirty worktree stop before writes. |
| B02 | Run-Tests.ps1: clean empty mock import | One private Project, 11 new custom fields, canonical built-ins and two required views; 137 unique story items with complete declared metadata. |
| B03 | Run-Tests.ps1: idempotent rerun | Same mock state yields zero mutations, no duplicate item or issue, stable mappings and equivalent verified values. |
| B04 | Run-Tests.ps1: interrupted import fixtures | Interrupt after shell, fields, views, every batch boundary, item response before field assignment, and uncertain response. Resume reads inventory and finishes without duplicate creation; unknown state stops. |
| B05 | Run-Tests.ps1: drift/auth/outage/rate fixtures | Lost scope, API/schema drift, wrong privacy, pagination >100, duplicate Story IDs, manual field edits, throttling, and connection failure all stop safely with evidence and one recovery action. |
| B06 | Run-Tests.ps1: lock/ownership fixtures | Second writer rejected. Expired timestamp alone does not clear a lock. Interrupted owner recovery requires inspection; no delete outside recorded ownership. |
| B07 | Run-Tests.ps1: public issue conversion fixture | 137 initial drafts, then exactly 136 drafts plus one S015 issue; approved body only, field values preserved, repeat conversion rejected, no issue for another story. |
| B08 | Run-Tests.ps1: rollback rehearsal | Remove only owned fixture fields/views/items, close only the recorded new issue, retain logs, and refuse to delete a pre-existing or whole Project. Unknown/intervening edits block automatic restore. |
| B09 | Run-Tests.ps1: secret/scope fixtures | Known synthetic credential patterns, private Project details in public issue payload, private source text and out-of-repository targets rejected; sanitized public issue text passes. |
| B10 | ProjectBootstrap.ps1 -Mode Verify | Exactly one target private personal Project, 13 expected visible fields/types/options, exactly two correct views, 137 stable keys and correct Phase/Sequence/workflow values, and only the recorded issue conversion. All paginated nodes read; zero inventory is failure. |
| B11 | ProjectBootstrap.ps1 -Mode Verify: links | All 137 pinned specification URLs correspond to files proved present at the baseline remote commit and return valid GitHub resources; no invented evidence URL. Owner verifies practical clickability during inspection. |
| B12 | ProjectBootstrap.ps1 -Mode Preview after Verify | Zero proposed mutations against an unchanged completed target. Write the actual reconciliation result. |
| B13 | Independent review / owner checkpoint | Real Anthropic reviewer identity/route and findings recorded; Critical/High findings resolved; owner opens URL, reads fields, locates only next story, confirms no workstation setup. No model-authored human evidence. |

Synthetic fixture inventory must include `empty-project`, `completed-project`, `duplicate-story`, `unknown-edit`, `partial-item`, `lost-response`, `expired-lock`, `wrong-owner`, `public-project`, `missing-scope`, `schema-drift`, `pagination-137`, `throttled`, `outage`, `rollback-owned`, `rollback-unowned`, `public-payload-leak`, and `forged-approval`. Fixture directories are disposable within `goagentic/fixtures/bootstrap/`; runtime temporary copies stay under `.goagentic/P01-S015/fixtures/`. No real services or public data are changed by tests.

## Checkpoints and rollback

Safe stops: before any mutation; after locally reviewed operation; after Project shell and verified privacy; after fields; after views; after each ten-item batch (last batch seven); after issue conversion; after live reconciliation; before human acceptance; and after accepted-evidence commit. Journal each individual successful mutation as well as batch checkpoints. A crash between an API success and journal append must be recovered from remote stable keys.

Local rollback point is the exact packet/approval commit recorded in the bootstrap ledger before implementation. After review, record another pre-live-write implementation commit. To roll back tracked implementation, inspect the diff, then run `git revert <recorded-implementation-commit>`; use additional targeted revert commits in reverse order if needed. No `git reset --hard`, broad delete, force push, or history rewrite. Preserve evidence and checkpoints even when disabling code. A rollback command containing a recorded ID is resolved from the journal, never guessed from a placeholder.

Remote rollback command contract is the reviewed operation's `-Mode Rollback` preview followed by `-ApplyRollback` only for original-scope owned records. Its exact permitted GitHub primitives are `deleteProjectV2Item(projectId,itemId)`, `deleteProjectV2Field(fieldId)` and `deleteProjectV2View(viewId)` for created IDs, field restoration for matching before/after state, and `gh issue close <recorded-issue-number> --repo banksjim/local-llm-setup --reason "not planned"` for the one newly created issue on abandonment. Restore/cleanup in reverse creation order and preserve unrecognized changes. Close the issue before removing its Project item. The public issue/history remains visible; publication is not fully reversible.

The bootstrap operation must refuse whole-Project deletion under this authorization. If the owner later explicitly approves deletion of the verified newly created Project, the separately previewed command would be `gh project delete <recorded-project-number> --owner banksjim`; never execute it for a pre-existing Project. No deletion approval is requested in this packet.

## Holds and unresolved conditions

**Current blockers to execution:** owner authorization is absent; bootstrap operation/tests are intentionally not implemented; genuine cross-provider review and owner validation have not occurred. These are explicit workflow gates, not missing design choices. Story remains Planned and cannot become Ready merely because these files exist.

**Pending live checks, not assumptions of success:** write entitlement, server-generated IDs/default resources, final view behavior, actual issue conversion, idempotency and rollback. Their exact capture rules, expected results and stop behavior are fixed above. Failure stops at the recorded checkpoint; a material API limitation needs a revised preview, not a workaround invented during apply.

**Reviewer access:** Claude CLI installation and first-party claude.ai login with a Pro subscription are verified in provider-auth.json. Entitlement to claude-sonnet-5-5 is not established by login status. Model access and genuine fresh review must succeed before external writes; otherwise report a review hold. No login renewal or purchase is authorized implicitly.

**No unresolved architecture/scope decision is delegated to the executor.** Exact future P01 model names, non-S015 activation details and later-phase tools are deliberately governed by their own research/activation stories. Phase scope approval does not turn those future stories Ready.

The first authorized next action after an accepted approval is to record the genuine authorization and bootstrap checkpoint, then implement/test/review P01-S015's bounded operation. It is not Project creation immediately, and it is not P01-S001 execution.
