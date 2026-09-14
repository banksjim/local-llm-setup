# P07-S004: Define multi-knowledge-base registry and schemas

| Property | Value |
|---|---|
| Story ID | P07-S004 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P07-S003 |
| Unlocks | P07-S019 |
| Preferred route | Interface: WSL coding agent; Provider: controller-selected cloud provider; Model class: general coding; Effort: high; Fallback: second provider review and correction. |
| Research freshness | JSON Schema, YAML safety, path, and identifier guidance checked within 30 days; tool versions inherited from P07-S001. |

## 1. User story

As the owner, I want explicit registries and schemas so every later adapter writes the same validated, multi-knowledge-base structure.

## 2. Bounded objective

Implement versioned schemas under workloads/rag/schemas/ for knowledge-base configuration, source identity, immutable snapshot manifest, job state, deterministic frontmatter, chunk profile, embedding profile, index publication, and evaluation cases, plus reusable operation operations/ubuntu/p07/P07-S004-define-kb-registry-and-schemas.

## 3. Learning objective

Not applicable — P07-S002 and P07-S003 supply the owner concepts; this is an engineering contract.

## 4. Current research requirements

Confirm current JSON Schema draft/library behavior, safe YAML library behavior, Windows/WSL path rules, and selected package compatibility before pinning dependencies.

## 5. Preconditions and unlock conditions

P07-S003 is Done; phase approval covers the previewed repository-only changes; the activation packet resolves exact module and output paths. P07-S019 unlocks only after schema compatibility and negative tests pass.

## 6. In scope

Public-safe schemas, synthetic examples, migration/version rules, stable ID rules, allowed state transitions, relative-path constraints, and a read-only validation command. Define the nine-category enum and the four-layer linkage.

## 7. Out of scope and prohibited changes

No H-drive mutation, database creation, service deployment, real source content, credentials, Git remote, conversion, or indexing.

## 8. Privilege and human approval

No additional participation is required after phase authorization; only this playbook repository and synthetic fixtures change.

## 9. Risk rationale

Medium: the schema shapes later components but changes only version-controlled code and can be reverted.

## 10. Execution contract

Expose an idempotent validator that reads a KB root or fixture and emits machine-readable diagnostics. Reject unknown state transitions, absolute/private paths in Git metadata, arbitrary YAML tags, duplicate IDs, mismatched hashes, unsupported source types, unsafe repository visibility, and missing provenance.

## 11. Automated acceptance tests

Positive fixtures validate for all nine categories. Negative fixtures independently fail for duplicate document ID, invalid transition, path escape, absolute H path in Git derivative, malformed hash, unknown category, secret marker, public-remote declaration, missing layer link, and unsupported schema version. Assert at least ten negative cases execute.

## 12. Human validation

Not applicable — schema behavior is objective and receives fresh-session technical review.

## 13. Idempotency and rollback

Repeated validation is read-only and byte-stable. Schema generation produces no diff on a second run. Rollback reverts story-owned schemas, fixtures, tests, and command registration.

## 14. Required evidence

The directory evidence/P07-S004/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Exact changed-file inventory, schema/version matrix, ten-or-more negative results, nine-category positive results, second-run diff result, dependency lock diff, and reviewer findings at evidence/P07-S004/.

## 15. Definition of done

All nine categories and four data layers validate; every named rejection works; the reusable validator is documented; independent review has no material finding; and P07-S019 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S004/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause between schema files or after a green test run. Do not publish a partially updated mutually dependent schema set.
