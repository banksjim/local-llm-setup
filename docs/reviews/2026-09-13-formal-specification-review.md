# Formal Specification Review

**Review date:** 2026-09-13  
**Scope:** Master program, four system specifications, ten phase specifications, canonical story contract, current 137-story inventory, README, navigation, local/remote delivery state, and removed legacy paths

**Method:** Two adversarial architecture passes, requirement trace, bootstrap-dependency analysis, story-sizing review, semantic anti-pattern scan, schema inspection, sequence and dependency-DAG validation, reciprocal-reference validation, link validation, obsolete-path inspection, and Git checks

**Result:** Batches 1 and 2 pass their bounded reviews; full-program remediation remains in progress

## Executive conclusion

The former plan was not safe to execute as written. It combined two operating systems and several independent systems in one document, contained bootstrap and runtime-boundary contradictions, used an overloaded state model, and did not express all approved work as testable stories. Later passes corrected many structural defects but incorrectly treated structural completeness as semantic completeness. A deeper audit found widespread template-only scope, evidence, rollback, completion, routing, and risk language. The architecture remains a useful Windows-only, ten-phase decomposition, but the specification set is not yet safe to execute without remediation.

No workstation implementation has started. P01-P02 and P03-P05 passed their bounded batches. P06-P09 completed first Batch 3 correction cycles, but P10 and the Batch 3/full-program reviews remain blocking. No story may become Ready merely because its document exists.

## Withdrawn decision and active remediation

The prior “Pass with corrections applied” decision is withdrawn. The active remediation record is [2026-09-13-specification-remediation-log.md](2026-09-13-specification-remediation-log.md).

The deeper audit found:

- 123 of 129 story scopes still depended on template language rather than named outputs and boundaries;
- 89 evidence and completion sections were generic;
- 67 rollback sections did not describe the story-owned state;
- preferred routes did not consistently provide all five contract fields;
- risk rationales were commonly copied instead of derived; and
- implementation stories did not consistently define reusable operations for later installer composition.

These findings are material. The final review decision stays open until all three remediation batches complete and two consecutive full-program passes find no material defect.

## Findings and corrections

| ID | Severity | Problem found | Correction applied |
|---|---|---|---|
| R01 | Critical | One “kitchen sink” specification mixed controller, workstation, RAG, agents, memory, Windows, and macOS concerns. | Created one master, ten phase specs, four system specs, a story standard, and 129 story documents. |
| R02 | High | Windows and macOS were one execution program despite independent machines and timing. | Made Windows the only active program; retained macOS as a separate future program with its 175 GB constraint. |
| R03 | Critical | The controller initially depended on WSL and client tools installed later. | Defined a Windows Controller Core, P02 migration to Ubuntu, fixture adapter tests in P01, and live client tests in P05. |
| R04 | High | The command table marked `go` both invalid and executable. | Defined `go` only as the subcommand in `goagentic go`; standalone or conversational “go” is not authorization. |
| R05 | High | Workflow values mixed state, activity, and blocking causes. | Replaced them with orthogonal Status, Step, and Hold reason fields plus mappings and examples. |
| R06 | High | Risk labels were esoteric and assignment was subjective. | Adopted Low, Medium, High, and Critical; eight dimensions; highest wins; LLMs cannot lower risk. |
| R07 | High | Story sections were recommendations rather than enforceable completeness. | Made every property and 16 sections mandatory; unexplained omission and not-applicable values fail. |
| R08 | High | Cross-phase dependencies used prose rather than immutable story IDs. | Linked every phase boundary to exact preceding and following story IDs and validated all references. |
| R09 | Critical | Hardened Ubuntu could not mount `H:`, while ingestion needed `H:\ai`. | Assigned ingestion to a narrowly mounted Rancher Desktop service; WSL agents cannot browse real sources. |
| R10 | High | Langflow risked becoming a competing primary UI. | Kept Langflow as learning/design administration and required the accepted flow to be callable from Open WebUI. |
| R11 | High | The plan implied Docling could produce the final metadata format directly. | Specified lossless Docling JSON plus Markdown and a deterministic token-free YAML-frontmatter stage. |
| R12 | High | Markdown-only storage could silently lose complex table/layout data. | Made original snapshots and Docling JSON canonical private records; Markdown is the Git derivative. |
| R13 | Critical | Private documents and the public playbook boundary were underspecified. | Separated source and knowledge repositories; real data never enters this public repository; remotes must be private. |
| R14 | High | Reingestion and missing sources could cause destructive replacement or deletion. | Preserve source versions, use Git history, mark missing sources, and require approval for deletion. |
| R15 | Medium | Important visuals could be lost or invisible to retrieval. | Preserve meaningful assets, use Git LFS thresholds, and add provenance-labeled local vision enrichment. |
| R16 | High | “Speech-to-text” conflated chat audio with Windows-wide dictation. | Split chat STT from a dedicated desktop-dictation selection and implementation specification. |
| R17 | High | The full PowerShell installer and maintenance suite was not explicitly gated. | Added it to P10-S008 with analysis, dry-run, idempotency, rollback, and deliverable checks. |
| R18 | High | Sharing one Windows token into WSL would undermine isolation. | Defined one credential store per security environment: Windows once and Ubuntu once, never per repository. |
| R19 | High | Local models might be used too early or never adopted. | Added role qualification and mandatory P03 reassessment of every remaining story, with probation and cloud review. |
| R20 | Medium | Learning content could go stale or become generic courses. | Made targeted lessons blocking and required current official docs plus vetted short/deep materials at activation. |
| R21 | High | RAG acceptance inputs were ambiguous. | Defined nine categories and three owner examples each: 27 private inputs plus public synthetic fixtures. |
| R22 | Medium | Backup destination was prematurely implied. | Kept managed storage provider-neutral; OneDrive, NAS, or both are selected and tested later. |
| R23 | High | Coding-harness and software-factory work competed with real-agent learning. | Deferred both; retained only the evaluation test harness required to measure agents. |
| R24 | Low | Generated browser-workflow folders obscured durable documentation. | Removed temporary preview state and the old workflow-specific tree; retained ordinary Markdown, Mermaid, and tables. |
| R25 | Medium | The draft omitted a stable zero-context entry artifact. | Required a static `START-HERE.md` in P01-S004 that points to `goagentic` and contains no dynamic status. |
| R26 | Critical | The visible GitHub Project was not created until late in P01, so the owner could not observe the plan while the controller was being built. | Added P01-S015 as sequence 1: create the personal Project, fields, views, complete deduplicated draft-item backlog, and durable URL before other work. P01-S011 now automates an existing board. |
| R27 | Critical | Early P01 stories required valid controller state and a mutation lease while those capabilities were still under construction. | Added an explicit Git-based P01 bootstrap ledger, lock, authorization, checkpoint, evidence, and manual-reconciliation protocol with staged retirement as controller controls pass. |
| R28 | High | Local cleanup and README commits had not reached the remote, while empty legacy directories remained locally; GitHub therefore still displayed removed files. | Removed the empty directory shell, retained no active legacy files, documented the removal, and made commit/push/fetch comparison part of delivery verification. |
| R29 | High | 109 learning sections used an ambiguous generated alternative instead of identifying why learning was not applicable. | Replaced every instance with an exact preceding learning-story reference or a story-specific reason; added a validator rejection for the old pattern. |
| R30 | High | Fourteen stories said current research was not applicable and then instructed the executor to record current research. | Removed all contradictory boilerplate and retained a concrete reason tied to accepted versions, fixtures, or owner validation. |
| R31 | High | P10-S008 combined the full installer, maintenance suite, all guides, diagrams, and prompts in one non-tactical story. | Split production into P10-S012 through P10-S015 and made P10-S008 a read-only catalog-validation gate. |
| R32 | Medium | The future macOS plan could either repeat all training or silently assume Windows knowledge. | Defined portable prior-learning dispositions, exact evidence and freshness checks, and mandatory macOS-specific delta learning while preserving standalone execution. |
| R33 | High | Planned stories intentionally defer current versions and exact targets, but the readiness transition did not require those variables to be resolved before execution. | Added a committed Ready-state activation packet with exact revisions, targets, versions, tests, risk, route, approvals, checkpoints, and rollback; unresolved material assumptions block Ready. |
| R34 | Critical | Structural completeness was incorrectly reported as a semantic pass even though most stories still contained template-only scope, evidence, rollback, routing, risk, and completion language. | Withdrew the pass decision, added executability/specificity rules and a bounded review stop rule, and began three remediation batches tracked in a durable log. |
| R35 | High | A dependency-check command matched zero story files and still printed `PASS`, demonstrating that a green result without an asserted test inventory is unsafe. | Corrected the filter, required exactly 129 stories and nonempty phase inventories, reran successfully, and made zero-applicable-test success invalid in the canonical contract. |
| R36 | High | “One approval per privileged phase” was still conflated with later human learning, login, elevation, and acceptance actions. | Defined one revision-bound phase authorization and distinguished later required human participation; material scope, target, risk, or operation change invalidates the authorization. |
| R37 | High | P01 implicitly depended on Pester even though its bootstrap must run before later tooling is installed. | Required dependency-free Windows PowerShell tests in P01; an external framework is permitted only if current inventory proves it is already present and the activation packet pins it. |
| R38 | Critical | Early P01 execution contracts still required acquiring the controller lease before P01-S006 implemented and accepted that lease. | Required the Git-based bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted. |
| R39 | High | P02 referred to a dedicated Linux user without assigning any story to create, select, or verify that account. | Added one owner-named non-root default account to P02-S005, prohibited password capture, and required default-user and secret-leak checks. |
| R40 | High | P04 used one integration story for search, extraction, vector storage, speech, and acceptance, preventing independent execution and diagnosis. | Decomposed it into five bounded stories and updated the dependency graph, phase table, README count, and downstream P05 dependency. |
| R41 | High | Current VS Code and extension facts had drifted: the built-in Ollama provider is deprecated, local BYOK chat does not provide inline suggestions, and Continue is no longer actively maintained. | Required current official Ollama-publisher provider research for chat, separated optional autocomplete research, and prohibited preselecting Continue. |
| R42 | Critical | The plan put models and project data on `H:` but silently left Rancher's growing WSL data disk and named volumes on the system drive. | Added exact `H:\ai\containers` distribution/snapshot targets, current Microsoft/Rancher method research, verified export and inventory checks, reset-path revalidation, and a prohibition on live PostgreSQL bind mounts. |
| R43 | Medium | Nine P03-P05 human-validation sections still named generic GUI, credential, elevation, and microphone actions, including actions irrelevant to their stories. | Replaced them with exact owner actions, private-input boundaries, and story-specific evidence. |
| R44 | High | The backlog headline said 132 stories while its phase table still listed P04 as 11, yielding an internally inconsistent total. | Corrected P04 to 14 and added a phase-count sum assertion to the review. |
| R45 | High | OpenWhispr's current scope now includes accounts, sync, meetings, calendars, agents, screen context, and remote interfaces beyond local dictation. | Kept it as a benchmark candidate but required a minimal dictation-only configuration, explicit feature disablement, connected traffic capture, and disqualification if unrelated access cannot be disabled. |
| R46 | High | The Open WebUI document/vector story did not explicitly bind indexing and query to the same accepted embedding model and dimension. | Added the P03 profile/dimension to configuration and made mismatch a pre-index hard failure. |
| R47 | High | Three acceptance stories named prohibited outcomes but did not explicitly make their detection fail the automated gate. | Added zero-fixture, external-traffic, isolation, restore, workflow, and boundary failure clauses to P04-S012, P04-S014, and P05-S012. |
| R48 | High | Six story-specific human-validation gates still allowed ambiguity about whether an LLM could author the owner's observations. | Added explicit anti-fabrication language to each gate and validated all 15 P03-P05 human gates independently. |
| R49 | Medium | P05 cited Ollama's Claude Code integration but omitted Claude Code's own current configuration authority. | Added the current official Claude Code configuration reference and included its domain in the source-baseline check. |
| R50 | Critical | P06 treated Ollama, LangChain, LangGraph, MCP, skills, and MLflow as a generic implementation objective without fixed authority, persistence, privacy, or evaluation boundaries. | Fixed the layer responsibilities; constrained the first agent and MCP server to synthetic read-only capabilities; required dedicated checkpoint storage, replay-safe effects, pre-emission trace redaction, deterministic safety checks, and 14 story-specific contracts. |
| R51 | Critical | P07's leaf stories were generic, publication was not atomic across Git and vectors, private-source safety was incomplete, the plan taught Langflow before any story deployed it, and no story initialized the separate knowledge repository. | Rebuilt SYS-RAG around immutable source, normalized record, Git derivative, and disposable index layers; added a durable job state machine with paired Git/index reconciliation; specified file, web, OAuth, credential, deletion, and restore denials; and inserted P07-S018 and P07-S019 as explicit Langflow and private-repository prerequisites. |
| R52 | Critical | P08 described personal-agent personas without a deployable shared runtime, combined two agents in one story, relied too heavily on prose boundaries, and did not clearly separate thread checkpoints, explicit exports, and future durable memory. | Added P08-S012 for a private LangGraph/Open WebUI runtime and P08-S011 for daily check-ins; rebuilt all 12 contracts around deterministic policy enforcement, bounded capabilities, current primary sources, redacted MLflow evaluation, explicit export confirmation, and a hard P09 memory boundary. |
| R53 | Critical | SYS-MEM allowed a deterministic rule to promote memory, treated a framework store as potentially authoritative, omitted a deployment story, and left candidate isolation, decision replay, deletion resurrection, and the pilot agent ambiguous. | Made owner review the sole promotion authority; separated quarantined candidates, an append-only portable ledger, and rebuildable projections; added P09-S013 deployment; specified anti-replay decisions and deletion tombstones; and fixed the accepted P08 life-planning agent as the only P09 pilot. |

## Redundancy removed

- One authority hierarchy replaces repeated precedence descriptions.
- One command contract owns pause, resume, authorization, and next-action behavior.
- One story contract owns fields, sections, lifecycle vocabulary, and risk rules.
- System specs own cross-phase architecture; phase specs contain only gates and order.
- Obsolete specifications and temporary walkthrough plans were removed from the active tree.
- Repeated story sections remain intentionally because each story must execute independently in a fresh LLM context.
- Stable story IDs remain unchanged when sequencing corrections are inserted; the separate Sequence field controls execution order.

## Owner requirement trace

| Requirement group | Authoritative coverage |
|---|---|
| Windows 11, 9800X3D, RTX 4090, 64 GB, and `H:\ai` | Master sections 1, 2, 7, and 8; P02, P03, and P10 |
| Open WebUI, Ollama, current primary/fast/vision models, SearXNG, Docling, and Rancher Desktop | Master sections 2 and 7; P03 and P04 |
| Windows-wide local dictation rather than chat-only STT | SYS-STT and P05-S001 through P05-S004 |
| VS Code, Codex CLI, Claude Code, desktop-client compatibility, optional autocomplete, and LM Studio localhost port 51239 | P02, P05, and P10-S014 |
| Python, Go, Node.js, and TypeScript inside protected Ubuntu WSL | P02 and master security boundaries |
| LangChain, LangGraph, MCP, skills/assets/scripts, MLflow, and targeted learning | P06 and master learning policy |
| RAG, Langflow, Crawl4AI, nine source categories, deterministic YAML, visuals, and 27 private samples | SYS-RAG and P07 |
| Personal agents and reviewed-inbox durable memory with current OSS selection | SYS-MEM, P08, and P09 |
| Idempotent installer, maintenance, architecture/model/usage guides, prompts, troubleshooting, updates, backup, restore, and removal | P10-S012 through P10-S015, then P10-S008 catalog validation |
| Visible GitHub Project, pause/resume, model routing, and provider-independent long-running control | SYS-CTL and P01, beginning with P01-S015 |
| Current-source research rather than training-memory assumptions | Story freshness property, Ready-state activation packet, and phase research stories |
| Independent future macOS installation without unnecessary repeated learning | Master learning policy and canonical portable-learning-credit policy |
| No workstation build before explicit authorization | Master gates, SYS-CTL command contract, and every story approval boundary |

## Deliberately deferred decisions

These are controlled gates, not missing requirements:

- Exact versions and image digests: refreshed in phase research stories.
- Final models and contexts: selected by P03 measurement on the RTX 4090.
- Desktop dictation winner: selected by P05 owner benchmark.
- Open WebUI-to-Langflow mechanism: selected from current supported interfaces in P07.
- Durable memory framework: selected through current OSS evaluation and an owner-approved ADR in P09.
- OneDrive, private NAS, or dual backup: selected before P10 backup implementation.
- Knowledge-base Git remotes: absent by default and added only through a private approved action.

## Automated review results

The earlier Batch 1 table is retained as structural-history evidence, not a current full-program pass. At that time 129 story files were asserted and all 27 P01-P02 stories passed. The current inventory is 137 after P04 decomposition and the added P07-P09 prerequisites. Batch 2 completed two consecutive clean passes covering all 37 P03-P05 stories. P06-P09 correction cycle 1 replaced all prior generic contracts and routes in those phases. P10 still contains 10 measured generic core story blocks and 15 incomplete routes. Batch 3 has not reached its two clean passes, so these residuals keep the program review open.

| Check | Result |
|---|---|
| Story count | 137 current; Batch 1's historical assertion was 129 |
| Unique story IDs | 137 current |
| Required properties and 16 sections | Pass |
| Per-phase sequence uniqueness and continuity | Pass |
| Dependency graph | Pass; 137 of 137 reciprocal nodes visited with no cycle |
| Reciprocal dependency and unlock references | Pass |
| Phase-table sequence, step, and risk agreement | Pass |
| Local Markdown links | Pass; 184 references parsed by the current validator and all resolve |
| Ambiguous learning and contradictory research prose | Pass; zero matches |
| Placeholder and obsolete terminology scan | Pass; explanatory README history is intentional |
| Removed documentation-tree presence | Pass; no active or empty legacy folder remains locally |
| P03-P05 concrete output and evidence contracts | Pass; 37 of 37 |
| P03-P05 Critical-risk controls | Pass; four of four include authorization, negative tests, and recovery |
| P03-P05 human-validation authenticity | Pass; 15 of 15 include an owner action and anti-fabrication boundary |
| P06 contract and route remediation | Correction cycle 1 passes phase-local structural and semantic checks; 14 of 14, but no Batch 3 pass is claimed |
| P07 contract and route remediation | Checked correction cycle passes phase-local structural and semantic validation for 19 of 19; no Batch 3 pass is claimed |
| P08 contract and route remediation | Checked correction cycle passes phase-local structural and semantic validation for 12 of 12; no Batch 3 pass is claimed |
| P09/SYS-MEM contract and route remediation | Checked correction cycle passes two internal phase-local structural and semantic passes for 13 of 13; no Batch 3 pass is claimed |
| Git whitespace validation | Pass |
| Workstation implementation evidence | Not applicable — implementation has not started |

## Residual risks

- The plan is intentionally long; controller reliability and phase gates are essential.
- APIs, models, licenses, and integrations will change; freshness gates must remain blocking.
- WSL is risk reduction, not hostile-code containment. The owner still approves credentials, host access, publication, and privileged changes.
- Personal-agent and memory quality require owner acceptance, not only automated tests.
- Real-document extraction varies; the 27-document set may generate correction stories.

## Review decision

Batch 2 passes its bounded review; P06-P09 have correction cycles, but this is not a Batch 3 or full-program pass. P10 remains blocking until Batch 3 correction and two consecutive full-program passes complete. When the full program eventually passes and the owner explicitly starts P01, P01-S015 will be the only story eligible for activation; its separate mutation preview and approval will gate creation of the personal GitHub Project.
