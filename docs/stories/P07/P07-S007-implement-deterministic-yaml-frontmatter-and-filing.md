# P07-S007: Implement deterministic YAML frontmatter and filing

| Property | Value |
|---|---|
| Story ID | P07-S007 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P07-S006 |
| Unlocks | P07-S008 |
| Preferred route | Interface: WSL coding agent; Provider: controller-selected cloud provider; Model class: general coding; Effort: high; Fallback: fresh-session second-provider review. |
| Research freshness | Current safe YAML serializer, JSON Schema, Unicode, newline, and Git path behavior checked within 30 days. |

## 1. User story

As the owner, I want deterministic frontmatter and filing so normalized documents are readable, versionable, and safe to query across multiple knowledge bases.

## 2. Bounded objective

Implement deterministic rendering under workloads/rag/derivative/ and reusable operation operations/ubuntu/p07/P07-S007-render-frontmatter-and-file that transforms validated conversion records into stable Markdown and asset paths governed by the P07-S004 schemas.

## 3. Learning objective

Not applicable — deterministic metadata was covered conceptually in P07-S002.

## 4. Current research requirements

Confirm serializer safe-mode behavior, ambiguous scalar quoting, UTC formatting, UTF-8/LF normalization, Windows-reserved names, Unicode normalization, and Git case-collision behavior.

## 5. Preconditions and unlock conditions

P07-S006 is Done. Activation resolves the repository root, content taxonomy, path-length policy, serializer version, and synthetic fixtures. The repository must have no remote.

## 6. In scope

Fixed frontmatter schema, stable ordering, safe scalars, managed relative paths, deterministic filenames/assets, classification/tags supplied by rules or approved config, Markdown normalization, secret/path scan, and staged derivative validation.

## 7. Out of scope and prohibited changes

No LLM-authored metadata, invented titles/tags, live Git commit, indexing, source mutation, absolute paths, credentials, arbitrary YAML objects/tags, or private fixture content in the public repo.

## 8. Privilege and human approval

Phase authorization is sufficient. The story writes only derived files in the approved private repository and public-safe code/tests in this repository.

## 9. Risk rationale

Medium: derived data can be regenerated and changes are version controlled, but malformed metadata would affect downstream retrieval.

## 10. Execution contract

Render from validated manifests only. Separate volatile ingestion timestamps into private manifests so identical source/profile inputs produce byte-identical derivatives. Stage files, validate schema/references/hashes/secret rules, then mark validated; do not commit yet.

## 11. Automated acceptance tests

Positive fixtures cover all required fields and four converted file types plus native Markdown. Negative tests reject arbitrary YAML tags, duplicate keys, ambiguous unquoted scalars, invalid UTC time, path traversal, reserved names, case collisions, missing assets, absolute paths, tokens/cookies/signed URLs, and unknown schema. Two clean renders must be byte-identical.

## 12. Human validation

Not applicable — schema and byte comparisons are objective; owner fidelity review occurs later.

## 13. Idempotency and rollback

Repeated render produces identical bytes and no Git diff. Rollback removes story-owned staged derivatives; converter records and originals remain.

## 14. Required evidence

The directory evidence/P07-S007/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Schema version, rendered synthetic tree, positive inventory, at least eleven named negative results, byte hashes from two runs, secret/path scan, Git diff result, rollback rehearsal, and reviewer findings at evidence/P07-S007/.

## 15. Definition of done

Five local source categories render deterministically; every unsafe case is rejected; no volatile/private value leaks; and P07-S008 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S007/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before staging replacement or after the complete derivative validates. Never pause with a partially replaced document tree.
