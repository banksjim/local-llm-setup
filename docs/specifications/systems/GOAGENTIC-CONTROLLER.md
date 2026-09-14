# Goagentic Controller Specification

**System ID:** `SYS-CTL`  
**Status:** Approved design; unimplemented  
**Bootstrap runtime:** Windows PowerShell  
**Canonical runtime after P02:** Ubuntu WSL2  
**Last reviewed:** 2026-09-13

## 1. Responsibility

`goagentic` is the durable controller for this multi-week program. It reads approved specifications, story state, evidence, Git state, and synchronized GitHub metadata; then it returns exactly one safe next action. It is intentionally provider- and interface-independent.

It does not autonomously redesign the program, purchase usage, invent approvals, or keep cloud agents continuously running. The owner is the orchestrator and manually opens the prescribed interface/model when asked.

## 2. Bootstrap and canonical execution

The controller cannot initially depend on the Ubuntu environment it will help create.

1. A minimal Controller Core is implemented and tested on Windows PowerShell.
2. It supports read-only orientation, schema validation, atomic state, logs, pause/resume, and bounded authorization.
3. P02 establishes the dedicated Ubuntu distribution.
4. The canonical controller runtime moves into Ubuntu.
5. A Windows `goagentic` wrapper forwards requests into Ubuntu and fails safely if Ubuntu is unavailable.
6. Early adapter packages are validated with contract fixtures; live PowerShell and WSL validation occurs in P02, and live Codex CLI and Claude Code validation occurs after those clients are configured in P05.

### Planned repository and runtime layout

P01 uses Windows PowerShell 5.1-compatible scripts so it has no dependency on software installed by later phases. P02-S007 installs PowerShell 7 inside Ubuntu, and P02-S011 proves the same controller modules under that runtime before switching authority. The activation packet may update this language decision only through an explicit architecture-change story.

```text
goagentic/
├── goagentic.ps1                 # stable Windows entry point
├── src/                          # side-effect-separated controller modules
├── schemas/                      # machine-readable program, story, state, and evidence schemas
├── adapters/                     # Codex, Claude Code, and later interface packages
├── fixtures/                     # synthetic valid and invalid states
└── tests/                        # dependency-free PowerShell unit, integration, and failure tests
evidence/<story-id>/              # sanitized accepted story evidence tracked by Git
.goagentic/                       # local runtime state; ignored except documented templates
```

Modules must separate planning from mutation. Every mutating operation exposes preview, apply, verify, and story-owned rollback behavior. The final installer and maintenance suite call these accepted operations rather than duplicating their logic.

P01 tests must run on a stock supported Windows PowerShell environment and may not assume Pester or another package is installed. P01-S001 may permit a pinned external test framework only if live inventory proves it is already available and the activation packet records its exact version and fallback; otherwise repository-owned assertion and test-runner scripts remain the required baseline.

### P01 bootstrap protocol

The program cannot require unfinished controller features to build those same features. Until each control is accepted, P01 uses a deliberately small manual protocol stored in Git:

- one active story recorded in a bootstrap ledger;
- one explicit owner authorization recorded before mutation;
- a repository-local lock record with actor, story, start time, operation, and safe checkpoint;
- a clean-worktree check and named rollback point before mutation;
- append-only evidence entries and a commit at each pause-safe boundary;
- manual GitHub Project reconciliation after each story; and
- stop-and-review behavior for ambiguity, drift, interruption, or a stale lock.

The protocol never pretends an unimplemented feature exists. P01-S003 introduces schema validation, P01-S005 introduces atomic state, P01-S006 replaces the bootstrap lock with the tested mutation lease, P01-S007 introduces automated reconciliation, P01-S008 introduces bounded authorization, and P01-S011 replaces manual board maintenance with tested synchronization. Each transition requires evidence that the new control preserves all earlier safeguards before the corresponding bootstrap mechanism is retired.

## 3. Command contract

Commands use `goagentic <command> [parameters]`. Bare `goagentic` is the zero-context entry point.

| Command | Behavior | May mutate project work? |
|---|---|---|
| `goagentic` | Reconstruct state and display exactly one next action | No |
| `status` | Show phase, story, step, hold, risk, lease, and evidence health | No |
| `next` | Explain the next action, interface/model, reason, and exact command | No |
| `model` | Show required model route, effort, budget, fallback, and reviewer | No |
| `verify [story]` | Run applicable deterministic checks | Evidence only |
| `review [story]` | Prepare or record an independent review | Review record only |
| `human-complete <story>` | Guide the owner to record genuine human evidence | Human evidence only |
| `pause [reason]` | Request a stop at the next safe boundary | Controller state only |
| `resume` | Reconcile state after a return, crash, or reboot; never execute work | Controller state only |
| `go` | When invoked as `goagentic go`, authorize one controller-defined execution interval; a standalone shell command or conversational “go” is not controller authorization | Yes, bounded |
| `audit` | Validate schemas, dependencies, evidence, Git, and synchronization | Evidence only |

Conversational words such as “go” are not machine authorization. Only the exact controller command counts after the controller is trusted. Before trust is established, the owner authorizes each story explicitly in the active agent session.

## 4. Bare-command response

The response must show:

- Current phase and story.
- Status, step, hold reason, and risk.
- What changed since the last checkpoint.
- Whether state, Git, and GitHub agree.
- Required interface, provider, model, effort, and budget class.
- Why that route is selected and permitted fallback.
- Whether learning, approval, testing, review, or human validation blocks execution.
- Exactly one recommended next action and its exact command.

## 5. Durable state

Authority order follows the program specification. Runtime state is atomic and append-only events are hash-linked or otherwise tamper-evident. Accepted evidence is tracked in Git without secrets. GitHub Projects is a visible mirror, not the source of truth.

Only one mutation lease exists. It records story, role, model/provider, host/process identity when observable, acquisition/heartbeat, current atomic operation, safe checkpoint, and expiry policy. An expired timestamp alone never proves a lease safe to remove.

## 6. Pause and resume

`pause` is accepted immediately and takes effect at the smallest declared safe boundary. `resume`:

1. Acquires an inspection lease.
2. Reads the last trusted checkpoint and event log.
3. Inspects Git, filesystem, running process, and relevant external state.
4. Classifies clean pause, pre-mutation crash, mid-operation crash, missing checkpoint, stale lease, drift, outage, or ambiguity.
5. Performs only predefined non-destructive reconciliation.
6. Reports the next action and releases the inspection lease.

`resume` never performs the pending story. A separate `goagentic go` is always required.

## 7. GitHub Project mapping

P01-S015 creates the personal Project before other implementation work and imports the approved backlog as deduplicated draft items. This provides visibility without creating a public repository issue for every future story. When a story becomes Ready, the controller creates or converts the corresponding repository issue using the current supported GitHub mechanism. P01-S011 automates reconciliation; until then, the P01 bootstrap protocol maintains the board manually.

The board shows Phase, Story ID, Sequence, Status, Step, Hold reason, Risk, Required model, Budget, Owner action, Specification link, and Evidence link. Examples:

| Visible situation | Field values |
|---|---|
| “Locked” future card | Planned / Implementation / Phase Not Activated |
| Lesson waiting on owner | Waiting / Learning / Approval |
| Privileged preview waiting | Waiting / Human Validation / Approval |
| Active automated operation | In Progress / Implementation / None |
| Test repair needed | Waiting / Testing / Blocked |
| Safely paused | Waiting / current step / Paused |
| Replaced requirement | Superseded / applicable step / None |

Synchronization never overwrites unexplained manual Project changes. A conflict becomes a visible reconciliation action.

## 8. Model routing

The owner normally switches models at story boundaries. The controller prescribes the interface and route. It never silently changes a model mid-operation.

| Work | OpenAI route | Claude route | Local route |
|---|---|---|---|
| Architecture/security | Sol-class, medium | Sonnet-class, medium | Only after role qualification |
| Ordinary implementation | Terra-class, medium | Sonnet-class, medium | Qualified worker model |
| Mechanical/docs | Luna-class, low/medium | Haiku-class | Qualified fast model |
| Difficult diagnosis | Sol-class, higher only with evidence | Sonnet-class, higher only with evidence | Advisory during probation |
| Independent review | Fresh session/model; cross-provider by risk | Fresh session/model; cross-provider by risk | Cloud review during probation |

Exact current product names and availability are researched at activation. Claude Opus 5 and all Opus-family defaults are prohibited. Fable is unavailable and prohibited. Astra-class models and maximum reasoning require explicit owner approval.

Usage classes are Small, Normal, and Expensive. Warn at 70% of a known included-usage window; do not begin a new story at 85% without owner override. The controller cannot buy or replenish credits.

## 9. Quality enforcement

The controller validates the canonical story contract, Ready-state activation packet, freshness, dependencies, scope, tests, idempotency, rollback, secret scan, independent review, human evidence, and completion evidence. It cannot execute directly from a generic `Planned` story. The implementer cannot be the sole reviewer. Reviewers write findings; they do not silently rewrite the work under review.

## 10. Trust stages

| Stage | Capability |
|---|---|
| Untrusted | Specifications only; owner explicitly directs work |
| Controller Core Trusted | Windows read/orient/pause/resume/authorize paths passed failure injection |
| Cross-Interface Trusted | Ubuntu canonical runtime and every configured adapter passed both fixture and live contract tests; this stage cannot be reached before P05 |
| Local Model Probation | Qualified tasks run locally with cloud review |
| Operationally Accepted | Owner drill and full program acceptance passed |

Failure injection covers interruption, corrupt state, stale lease, unexpected changes, GitHub outage, stopped WSL, stopped Rancher Desktop, wrong model, missing approval, duplicate writer, and simulated rollback.

## 11. Acceptance

The system passes when a fresh Codex or Claude session, Windows shell, WSL shell, or VS Code terminal can recover the same safe state; `goagentic` returns one action; `resume` never runs work; concurrent writers fail; approval and learning gates cannot be bypassed; and a guided owner drill succeeds after an application restart and a machine reboot.
