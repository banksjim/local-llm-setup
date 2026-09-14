# P07-S016: Run owner-provided 27-document acceptance

| Property | Value |
|---|---|
| Story ID | P07-S016 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 18 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S015 |
| Unlocks | P07-S017 |
| Preferred route | Interface: goagentic guided intake and Open WebUI; Provider: controller-selected cloud provider for orchestration with approved local models for processing; Model class: high-reliability coordinator; Effort: high; Fallback: pause, preserve accepted items, and create correction stories. |
| Research freshness | Current source permissions, API/site constraints, pinned stack health, and evaluation guidance confirmed within 7 days. |

## 1. User story

As the owner, I want three real examples from every supported category tested so I can judge fidelity and usefulness while the system proves privacy and reliability.

## 2. Bounded objective

Create evidence/P07-S016/owner-acceptance.md plus its private 27-row manifest, then ingest, index, query, and record guided outcomes for three each of PDF, DOCX, XLSX, PPTX, Markdown, website, Google Docs, Google Sheets, and Google Slides.

## 3. Learning objective

Teach the owner how to stage sources, recognize successful fidelity/citations, report a bad conversion, distinguish missing retrieval from hallucination, and safely resume a partially completed acceptance run.

## 4. Current research requirements

Revalidate every live website's authorization/capture constraints, Google export behavior, model/profile identities, and evaluation thresholds. Do not broaden access to make a fixture pass.

## 5. Preconditions and unlock conditions

P07-S015 is Done with both reviews accepted. Activation creates a 27-row private manifest with opaque IDs, category, authorization status, expected structural features, owner questions, and no content in this public repository. All private roots/backups and previous active pointer are verified.

## 6. In scope

Guided staging/URLs/OAuth; one item at a time; preservation, conversion, visual review, deterministic Markdown, indexing, known-answer and unknown-answer questions, citations, aggregate metrics, failure/correction creation, and private-repository integrity.

## 7. Out of scope and prohibited changes

No private content in cloud prompts or public traces, no unnecessary source text in local traces, no bulk Drive browsing, no unapproved remote, no automatic deletion, no substitution of synthetic data for missing owner rows, and no marking failed rows accepted. The approved local retrieval model receives only the minimum retrieved chunks needed for the current question.

## 8. Privilege and human approval

Critical private-data and credential boundary. Existing phase authorization covers the previewed roots/services. The owner chooses/stages every source, authenticates personally, confirms site rights, and judges observable fidelity; the LLM owns technical validation.

## 9. Risk rationale

Critical: real private originals and cloud authorization cross host, container, Git, database, and model boundaries.

## 10. Execution contract

Process one manifest row transactionally; show only sanitized status; ask category-specific fidelity questions; record pass/fail and reason; checkpoint; then continue. A failed row remains quarantined or on the previous accepted version and generates a linked correction story. The phase cannot claim 27/27 when any row is absent.

## 11. Automated acceptance tests

Assert manifest cardinality is 27 with exactly three per category. For every row validate immutable snapshot, normalized record, frontmatter, relative assets, Git commit linkage, active chunk linkage, citation resolution, unchanged reingest, and no-secret/private-public leakage. Aggregate retrieval/citation/latency/storage thresholds must pass; failed rows are explicitly counted and linked.

## 12. Human validation

For every row the owner answers a short category-specific checklist: identity/title, expected structure/counts, meaningful visual fidelity where relevant, one known-answer citation, one unknown-answer abstention, and overall usable/not usable. The owner is not asked to review code or architecture.

## 13. Idempotency and rollback

Resume starts at the next incomplete row. Reprocessing an unchanged row creates no duplicate snapshot, commit, or vector. Rollback restores the pre-acceptance active pointer and configuration while preserving immutable owner snapshots and row evidence.

## 14. Required evidence

The directory evidence/P07-S016/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Private 27-row manifest, exactly-three-per-category assertion, sanitized per-row outcomes, owner checklist attestations, aggregate fidelity/retrieval/citation/privacy/latency/storage metrics, leak scans, correction-story links, rerun result, rollback rehearsal, and two technical reviews at evidence/P07-S016/. Public evidence contains aggregate counts only.

## 15. Definition of done

All 27 rows have genuine owner outcomes; every accepted row passes technical lineage and privacy checks; no unresolved failed row remains without an approved correction/resolution; aggregate thresholds pass; and P07-S017 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S016/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause after any completed row. Never pause during OAuth, authenticated browsing, source copy, publication swap, or rollback; finish or compensate that atomic action first.
