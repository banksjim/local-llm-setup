# P07-S006: Implement Docling conversion and lossless archive

| Property | Value |
|---|---|
| Story ID | P07-S006 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 8 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P07-S005 |
| Unlocks | P07-S007 |
| Preferred route | Interface: WSL coding agent plus isolated Rancher workload; Provider: controller-selected cloud provider; Model class: high-reliability coding; Effort: high; Fallback: second provider review and pinned prior converter profile. |
| Research freshness | Current Docling supported-format, CLI/API, OCR, serialization, model-download, and security documentation checked within 7 days. |

## 1. User story

As the owner, I want deterministic PDF and Office conversion so structure and assets can be reproduced without rereading live sources.

## 2. Bounded objective

Implement a versioned Docling profile under workloads/rag/profiles/docling/ and reusable operation operations/windows/p07/P07-S006-docling-conversion that reads accepted snapshots and writes staged Docling JSON, Markdown draft, referenced images, and a conversion manifest for PDF, DOCX, XLSX, and PPTX.

## 3. Learning objective

Not applicable — this is the converter implementation behind the concepts learned in P07-S002.

## 4. Current research requirements

Select the current compatible Docling release at activation, record package/model digests and licenses, verify offline behavior after model acquisition, and document OCR/table/image limitations. Do not hard-code an obsolete major.

## 5. Preconditions and unlock conditions

P07-S005 is Done. Activation resolves the pinned converter image/dependencies, model cache, CPU/GPU policy, output root, limits, and synthetic corpus. Only snapshotted inputs are eligible.

## 6. In scope

Four format adapters, OCR decision rules, page/sheet/slide counts, referenced-image export, lossless JSON, normalized error codes, resource limits, restart from snapshotted state, and converter provenance.

## 7. Out of scope and prohibited changes

No frontmatter, final Git publication, web/Google adapters, LLM text cleanup, source overwrite, macros, embedded-code execution, external-resource retrieval, or active-index mutation.

## 8. Privilege and human approval

P07 authorization covers the pinned container/model download and narrow private mount. No additional human participation is needed unless a new model license or network source appears.

## 9. Risk rationale

High: private content is processed across a container and model cache; failure must not publish partial derivatives.

## 10. Execution contract

Convert into a job-specific staging directory. Record input hash, profile, Docling/package/model versions, warnings, counts, output hashes, duration, and resource use. Validate JSON and every referenced asset before atomically advancing converted. Disable network after approved dependency/model acquisition where supported.

## 11. Automated acceptance tests

For each of four formats, verify headings/tables/counts and referenced assets against golden synthetic fixtures. Inject corrupted input, OCR failure, converter crash, timeout, out-of-memory limit, missing model, missing asset, output-hash mismatch, and attempted external reference; each must quarantine or fail without final Markdown, Git commit, or active-index change. A second run must reproduce normalized outputs byte-for-byte.

## 12. Human validation

Not applicable — fixture fidelity and failure isolation are technically reviewed. Owner visual judgment occurs in P07-S016.

## 13. Idempotency and rollback

Same snapshot/profile reuses verified conversion or reproduces identical normalized outputs. Rollback removes only staged/derived converter outputs and profile deployment; immutable snapshots remain.

## 14. Required evidence

The directory evidence/P07-S006/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Pinned versions/digests/licenses, profile file, four golden comparisons, all nine failure results, offline/network observation, output hashes, second-run comparison, resource measurements, rollback rehearsal, and reviewer findings at evidence/P07-S006/.

## 15. Definition of done

Four formats yield validated lossless records and deterministic drafts; all failure cases preserve prior state; and P07-S007 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S006/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before conversion or after converted-state manifest commit. A partial staging directory is never resumed without input/profile/hash validation.
