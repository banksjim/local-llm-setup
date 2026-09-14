# Canonical Story Contract

**Contract version:** 1.0  
**Status:** Required  
**Last reviewed:** 2026-09-13

Every implementation, learning, research, testing, review, and human-intervention story is a separate Markdown document. Every property and section below is mandatory. When a value does not apply, write `Not applicable — <specific reason>`; an empty value or bare `N/A` is invalid.

## Required properties

| Property | Rule |
|---|---|
| Story ID | Stable `Pnn-Snnn` identifier; never reused |
| Phase | Stable phase ID and name |
| Sequence | Integer ordering within the phase |
| Status | Planned, Ready, In Progress, Waiting, Done, or Superseded |
| Step | Research, Learning, Implementation, Testing, Review, Human Validation, or Merge |
| Hold reason | None, Phase Not Activated, Dependency, Approval, Paused, Blocked, Usage Budget, or External System |
| Risk | Low, Medium, High, or Critical |
| Actor | Human, LLM, or Human + LLM |
| Dependencies | Exact story IDs or an explained not-applicable value |
| Unlocks | Exact story IDs or an explained not-applicable value |
| Preferred route | Five labeled fields: `Interface`, `Provider`, `Model class`, `Effort`, and `Fallback`; `Automatic` or `controller-selected` alone is invalid |
| Research freshness | Maximum age and sources that must be checked at activation |

Story ID is an immutable key, not an ordering mechanism. `Sequence` controls execution order, so a later-added story may have a higher ID but an earlier sequence. Phase indexes must sort by Sequence and explain any intentional difference.

## Required sections

1. User story.
2. Bounded objective.
3. Learning objective.
4. Current research requirements.
5. Preconditions and unlock conditions.
6. In scope.
7. Out of scope and prohibited changes.
8. Privilege and human approval.
9. Risk rationale.
10. Execution contract.
11. Automated acceptance tests.
12. Human validation.
13. Idempotency and rollback.
14. Required evidence.
15. Definition of done.
16. Pause-safe boundaries.

## Risk assignment

Assess each dimension and assign the highest resulting level:

| Dimension | Low | Medium | High | Critical |
|---|---|---|---|---|
| Privilege | Read-only/user files | User configuration | Admin or system configuration | Security boundary or broad privileged change |
| Reversibility | Trivial | Backed-up edit | Service/data restore needed | Irreversible or uncertain recovery |
| Data loss | None | Derived data | User data possible | Original or broad data possible |
| Secrets/privacy | None | Local nonsecret data | Private content or credentials | Credential transfer, exposure, or regulated data |
| Network/publication | None | Localhost | Outbound/authenticated or private remote | Public exposure or access-control boundary |
| Blast radius | One document | One component | Multiple services/host | Entire workstation or external systems |
| Cost | No meaningful cost | Small bounded use | Material quota/cost | Unbounded or purchase-capable |
| Uncertainty | Deterministic | Known integration | New/poorly characterized | Architecture-invalidating ambiguity |

The story author proposes risk. Validation derives the minimum from the table. The effective value is the higher one. An LLM cannot lower it; the owner may lower it only with a recorded rationale.

## Quality controls by risk

| Risk | Minimum controls |
|---|---|
| Low | Schema, links/static checks, evidence, lightweight independent review |
| Medium | Low controls plus unit tests, idempotency, rollback, fresh-session review |
| High | Medium controls plus integration tests, failure injection, cross-provider review |
| Critical | High controls plus explicit phase approval, isolated rehearsal, owner acceptance |

`Privilege and human approval` must distinguish authorization from participation. Each privileged phase receives one revision-bound owner authorization covering its previewed operations. A later story may require the owner to answer a lesson, authenticate, satisfy an elevation prompt, inspect a GUI, or perform acceptance; those are human actions, not additional approvals of unchanged scope. Any material scope, target, risk, or operation change invalidates the phase authorization and requires a new preview and approval.

## Lifecycle vocabulary

Status answers where the story is. Step answers what kind of work happens next. Hold reason answers why it cannot advance.

| Example | Status | Step | Hold reason |
|---|---|---|---|
| Future story whose phase is not active | Planned | Implementation | Phase Not Activated |
| Story whose prerequisites passed | Ready | Implementation | None |
| Owner must finish a lesson | Waiting | Learning | Approval |
| Installer is executing | In Progress | Implementation | None |
| Tests failed and need diagnosis | Waiting | Testing | Blocked |
| Owner paused safely | Waiting | Current step | Paused |
| Independent review requested | Waiting | Review | Approval |
| Accepted story | Done | Merge | None |
| Replaced by a newer story | Superseded | Applicable step | None |

The former display labels `Locked`, `Learning`, `Awaiting You`, `Testing`, `Review`, `Blocked`, and `Paused` are presentations of these three fields, not additional states.

## Validation rules

- Dependencies form an acyclic graph.
- Only one story may hold the mutation lease.
- A story cannot be `Done` without its required evidence and review.
- Human evidence cannot be generated by an LLM.
- Research older than the declared window blocks execution.
- Changes outside declared scope block acceptance.
- Repeating the same failed action without new evidence is prohibited.
- A story may depend only on controls that are already accepted. Bootstrap stories must name the temporary governance mechanism used in place of unfinished controller features.
- A validator must assert the expected inventory or another nonzero lower bound before reporting success; running zero applicable tests is a failure unless an explained not-applicable result is part of the accepted contract.

## Ready-state activation packet

A `Planned` story is a schedulable specification, not permission to execute. Before it can become `Ready`, the controller—or the P01 bootstrap protocol—must compile and commit a self-contained activation packet containing:

- the exact approved revisions of the master, system, phase, and story specifications;
- resolved output paths, files, services, endpoints, and ownership boundaries;
- current versions, immutable identifiers or digests where available, and dated primary sources;
- the executable test list with expected results and required fixtures;
- derived risk, approval requirements, actor, model route, effort, and budget class;
- the exact mutation preview, safe checkpoints, rollback point, and rollback commands; and
- explicit unresolved assumptions, each of which blocks `Ready` if it could change scope, architecture, safety, or acceptance.

The packet may resolve variables that were intentionally deferred for freshness, but it may not broaden the bounded objective or silently redesign the story. A material change creates a design-change story. With this packet and its cited authority chain, a fresh qualified LLM must be able to execute and test the story without chat history.

## Executability and specificity rules

A story is independently executable only when its own document and declared authority chain identify:

- concrete deliverables or state transitions;
- exact ownership boundaries and prohibited mutations;
- the reusable command, module, configuration unit, checklist, research record, or evidence artifact it creates or updates;
- observable acceptance results rather than phrases such as “tests pass”;
- story-specific evidence and rollback or repeat behavior; and
- all decisions that may safely wait for the activation packet.

The activation packet may resolve changing facts such as supported versions, immutable digests, a current model name, a selected package release, an OS-generated identifier, or an available private port. It may not invent deliverables, choose an unspecified architecture, define missing safety boundaries, or turn generic boilerplate into scope.

The following exact or equivalent language fails semantic validation unless followed by a concrete story-specific inventory: “only the objective,” “declared files and services,” “minimum safe supporting changes,” “the objective and tests pass,” or a generic evidence/rollback list that does not name the story's outputs. Repeated prose is acceptable only for genuinely shared invariants; it cannot substitute for story-specific content.

Implementation stories must expose reusable idempotent operations where the work can reasonably be automated. Later installers and maintenance commands compose those accepted operations instead of independently reimplementing them. A justified exception must name the manual-only boundary.

## Specification review stop rule

Review proceeds in bounded batches. Each batch receives structural validation, semantic review, correction, cross-document tracing, current-source review, and a fresh parent-to-leaf pass. Two consecutive full passes with no material defect are required for completion. Five correction cycles is the maximum per batch; reaching the limit leaves the batch incomplete and requires an owner-visible residual-defect report. Internal self-review must be labeled internal and cannot be described as independent or cross-provider review.

## Portable learning credit for future platform programs

A future macOS program must contain its own complete learning stories so it can run independently, but the same owner should not repeat unchanged material. Every macOS learning story must record one disposition:

| Disposition | Meaning |
|---|---|
| Required | No acceptable prior evidence exists. |
| Satisfied by prior learning | Exact prior evidence is linked and a short retention and delta check passes. |
| Delta refresher required | Core learning transfers, but current versions or platform behavior changed materially. |
| Relearn required | Evidence is missing, stale, incompatible, or the retention check fails. |

Credit requires the same owner, an exact source story and evidence reference, compatible concepts and major versions, a current-source freshness check, and a recorded retention/delta result. An LLM cannot grant credit from chat memory alone. Platform-specific learning—Apple unified memory, Metal or MLX, macOS permissions, filesystem layout, service management, storage limits, and macOS-specific Ollama or Rancher Desktop behavior—remains mandatory even when general concepts transfer.
