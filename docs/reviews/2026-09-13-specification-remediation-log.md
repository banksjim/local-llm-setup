# Specification Remediation Log

**Started:** 2026-09-13

**Working branch:** `work-2026-09-13`

**Worktree policy for this planning phase:** Use the ordinary repository checkout; do not create a worktree.
**Status:** Batch 1 in progress; no workstation implementation has started.

This file is the durable restart point for the specification-quality remediation. It records work state, not proof that a batch passed.

## Objective

Turn the program specifications and every story into a concrete, independently executable, independently testable plan. Remove generated boilerplate, resolve cross-document contradictions, and replace unsupported review claims with measured results.

No Git-workflow document will be added to the public repository. Repository-level Codex instructions supplied separately by the owner govern Git operations.

## Correction batches

| Batch | Scope | State |
|---|---|---|
| 1 | README, master program, story contract, controller specification, formal review, phase specifications P01-P02, and all P01-P02 stories | Complete; two consecutive clean passes |
| 2 | Phase specifications and stories P03-P05 | Next |
| 3 | System specifications for dictation, RAG, and memory; phase specifications and stories P06-P10; final cross-program review | Not started |

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

The corrected validators assert 129 total story files and 27 Batch 1 stories before evaluating content.

- Clean pass 1 verified the canonical contract, five-field routes, observable learning objectives, removal of targeted boilerplate, uniqueness of story-specific sections, bootstrap correctness, terminology, and all local links.
- Clean pass 2 independently verified P01/P02 phase-table-to-story agreement, the full 129-node reciprocal acyclic dependency graph, risk and human-boundary coherence, reusable-operation composition, honest review status, planning-only file scope, and Git diff health.

Batch 1 is complete under the bounded stop rule. This is not a full-program pass: P03-P10 still contain 97 known generic scope/evidence records and 102 routes that do not yet satisfy the five-field contract.

## Exact resume action

1. Read this file, the root `README.md`, the master program specification, `STORY-CONTRACT.md`, the relevant phase/system specifications, and the formal review.
2. Inspect `git status` and all active repository-level Codex project instructions.
3. Begin Batch 2 on the next ordinary working branch after Batch 1 is merged: remediate P03-P05 and their 34 stories using the same specificity and bounded-loop standard.
4. Recheck current official sources for model, Ollama, Rancher Desktop, Open WebUI, supporting services, dictation, VS Code, client integrations, and LM Studio claims that affect the specifications.
5. Keep the formal review `Remediation in progress`; do not claim a full-program pass until Batch 3 and the final two-pass review complete.
6. Do not install or configure workstation software.

## Delivery state

Batch 1 content and its two clean passes are ready for the owner's Ship It sequence. Git commits, pull requests, merge state, and branch cleanup are authoritative in Git/GitHub history rather than manually updated in this log after delivery.
