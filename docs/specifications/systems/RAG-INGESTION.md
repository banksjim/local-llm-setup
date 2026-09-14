# RAG and Ingestion System Specification

**System ID:** `SYS-RAG`  
**Status:** Approved design; unimplemented  
**Primary phase:** P07  
**Last reviewed:** 2026-09-14

## 1. Purpose and non-goals

The system creates reproducible, private knowledge bases from heterogeneous sources without paying an LLM to perform routine scraping, conversion, metadata generation, filing, hashing, or validation. LLM use is limited to explicitly labeled visual enrichment and retrieval answers.

The first release is not a general web crawler, enterprise records system, public service, agent memory store, or substitute for the original source application. Open WebUI remains the normal conversational interface; Langflow is a local visual learning and flow-administration surface.

## 2. Supported sources

The acceptance contract contains exactly nine categories: PDF, DOCX, XLSX, PPTX, Markdown, public or explicitly authorized website URLs, Google Docs URLs, Google Sheets URLs, and Google Slides URLs. Legacy or macro-enabled Office files, archives, executable attachments, email stores, and arbitrary cloud drives are rejected in the first release.

## 3. Four-layer data model

Every accepted document has four distinct layers:

1. **Immutable source snapshot** — the supplied file, fetched HTML/MHTML plus response metadata, or Google export plus Drive metadata; content-addressed and never overwritten.
2. **Lossless normalized record** — converter JSON and referenced assets sufficient to reproduce the Git derivative without rereading the live source.
3. **Versioned Git derivative** — deterministic Markdown with YAML frontmatter and meaningful assets in a private, local knowledge repository.
4. **Active retrieval index** — rebuildable chunks and embeddings in a versioned PostgreSQL/PGVector collection.

The source snapshot and normalized record are authoritative preservation artifacts. Markdown is the readable, reviewable derivative. The vector index is disposable and may always be rebuilt.

## 4. Storage and trust boundaries

Each knowledge base has a stable ID and independent configuration.

| Data | Windows location | Git status |
|---|---|---|
| Originals, exports, manifests, converter JSON, quarantine | `H:\ai\knowledge-sources\<kb-id>` | Never in Git |
| Markdown, meaningful assets, schemas, tests, flow exports | `H:\ai\knowledge-repos\<kb-id>` | Independent private local Git repository |
| Vector data | Dedicated P04 PostgreSQL database/schema/role | Never in Git; logical backup only |
| Playbook code and synthetic fixtures | This public repository | Public-safe only |

The knowledge repository has no remote by default. Adding one is a human-approved operation and only a private personal repository or private business-organization repository is permitted. Pre-commit validation rejects credentials, cookies, signed URLs, absolute local paths, original-file paths, and known private fixture markers.

The ingestion coordinator is a dedicated Rancher Desktop workload with read/write mounts limited to the selected knowledge-source and knowledge-repository roots. It receives a dedicated least-privilege database identity. Hardened WSL agents may develop and test with synthetic Linux fixtures but cannot browse real `H:\ai\knowledge-sources` content. Deployment crosses the controller's reviewed privileged path.

## 5. Job state machine and atomic publication

Each document/version receives a durable job manifest and advances only through:

```text
received -> snapshotted -> converted -> validated -> git-committed -> indexed-staged -> active
```

`quarantined`, `failed`, and `rolled-back` are terminal outcomes for that attempt. State changes use atomic manifest replacement and record timestamps, tool versions, hashes, inputs, outputs, and error codes. Restart resumes from the last verified state rather than rerunning completed destructive work.

Publication uses a staging directory, a transaction-specific Git ref, and a shadow vector collection. The accepted Git branch and active-index pointer change only after derivative validation, a successful candidate commit, index count/dimension checks, and retrieval smoke tests. A durable reconciliation journal records both changes. If either final pointer update fails, reconciliation completes the pair or restores both accepted pointers to their prior values; the candidate commit and shadow index remain inactive for diagnosis, and the old active index is never deleted during the transaction.

## 6. Intake safety

Files are treated as untrusted data. Intake copies to a story-owned staging area, rejects unsupported extensions and type/signature mismatches, enforces configured byte/page/sheet/slide/time/decompression limits, never executes macros or embedded code, never follows Office external links, hashes the staged bytes, atomically moves them to a content-addressed snapshot, then rehashes. An interrupted copy cannot become `snapshotted`.

Duplicate content hashes reuse the existing snapshot. Stable document IDs identify logical sources; version IDs identify immutable content. No ordinary command deletes originals. Any original or derivative deletion is a separate Critical operation with an exact preview and owner confirmation.

For Google-native files there is no downloadable native binary. The immutable snapshot therefore consists of Drive metadata (file ID, name, MIME type, modified time, revision/version identifiers when available, permissions relevant to download, export MIME, retrieval time) plus the chosen export bytes and hashes. The adapter checks `capabilities.canDownload`, uses read-only scope selected from current Google guidance, and stores OAuth tokens only in the approved host secret store outside Git and logs.

## 7. Conversion and deterministic derivative

Current compatible releases are selected in P07-S001; the design does not hard-code a stale major version. Docling provides structured JSON, Markdown, OCR when required, and referenced images for Office/PDF inputs. Crawl4AI provides browser-rendered HTML, raw/cleaned HTML, Markdown, links, and media for one-off web inputs using its deterministic, non-LLM path. Raw captured web content and response metadata are preserved when permitted.

The YAML layer is separate from Docling. A safe serializer with a fixed JSON Schema uses UTF-8, LF endings, stable key ordering, UTC ISO-8601 timestamps, quoted ambiguous scalars, and no arbitrary YAML tags. Machine paths are recorded only as managed relative paths. Required fields include schema version, document ID, version ID, knowledge-base ID, title, source category, nonsecret source locator, source identity/modified time when applicable, first-accepted version time, source and derivative hashes, converter and extraction profile versions, language, structural counts, classification, collection, tags, status, and provenance references.

Unchanged source bytes plus the same profiles must produce byte-identical JSON-normalized Markdown and stable asset names. The first-accepted time is immutable for that document version; retry and observation times belong in the private job manifest, not the Markdown derivative.

## 8. Source-specific behavior

### Web

Crawl4AI is used for owner-directed one-off capture, not systematic crawling. The default path uses fresh retrieval, bounded timeouts, an allowlisted HTTP(S) URL, deterministic Markdown generation, and CSS/XPath extraction where needed—without an LLM. The snapshot records requested/final URL, retrieval time, status, response metadata allowed by policy, content hash, selected elements, raw HTML or MHTML, and capture profile.

Authenticated capture is Critical and case-by-case. The owner confirms authorization and authenticates interactively into a disposable isolated browser profile. Credentials, cookies, headers, and session storage never enter a prompt, log, manifest, Git repository, or reusable default profile. The implementation does not bypass CAPTCHAs, paywalls, robots controls, access restrictions, or contractual prohibitions. A local mock proves automation; a live private site is never required merely to make the software test pass.

### Google Workspace

The owner supplies a URL. The adapter resolves the Drive file ID, validates type and download capability, and exports:

- Docs: compare current Markdown and DOCX export paths on qualification fixtures; record and use the selected fidelity profile.
- Sheets: XLSX to preserve all sheets; CSV/TSV is never canonical because Drive exports only the first sheet.
- Slides: PPTX as canonical structured export; PDF may be captured as a secondary visual reference.

Every export stores metadata and bytes as one immutable snapshot. Revoked access fails closed without altering accepted content.

## 9. Visual content

Meaningful charts, diagrams, screenshots, and slide images are preserved under deterministic `assets/` paths and referenced from Markdown. Decorative assets are omitted by a versioned deterministic rule set with a review override. Large-file handling is selected and tested during activation; if Git LFS is used, backup and restore must include LFS objects and a compatible private remote before any push.

A local vision model may add searchable descriptions only after deterministic extraction. Each description is marked as generated and records model, digest/version, prompt profile, timestamp, and source-asset hash. It cannot replace OCR, extracted labels, tables, alt text, or source truth. Failure leaves the asset available without a generated description.

## 10. Version, deletion, and failure behavior

Changed content creates a new immutable snapshot and updates the stable Markdown path in a new Git commit. Missing sources become `missing` but remain searchable with their last accepted version. Deletion is never inferred from absence and requires a Critical deletion preview naming every snapshot, derivative, Git revision effect, and index row.

Failed or quarantined attempts cannot publish Markdown, change the active pointer, or delete a previous version. Repair commands operate only on story-owned staging artifacts. Original snapshots are append-only in normal operation.

## 11. Chunking, indexing, and retrieval

Chunk profiles are content-aware, versioned, and independent of conversion profiles. Chunk IDs derive from knowledge-base ID, document ID, accepted version, chunk profile, and stable ordinal/hash. The embedding profile records model identity/digest, dimension, normalization, distance metric, and query prefix behavior. Ingest and query must use the same profile; a mismatch hard-fails before a database write.

Index builds write to a named shadow collection. Tests compare approximate retrieval with exact search, measure recall, and select HNSW/IVFFlat/no-index parameters for the measured corpus rather than assuming them. A model or dimension change creates a named reindex and preserves the previous collection until acceptance.

Retrieval returns stable document/version/chunk IDs and citations resolvable to the Markdown derivative. Evaluation has a versioned tuning set and untouched holdout set. Deterministic source coverage, retrieval recall/precision, citation resolution, unsupported-claim checks, latency, and storage growth are primary. A model judge may supplement but can never be the sole acceptance signal.

## 12. Langflow and Open WebUI boundary

The accepted Langflow flow is exported as versioned JSON with credentials externalized. Langflow binds only to the approved localhost/private container network. At story activation, the current stable flow-run API and current Open WebUI extension/tool mechanism are verified; the selected adapter invokes the accepted flow and returns answer text plus structured citations. Open WebUI's P04 built-in document feature is only a small baseline, not the authoritative pipeline.

## 13. Observability and privacy

MLflow traces record stage timings, counts, hashes/identifiers safe for logs, retrieval decisions, model/profile identities, errors, and evaluation results. A pre-emission redaction layer blocks source text, private URLs, OAuth material, filesystem paths, and document content by default. Synthetic traces prove observability; private acceptance evidence contains only aggregate counts, hashes where safe, pass/fail outcomes, and owner checklist results.

## 14. Backup and recovery

The recoverable unit contains immutable snapshots, normalized records, manifests, knowledge Git objects and any LFS objects, flow/config/profile exports, database schema plus logical dump, and the documented secret-recreation procedure (never raw secrets in the archive). P07 proves an isolated local recovery copy; P10 chooses and operates the durable OneDrive, private NAS, or combined destination.

## 15. Acceptance invariants

- Three owner inputs in each of nine categories have reviewed outcomes.
- No original, credential, private fixture, or absolute private path enters the public playbook or any unapproved remote.
- Unchanged reingestion is byte-stable and creates neither duplicate commits nor duplicate vectors.
- Interrupted copies, converter crashes, malformed YAML, dimension mismatch, indexing failure, revoked OAuth, and retrieval failure leave the previous accepted version active.
- Every active chunk resolves to one accepted Markdown version and one immutable source snapshot.
- The holdout set meets activation-packet thresholds for retrieval, citations, unsupported claims, latency, and storage.
- An isolated restore reproduces manifests, Git integrity, active row counts, and known-answer retrieval.

## 16. Current primary references

- [Docling supported formats](https://docling-project.github.io/docling/usage/supported_formats/)
- [Docling CLI and referenced-image export](https://docling-project.github.io/docling/reference/cli/)
- [Docling serialization](https://docling-project.github.io/docling/concepts/serialization/)
- [Crawl4AI browser and crawler configuration](https://docs.crawl4ai.com/core/browser-crawler-config/)
- [Crawl4AI self-hosting security notes](https://docs.crawl4ai.com/core/self-hosting/)
- [Google Workspace export formats](https://developers.google.com/workspace/drive/api/guides/ref-export-formats)
- [Google Drive download/export guidance](https://developers.google.com/workspace/drive/api/guides/manage-downloads)
- [Langflow flow trigger API](https://docs.langflow.org/api-flows-run)
- [LangChain PGVector integration](https://docs.langchain.com/oss/python/integrations/vectorstores/pgvector)
- [pgvector project and index guidance](https://github.com/pgvector/pgvector)
- [MLflow tracing](https://mlflow.org/docs/latest/genai/tracing)
