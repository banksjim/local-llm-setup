# Specification Remediation Log

**Started:** 2026-09-13

**Working branch:** `work-2026-09-13-b`

**Worktree policy for this planning phase:** Use the ordinary repository checkout; do not create a worktree.
**Status:** Batches 1 and 2 complete; Batch 3 not started; no workstation implementation has started.

This file is the durable restart point for the specification-quality remediation. It records work state, not proof that a batch passed.

## Objective

Turn the program specifications and every story into a concrete, independently executable, independently testable plan. Remove generated boilerplate, resolve cross-document contradictions, and replace unsupported review claims with measured results.

No Git-workflow document will be added to the public repository. Repository-level Codex instructions supplied separately by the owner govern Git operations.

## Correction batches

| Batch | Scope | State |
|---|---|---|
| 1 | README, master program, story contract, controller specification, formal review, phase specifications P01-P02, and all P01-P02 stories | Complete; two consecutive clean passes |
| 2 | Phase specifications and stories P03-P05 plus the directly dependent desktop-dictation system specification | Complete; two consecutive clean passes |
| 3 | System specifications for RAG and memory; phase specifications and stories P06-P10; final cross-program review | Not started |

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

The current inventory is 132 story documents. P04 grew from 11 to 14 stories when the former four-system integration/acceptance story was decomposed into separate SearXNG, document/vector, in-chat speech, automated acceptance, and owner-acceptance units. Batch 2 therefore contains 37 P03-P05 stories rather than the originally estimated 34.

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

## Exact resume action

1. Read this file, the root `README.md`, the master program specification, `STORY-CONTRACT.md`, the relevant phase/system specifications, and the formal review.
2. Inspect `git status` and all active repository-level Codex project instructions.
3. After Batch 2 is merged and synchronized, create an ordinary planning branch for Batch 3; do not create a worktree during specification development.
4. Remediate the RAG and memory system specifications, P06-P10 phase specifications, and all 68 remaining stories. Replace the measured 63 generic core blocks and complete all 68 five-field routes, then run the final two-pass cross-program review.
5. Keep the formal review `Remediation in progress`; do not claim a full-program pass until Batch 3 and the final two-pass review complete.
6. Do not install or configure workstation software.

## Delivery state

Batch 1 was delivered through pull request 1 and merged as `4601476fc844fc3082374e94d116bb28815f7896`. Batch 2 is validated and ready for the owner's full Ship It sequence on the ordinary branch named above. Git commits, pull requests, merge state, and branch cleanup are authoritative in Git/GitHub history.
