# P07-S011: Implement visual asset preservation and enrichment

| Property | Value |
|---|---|
| Story ID | P07-S011 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 13 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P07-S010 |
| Unlocks | P07-S012 |
| Preferred route | Interface: WSL coding agent plus local Ollama vision endpoint; Provider: controller-selected cloud provider for code and approved local model for enrichment; Model class: high-reliability coding/local vision; Effort: high; Fallback: preserve assets without generated descriptions. |
| Research freshness | Current Docling image export, selected vision-model card/license, Ollama vision support, Git/LFS, and accessibility guidance checked within 7 days. |

## 1. User story

As the owner, I want meaningful figures and charts preserved and optionally described so visual knowledge remains searchable without presenting generated descriptions as source truth.

## 2. Bounded objective

Implement the asset module under workloads/rag/assets/ and reusable operation operations/windows/p07/P07-S011-visual-assets for deterministic naming, meaningful/decorative classification, Markdown references, optional local-vision descriptions with provenance, and measured large-file handling.

## 3. Learning objective

Not applicable — the owner evaluates visual fidelity in P07-S016; this story is engineering implementation.

## 4. Current research requirements

Verify current converter image metadata, selected vision model inputs/context/license, local-only endpoint, reproducibility settings, Git object growth, and Git LFS restore implications before setting thresholds.

## 5. Preconditions and unlock conditions

P07-S010 is Done. Activation resolves the local vision model digest, prompt profile, deterministic classification rules, asset-size threshold, LFS decision, and fixtures containing meaningful and decorative images.

## 6. In scope

Hash-based asset paths, deduplication, source references, deterministic size/type/placement heuristics, review override, generated-description labeling/provenance, local inference, timeout/failure behavior, and asset integrity validation.

## 7. Out of scope and prohibited changes

No cloud vision API, replacement of OCR/tables/alt text, deletion of source assets, unlabeled generated claims, inferred numeric chart values presented as fact, automatic LFS use without restore proof, or failure of vision enrichment blocking text ingestion.

## 8. Privilege and human approval

P07 authorization covers local model use and derived private assets. A new model license or remote endpoint requires a new preview.

## 9. Risk rationale

High: private images enter a model pipeline and Git asset choices can materially affect storage and retrieval, though originals remain preserved.

## 10. Execution contract

Extract and hash first; classify with deterministic rules; preserve every meaningful asset; call only the approved localhost model for optional enrichment; attach generated status, model digest, prompt-profile hash, timestamp, source hash, confidence/limitations; validate references before publication.

## 11. Automated acceptance tests

Fixtures prove chart, diagram, screenshot, slide image, duplicate asset, and decorative logo behavior. Failures cover model unavailable, timeout, malformed response, hallucinated-number guard, source-hash mismatch, broken reference, unsupported image, oversized asset, LFS missing object when enabled, and private outbound call. Text remains publishable when enrichment fails.

## 12. Human validation

The owner reviews a guided sample containing one chart, diagram, and decorative image and rates preservation and description usefulness; no code judgment is requested.

## 13. Idempotency and rollback

Same source/model/prompt profile produces stable asset paths; nondeterministic prose differences create a new labeled enrichment version without changing source assets. Rollback removes generated descriptions and story deployment, not originals.

## 14. Required evidence

The directory evidence/P07-S011/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Model/license/digest, prompt hash, asset-rule version, fixture matrix, ten failure results, outbound-network assertion, Git/LFS measurement and restore check if applicable, owner ratings, rerun result, rollback, and review at evidence/P07-S011/.

## 15. Definition of done

Meaningful assets remain linked and verifiable; generated text is unmistakably labeled; enrichment failure is nonblocking; storage handling is restore-tested; and P07-S012 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S011/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before model invocation or after a complete asset/enrichment manifest is committed to staging. Cancelled calls cannot leave a description marked accepted.
