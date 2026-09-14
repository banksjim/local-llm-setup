# P07-S001: Refresh RAG and ingestion tool guidance

| Property | Value |
|---|---|
| Story ID | P07-S001 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P06-S014 |
| Unlocks | P07-S002 |
| Preferred route | Interface: web-capable coding agent; Provider: controller-selected cloud provider; Model class: economical research; Effort: medium; Fallback: second cloud provider if a primary-source conflict remains. |
| Research freshness | Official documentation, repositories, releases, licenses, and security notices checked within 7 days of activation. |

## 1. User story

As the owner, I want a dated technology decision record so implementation uses current tools and known limitations rather than training-memory assumptions.

## 2. Bounded objective

Create docs/research/p07/P07-S001-rag-tool-baseline.md and evidence/P07-S001/activation-data.json covering Docling, Crawl4AI, Google Drive export/OAuth, Langflow, LangChain PostgreSQL integration, pgvector, local embedding candidates, and MLflow tracing/evaluation.

## 3. Learning objective

Not applicable — this produces the evidence used to construct the next two owner learning modules.

## 4. Current research requirements

Use primary sources. Record access date, stable URL, current stable version or immutable release/tag, license, supported role, material limitations, security advisories, conflicts, and whether each conclusion is fact or inference. Revalidate the P03-selected embedding profile; compare replacements only if it is unavailable, incompatible, materially stale, or fails the P07 corpus qualification—never by leaderboard alone.

## 5. Preconditions and unlock conditions

P06-S014 is Done; the repository is clean; the controller validates the authority chain and creates the activation packet. Completion unlocks P07-S002 only after link and inventory checks pass.

## 6. In scope

Research and decisions for the exact P07 stack, including the current Docling major, Crawl4AI safe deployment mode, Google export formats/scopes, Langflow invocation boundary, Python PostgreSQL adapter, pgvector index options, embedding candidates, and evaluation metrics.

## 7. Out of scope and prohibited changes

No installation, credential request, external account mutation, model download, service start, private-source access, or replacement of the approved SYS-RAG architecture.

## 8. Privilege and human approval

Phase authorization is sufficient; this story performs read-only public research. The owner is not asked to technically review it.

## 9. Risk rationale

Low: public read-only research and repository documentation only. A conflict that could alter architecture creates a design-change finding and stops unlock.

## 10. Execution contract

The research record ends with a decision table containing component, selected role, current candidate, version resolution, license, primary sources, rejected alternatives, known failure modes, and stories affected. The activation-data file is machine-readable and contains no credentials.

## 11. Automated acceptance tests

Assert eight component rows exist; every row has a source accessed within seven days; all URLs resolve; every versioned selection has a release/tag or runtime-resolution rule; every license is identified; no TBD, bare “latest,” or unsupported benchmark claim remains; and repository secret/link/schema checks pass.

## 12. Human validation

Not applicable — an independent qualified LLM reviews evidence against primary sources; the owner supplies preferences only if research exposes a material choice.

## 13. Idempotency and rollback

Rerun replaces the dated record only when evidence changed and otherwise produces no diff. Rollback reverts the two story-owned files.

## 14. Required evidence

The directory evidence/P07-S001/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Sanitized source table, version/license table, search dates, conflict resolutions, rejected alternatives, acceptance output, changed-file list, and reviewer findings at evidence/P07-S001/.

## 15. Definition of done

All eight technology areas have current, primary-source-backed decisions; automated checks pass; independent review has no unresolved material finding; and the controller records P07-S002 as Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S001/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause after each component row or before committing the final decision table. Partial research leaves the story Waiting with Hold reason Paused and cannot unlock P07-S002.
