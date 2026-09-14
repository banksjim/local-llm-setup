# Formal Specification Review

**Review date:** 2026-09-13  
**Scope:** Master program, four system specifications, ten phase specifications, canonical story contract, 129 story documents, README, navigation, local/remote delivery state, and removed legacy paths

**Method:** Two adversarial architecture passes, requirement trace, bootstrap-dependency analysis, story-sizing review, semantic anti-pattern scan, schema inspection, sequence and dependency-DAG validation, reciprocal-reference validation, link validation, obsolete-path inspection, and Git checks

**Result:** Pass with corrections applied; specifications only, workstation implementation not started

## Executive conclusion

The former plan was not safe to execute as written. It combined two operating systems and several independent systems in one document, contained bootstrap and runtime-boundary contradictions, used an overloaded state model, and did not express all approved work as testable stories. The first replacement pass also put GitHub Project creation too late, allowed early controller stories to assume unfinished controller controls, retained ambiguous generated prose, and left one oversized final-deliverables story. The corrected design is a Windows-only, ten-phase program with 129 canonical stories. macOS and software-factory work are explicitly deferred.

No workstation implementation has started. The next gate is owner review of the written specification set.

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
| VS Code, Codex CLI, Claude Code, desktop-client compatibility, optional autocomplete, and LM Studio port 1239 | P02, P05, and P10-S014 |
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

| Check | Result |
|---|---|
| Story count | 129 |
| Unique story IDs | 129 |
| Required properties and 16 sections | Pass |
| Per-phase sequence uniqueness and continuity | Pass |
| Dependency graph | Pass; 129 of 129 nodes visited with no cycle |
| Reciprocal dependency and unlock references | Pass |
| Phase-table sequence, step, and risk agreement | Pass |
| Local Markdown links | Pass after relative-depth correction |
| Ambiguous learning and contradictory research prose | Pass; zero matches |
| Placeholder and obsolete terminology scan | Pass; explanatory README history is intentional |
| Removed documentation-tree presence | Pass; no active or empty legacy folder remains locally |
| Git whitespace validation | Pass |
| Workstation implementation evidence | Not applicable — implementation has not started |

## Residual risks

- The plan is intentionally long; controller reliability and phase gates are essential.
- APIs, models, licenses, and integrations will change; freshness gates must remain blocking.
- WSL is risk reduction, not hostile-code containment. The owner still approves credentials, host access, publication, and privileged changes.
- Personal-agent and memory quality require owner acceptance, not only automated tests.
- Real-document extraction varies; the 27-document set may generate correction stories.

## Review decision

The specification set passes the second internal review but remains specifications, not authorization to build the workstation. When the owner explicitly starts P01, P01-S015 is the only story eligible for activation; its separate mutation preview and approval gate the creation of the personal GitHub Project.
