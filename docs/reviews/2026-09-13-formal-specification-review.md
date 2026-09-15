# Formal Specification Review

**Review date:** 2026-09-13  
**Scope:** Master program, four system specifications, ten phase specifications, canonical story contract, current 137-story inventory, README, navigation, local/remote delivery state, and removed legacy paths

**Method:** Two adversarial architecture passes, requirement trace, bootstrap-dependency analysis, story-sizing review, semantic anti-pattern scan, schema inspection, sequence and dependency-DAG validation, reciprocal-reference validation, link validation, obsolete-path inspection, and Git checks

**Result:** Pass for controlled planning execution; all three remediation batches and two consecutive full-program passes complete

## Executive conclusion

The former plan was not safe to execute as written. It combined two operating systems and several independent systems in one document, contained bootstrap and runtime-boundary contradictions, used an overloaded state model, and did not express all approved work as testable stories. Later passes corrected structural defects but initially mistook structural completeness for semantic completeness. Three bounded remediation batches have now replaced the template-only contracts, repaired architecture and dependency gaps, and completed two consecutive full-program passes.

No workstation implementation has started. The Windows-only ten-phase specification is now suitable for controlled execution through its controller, research, learning, authorization, testing, review, and owner gates. This verdict does not authorize implementation: no story may become Ready merely because its document exists, and only P01-S015 may be considered after the owner explicitly starts the program.

## Withdrawn decision and completed remediation

The earlier unsupported “Pass with corrections applied” decision remains withdrawn. The completed remediation record is [2026-09-13-specification-remediation-log.md](2026-09-13-specification-remediation-log.md).

The deeper audit found:

- 123 of 129 story scopes still depended on template language rather than named outputs and boundaries;
- 89 evidence and completion sections were generic;
- 67 rollback sections did not describe the story-owned state;
- preferred routes did not consistently provide all five contract fields;
- risk rationales were commonly copied instead of derived; and
- implementation stories did not consistently define reusable operations for later installer composition.

These findings were material. All three remediation batches are now complete, and two consecutive full-program passes after the final P10 correction found no material defect.

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
| R17 | High | The full PowerShell installer and maintenance suite was not explicitly gated. | Assigned production to P10-S012 and P10-S013 with analysis, dry-run, idempotency, rollback, and exact command inventories; P10-S008 independently validates the catalog. |
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
| R54 | Critical | P10 retained generic operational shells, incomplete model routes, no fixed release architecture, ambiguous backup/removal boundaries, and an early lesson that appeared to depend on final runbooks not yet written. | Rebuilt all 15 contracts around named research, lesson, security, 4090 profile, lifecycle, backup, removal, installer, maintenance, guide, catalog, end-to-end, review, and acceptance artifacts; made the lesson use accepted P01–P09 operations; and fixed exact failure, privacy, rehearsal, rollback, prompt, and release controls. |

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

The earlier Batch 1 table is retained as structural-history evidence, not the basis for the current verdict. At that time 129 story files were asserted and all 27 P01-P02 stories passed. The current inventory is 137 after P04 decomposition and added P07-P09 prerequisites. Batch 2 completed two clean passes over P03-P05. Batch 3 rebuilt P06-P10 and SYS-RAG/SYS-MEM, then completed two consecutive full-program passes after the last material correction. Pass 1 reconstructed all story metadata, phase tables, routes, and the reciprocal acyclic graph. Pass 2 independently checked concrete P10 contracts, Critical controls, exact release inventories, requirement trace, links, removed paths, and whitespace.

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
| P06 contract and route remediation | Pass; 14 of 14 and included in the clean Batch 3/full-program result |
| P07/SYS-RAG contract and route remediation | Pass; 19 of 19 and included in the clean Batch 3/full-program result |
| P08 contract and route remediation | Pass; 12 of 12 and included in the clean Batch 3/full-program result |
| P09/SYS-MEM contract and route remediation | Pass; 13 of 13 and included in the clean Batch 3/full-program result |
| P10 contract and route remediation | Pass; 15 of 15 have exact outputs, five-field routes, story-specific tests/evidence/rollback, and continuous phase sequencing |
| Batch 3 full-program review | Pass; two consecutive complete passes after the final material correction |
| Git whitespace validation | Pass |
| Workstation implementation evidence | Not applicable — implementation has not started |

## Residual risks

- The plan is intentionally long; controller reliability and phase gates are essential.
- APIs, models, licenses, and integrations will change; freshness gates must remain blocking.
- WSL is risk reduction, not hostile-code containment. The owner still approves credentials, host access, publication, and privileged changes.
- Personal-agent and memory quality require owner acceptance, not only automated tests.
- Real-document extraction varies; the 27-document set may generate correction stories.

## Review decision

The planning specification passes its bounded adversarial review. All three remediation batches and two consecutive full-program passes are complete with no known material defect. This is a specification verdict, not implementation evidence or permission to build. When the owner explicitly starts P01, P01-S015 is the only story eligible for activation; its bootstrap preview and revision-bound phase authorization gate creation of the personal GitHub Project.
