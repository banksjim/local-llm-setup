# Specification Remediation Log

**Started:** 2026-09-13

**Working branch:** `work-2026-09-14-p10-operations`

**Worktree policy for this planning phase:** Use the ordinary repository checkout; do not create a worktree.
**Status:** All three batches complete; P06 through P10 correction cycles applied; two consecutive full-program passes complete; no workstation implementation has started.

This file is the durable restart point for the specification-quality remediation. It records work state, not proof that a batch passed.

## Objective

Turn the program specifications and every story into a concrete, independently executable, independently testable plan. Remove generated boilerplate, resolve cross-document contradictions, and replace unsupported review claims with measured results.

No Git-workflow document will be added to the public repository. Repository-level Codex instructions supplied separately by the owner govern Git operations.

## Correction batches

| Batch | Scope | State |
|---|---|---|
| 1 | README, master program, story contract, controller specification, formal review, phase specifications P01-P02, and all P01-P02 stories | Complete; two consecutive clean passes |
| 2 | Phase specifications and stories P03-P05 plus the directly dependent desktop-dictation system specification | Complete; two consecutive clean passes |
| 3 | System specifications for RAG and memory; phase specifications and stories P06-P10; final cross-program review | Complete; two consecutive clean full-program passes |

The LM Studio evaluation endpoint changes from assigned user port `1239` to private/dynamic port `51239`. The port remains localhost-only and must pass an availability check at activation.

## Material findings to resolve

- 123 of 129 stories contain template-only scope and out-of-scope text.
- 89 stories contain generic evidence requirements and generic definitions of done.
- 67 stories contain generic rollback language.
- Preferred routes do not consistently declare interface, provider, model class, effort, and fallback.
- Risk rationales are commonly copied rather than derived from each story's actual blast radius.
- Implementation stories do not consistently identify reusable, idempotent operations that the final installer and maintenance suite can compose.
- The formal review and README incorrectly claim a completed passing review.
- Port `1239` is an assigned IANA user port; `51239` is in the dynamic/private range.

## Bounded review loop

Each batch receives these checks in order:

1. Contract and structural validation.
2. Story-by-story semantic review.
3. Corrections.
4. Cross-document requirements and dependency trace.
5. Current-source and contradiction review.
6. A fresh pass starting from the parent specification.

A batch may be declared complete only after two consecutive full passes find no material defect. A material defect affects scope, safety, executability, testability, traceability, factual currency, or workflow integrity. The loop stops after five correction cycles even if defects remain; at that point the remaining defects are reported to the owner and the batch is not marked complete.

## Completed read-only checks

- Repository was clean and synchronized with `origin/main` before the working branch was created.
- No project worktree was created.
- 129 story documents and ten phase documents were inventoried.
- Story IDs, phase sequence, dependency references, and local links had previously passed structural checks; those results must be rerun after correction.
- Current IANA guidance was checked on 2026-09-13: ports 49152-65535 are dynamic/private and are not assigned.

## Batch 1 correction history

Correction cycle 1 replaced template-only sections and incomplete routes across all 27 P01-P02 stories and added fixed controller/P02 artifact boundaries. Semantic review then found and corrected:

- repeated per-story approval language that conflicted with one approval per privileged phase;
- an undeclared Pester dependency in the dependency-free P01 bootstrap;
- early P01 stories requiring a controller lease before that lease exists;
- a missing dedicated non-root Linux-account creation responsibility; and
- a validation command that matched zero stories but incorrectly printed `PASS`.

The corrected Batch 1 validators asserted the then-current 129 total story files and 27 Batch 1 stories before evaluating content.

- Clean pass 1 verified the canonical contract, five-field routes, observable learning objectives, removal of targeted boilerplate, uniqueness of story-specific sections, bootstrap correctness, terminology, and all local links.
- Clean pass 2 independently verified P01/P02 phase-table-to-story agreement, the full 129-node reciprocal acyclic dependency graph, risk and human-boundary coherence, reusable-operation composition, honest review status, planning-only file scope, and Git diff health.

Batch 1 is complete under the bounded stop rule. The counts in this section are historical evidence from that batch, not the current inventory.

## Batch 2 correction history

At the start of the completed Batch 2 review, the inventory was 132 story documents. P04 grew from 11 to 14 stories when the former four-system integration/acceptance story was decomposed into separate SearXNG, document/vector, in-chat speech, automated acceptance, and owner-acceptance units. Batch 2 therefore contains 37 P03-P05 stories rather than the originally estimated 34.

Correction cycles found and addressed:

- the P04 four-system integration story was too large to execute and diagnose independently;
- Open WebUI needed a separately scoped Rancher-to-Ollama gateway rule rather than an implicit unrestricted path;
- the LM Studio guide incorrectly made live optional installation part of unconditional completion and did not name its exact `H:\ai\models\lm-studio` store;
- VS Code's built-in Ollama provider is deprecated, requiring current official provider-extension research, while local BYOK chat does not supply inline suggestions;
- Continue is read-only and no longer actively maintained, so it cannot be the preselected autocomplete default;
- 15 implementation stories lacked an exact reusable operation path;
- phase authorization language conflated research, human participation, and repeat approvals;
- human-gate automation risked validating or generating owner answers rather than only their schema and genuine presence;
- nine human-validation sections still contained irrelevant generic GUI/credential/microphone language;
- Rancher's growing `rancher-desktop-data` distribution and snapshots were left implicitly on the system drive despite the `H:\ai` storage requirement;
- the backlog headline and phase-count table disagreed after P04 decomposition;
- OpenWhispr's expanded account, sync, meeting, calendar, agent, screen-context, and remote-interface surface needed explicit dictation-only disablement and traffic tests; and
- the document/vector integration did not hard-bind indexing and query to the same accepted embedding model and dimension;
- three acceptance stories described prohibited outcomes without stating that detection must fail the automated gate;
- six story-specific human gates did not explicitly forbid the LLM from authoring the owner's observation; and
- the P05 parent source baseline covered Ollama's Claude integration but omitted Claude Code's current official configuration reference.

The corrected P04 storage design keeps named volumes in Rancher's Linux data distribution, moves that distribution and snapshots to exact `H:\ai\containers` targets only through activation-verified supported methods, requires a verified export and inventory comparison, and prohibits live PostgreSQL files in Windows bind mounts.

An attempted clean pass on 2026-09-14 asserted 132 total stories and 37 Batch 2 stories, all mandatory properties/sections, complete Batch 2 routes, reusable implementation paths, exact phase and backlog totals, the reciprocal 132-node acyclic graph, 178 local links, exact storage and obsolete-path boundaries, unique concrete core contracts, negative tests, actor alignment, and no unfinished markers. It was later invalidated when the independent architecture pass found that P04-S012 did not name its checkpoint file; the clean-pass count returned to zero.

Current-source review for the pass used primary sources checked on 2026-09-14: Ollama Windows/context/GPU and official model registry pages; current Rancher Desktop engine, Windows installation, volume, snapshot, and `rdctl` guidance; Microsoft WSL backup/move guidance; Open WebUI SearXNG, Docling, PGVector, audio, and environment references; SearXNG and Docling Serve documentation; MLflow tracing/backend guidance; VS Code language-model documentation; official Codex configuration/MCP documentation; Ollama's Claude Code integration; LM Studio server/CLI documentation; and the OpenWhispr, Handy, Whisper Local, and Continue repositories.

After the invalidated attempt, Batch 2 completed two new consecutive clean passes on 2026-09-14. Pass 1 asserted all 132 contracts, 37 Batch 2 stories, reciprocal acyclic dependencies, exact Batch 2 checkpoints, 208 local links, distinct story-specific core sections, explicit failure boundaries, architecture/storage/security requirements, obsolete-content removal, and a clean staged diff. Pass 2 independently reconstructed every P03-P05 phase row from leaf metadata, topologically ordered all 132 nodes, verified 37 concrete output and evidence contracts, four Critical-risk recovery contracts, 15 genuine human-validation gates, conditional optional tracks, parent-to-leaf requirement trace, current primary-source baselines, freshness fields, and no unfinished markers. No material defect remained in either complete pass.

The remaining P06-P10 inventory is 68 stories. A measured scan currently finds 63 stories with the old generic core scope/out-of-scope/execution/evidence/completion block and all 68 with incomplete five-field routes. Those are Batch 3 work; no full-program pass is claimed.

## Batch 3 correction history

P06 correction cycle 1 replaced the 14 incomplete routes and generic contracts with exact learning artifacts, WSL workspace paths, agent packages, operations, fixtures, tests, evidence, rollback, and checkpoint boundaries. The P06 parent now fixes the separation among Ollama, LangChain, LangGraph, MCP, skills/assets/scripts, and self-hosted MLflow; requires a dedicated PostgreSQL checkpointer database/role; constrains the first agent and MCP server to synthetic read-only capabilities; excludes secrets/private content before tracing; and keeps deterministic safety checks independent of model judges. Current primary sources were checked on 2026-09-14, including the current LangChain/LangGraph documentation, current ChatOllama integration, the official MCP Python SDK and protocol line, and current MLflow tracing/evaluation documentation. At that correction point P07-P10 and SYS-RAG/SYS-MEM remained uncorrected, so no Batch 3 clean pass was claimed.

P07 correction cycle 1 replaced 17 generic leaf contracts, added missing Langflow deployment and private knowledge-repository initialization stories, and rewrote SYS-RAG around four distinct data layers and atomic publication. The current inventory is 134 stories, with 19 in P07. P07 now requires content-addressed immutable snapshots, deterministic normalized records and Markdown, transaction-specific Git refs paired with shadow indexes, failure reconciliation, least-privilege Google OAuth, SSRF-safe one-off Crawl4AI capture, disposable authenticated-browser profiles, labeled local-vision enrichment, genuine 27-input owner acceptance, and isolated restore. Current primary sources checked on 2026-09-14 include official Docling, Crawl4AI, Google Drive, Langflow, LangChain PostgreSQL, pgvector, and MLflow documentation. P08-P10 and SYS-MEM remain uncorrected; 37 leaf stories retain incomplete routes and 32 retain measured generic core blocks, so no Batch 3 clean pass is claimed.

The P07 review loop found and corrected four material omissions after the initial rewrite: no safe Langflow deployment prerequisite, no owner for initializing the independent private knowledge repository, no paired Git/index publication protocol, and a volatile frontmatter timestamp that contradicted byte-stable reingestion. The post-correction phase-local pass asserts 19 contracts and five-field routes, 19 concrete operation/artifact paths, continuous sequence 1–19 despite stable out-of-order IDs, phase-table agreement, actor/risk controls, all required denial families, and zero targeted generic blocks. The global graph now contains 134 reciprocal acyclic nodes and all 181 parsed local Markdown links resolve. This is a checked P07 correction cycle, not a Batch 3 clean pass.

P08 correction cycle 1 rebuilt all ten inherited leaf contracts and added two missing tactical units: P08-S012 deploys the shared private LangGraph/Open WebUI runtime and P08-S011 separates the daily check-in from life planning. The parent and leaves now distinguish thread checkpointing from P09 durable memory; enforce deny-by-default tools/RAG, explicit export confirmation, provider/model/data disclosure, pre-emission trace redaction, deterministic hard safety rules, current official health/financial/crisis sources, and independent evaluation. Research checked on 2026-09-14 included current official Open WebUI Workspace/model/tool documentation, LangChain human-in-the-loop and guardrail documentation, MLflow GenAI evaluation/regression documentation, OWASP Agentic Top 10, 988/SAMHSA, CDC/HHS, CFPB, and Investor.gov. P09-P10 and SYS-MEM remain uncorrected; 27 leaf stories retain incomplete routes and 22 retain measured generic core blocks, so no Batch 3 clean pass is claimed.

The P08 internal review loop then found and corrected five defects: noncanonical Hold-reason and Actor values, an underspecified Open WebUI-to-agent protocol, accidental ambiguity about creating a second checkpoint store, no fixed private export/state root, and missing Critical controls on the private-RAG boundary. Two different phase-local passes now assert 12 complete contracts, five-field routes, distinct outputs and evidence, continuous sequence 1–12, phase-table agreement, exact safety/privacy/model requirements, Critical rehearsal/authorization/acceptance controls, a 136-node reciprocal acyclic program graph, 183 resolving local Markdown links, and a clean Git whitespace check. These are internal phase-local checks, not independent review and not a Batch 3 clean pass.

P09 correction cycle 1 rewrote SYS-MEM and all 12 inherited stories, then added P09-S013 as the missing private deployment gate. The design now makes the owner the sole durable-promotion authority; separates quarantined candidates, a framework-neutral append-only ledger, rebuildable projections, and sanitized audit; fixes the life-planning agent as the only pilot; binds decisions against replay; and defines correction, Restricted data, purge/tombstone, backup aging, and non-resurrection behavior. The current comparison must include Mem0, LangGraph Store/LangMem, Graphiti, Letta, Cognee, Hindsight, Supermemory, and new credible OSS alternatives, while separating managed claims from reproducible self-hosted behavior. At that historical checkpoint, P10 had not yet been reworked: 15 routes and 10 measured generic core blocks were still open, so no Batch 3 clean pass was claimed then.

The P09 internal review loop caught and corrected an incomplete Critical-control statement and an uncontracted `goagentic memory inbox` subcommand; the inbox now exposes a story-owned operation that `goagentic next` may recommend without changing the controller command contract. Two different internal phase-local passes assert 137 complete reciprocal acyclic story nodes, 13 P09 contracts and five-field routes, phase metadata agreement, exact Critical controls, the full framework/owner-authority/privacy/recovery/pilot trace, 184 resolving local Markdown links, current story counts, and clean Git whitespace. These are internal checks, not independent or Batch 3 review.

P10 correction cycle 1 rebuilt all 15 operational contracts and the phase parent. It fixes the P10 authorization packet, loopback/private-network release boundary, four measured RTX 4090 profiles, component/data/backup matrices, migration-aware rollback, isolated encrypted restore, fail-closed retained-data removal, composition-only installer, ten maintenance wrappers, 19 exact core guide/prompt artifacts, eight operations runbooks, nonzero catalog validation, full end-to-end matrix, independent review, and genuine owner acceptance/tagging. Current primary sources checked on 2026-09-14 included Microsoft WSL and PowerShell/PSScriptAnalyzer guidance, current Rancher Desktop installation/`rdctl`/snapshot behavior, Open WebUI migration warnings, Ollama context/concurrency/keep-alive guidance, NVIDIA NVSMI metrics, and CISA backup/recovery guidance.

The P10 review loop caught and corrected three material defects after the initial rewrite: the catalog froze the program permanently at exactly 137 stories rather than deriving the active master count; three Critical stories only implied the final owner-acceptance control; and P10-S014 claimed a named artifact count without naming its execution prompts. The corrected design uses 137 as a current minimum baseline, makes the Critical authorization/rehearsal/review/acceptance chain explicit, and names all 19 documentation/prompt artifacts.

Two consecutive full-program passes after the last material correction found no material defect. The first asserted 137 canonical contracts, exact phase inventory and continuous sequence, phase-table agreement, allowed lifecycle/risk/actor values, five-field routes, reciprocal acyclic dependencies, no standalone generic core, and clean whitespace. The second independently asserted P10's complete chain, unique core contracts, eight Critical control sets, exact installer/maintenance/documentation inventories, owner-requirement trace, 184 resolving local links, removed legacy-tree state, and clean whitespace.

## Exact resume action

1. Read this file, the root `README.md`, the master program specification, `STORY-CONTRACT.md`, the relevant phase/system specifications, and the formal review.
2. Inspect `git status` and all active repository-level Codex project instructions.
3. Work from an ordinary planning branch; do not create a worktree during specification development.
4. If this P10 branch is not yet merged, rerun the staged full-program gates and complete the personal Ship It sequence; otherwise verify clean synchronized `main` with no work branch or extra worktree.
5. Planning remediation is complete. Do not start P01 or create the GitHub Project until the owner explicitly invokes the documented program-start workflow; then only P01-S015 may be activated.
6. Do not install or configure workstation software.

## Delivery state

Batch 1 was delivered through pull request 1 and merged as `4601476fc844fc3082374e94d116bb28815f7896`. Batch 2 was delivered through pull request 2 and merged as `5f7a8dd309b34c7bc32537d2eff8064c16e9bc79`. The P06 Batch 3 correction was delivered through pull request 3 and merged as `2ba7e2c36e395265c62f87e638d21f9dc4239c79`. The P07 correction was delivered through pull request 4 and merged as `2769920cc53968509a608e0b097b1bd8a5fc8466`. The P08 correction was delivered through pull request 5 and merged as `9fb54a24279f956659de1268bbb4720789e3983c`. The P09 correction was delivered through pull request 6 and merged as `d3b257d70c7905dd3027998d97c991b95ba6232a`. The P10/final-review correction is prepared by the ordinary branch named above; its durable delivery record is the resulting Git commit and GitHub pull request. Git commits, pull requests, merge state, and branch cleanup are authoritative in Git/GitHub history.
