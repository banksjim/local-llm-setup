# Formal Specification Review

**Review date:** 2026-09-13  
**Scope:** Master program, four system specifications, ten phase specifications, canonical story contract, 124 story documents, README, and navigation  
**Method:** Adversarial architecture review, requirement trace, placeholder and terminology scan, schema-shape inspection, dependency/reference validation, link validation, and Git whitespace checks  
**Result:** Pass with corrections applied; ready for owner review, not implementation

## Executive conclusion

The former plan was not safe to execute as written. It combined two operating systems and several independent systems in one document, contained bootstrap and runtime-boundary contradictions, used an overloaded state model, and did not express all approved work as testable stories. The replacement is a Windows-only, ten-phase program with 124 canonical stories. macOS and software-factory work are explicitly deferred.

No workstation implementation has started. The next gate is owner review of the written specification set.

## Findings and corrections

| ID | Severity | Problem found | Correction applied |
|---|---|---|---|
| R01 | Critical | One “kitchen sink” specification mixed controller, workstation, RAG, agents, memory, Windows, and macOS concerns. | Created one master, ten phase specs, four system specs, a story standard, and 124 story documents. |
| R02 | High | Windows and macOS were one execution program despite independent machines and timing. | Made Windows the only active program; retained macOS as a separate future program with its 175 GB constraint. |
| R03 | Critical | The controller initially depended on WSL and client tools installed later. | Defined a Windows Controller Core, P02 migration to Ubuntu, fixture adapter tests in P01, and live client tests in P05. |
| R04 | High | The command table marked `go` both invalid and executable. | Defined `go` only as the subcommand in `goagentic go`; standalone or conversational “go” is not authorization. |
| R05 | High | Workflow values mixed state, activity, and blocking causes. | Replaced them with orthogonal Status, Step, and Hold reason fields plus mappings and examples. |
| R06 | High | Risk labels were esoteric and assignment was subjective. | Adopted Low, Medium, High, and Critical; eight dimensions; highest wins; LLMs cannot lower risk. |
| R07 | High | Story sections were recommendations rather than enforceable completeness. | Made every property and 16 sections mandatory; unexplained omission and not-applicable values fail. |
| R08 | High | Cross-phase dependencies used prose rather than immutable story IDs. | Linked every phase boundary to exact preceding and following story IDs and validated all references. |
| R09 | Critical | Hardened Ubuntu could not mount `H:`, while ingestion needed `H:\ai`. | Assigned ingestion to a narrowly mounted Rancher Desktop service; WSL agents cannot browse real sources. |
| R10 | High | Langflow risked becoming a competing primary UI. | Kept Langflow as learning/design administration and required the accepted flow to be callable from Open WebUI. |
| R11 | High | The plan implied Docling could produce the final metadata format directly. | Specified lossless Docling JSON plus Markdown and a deterministic token-free YAML-frontmatter stage. |
| R12 | High | Markdown-only storage could silently lose complex table/layout data. | Made original snapshots and Docling JSON canonical private records; Markdown is the Git derivative. |
| R13 | Critical | Private documents and the public playbook boundary were underspecified. | Separated source and knowledge repositories; real data never enters this public repository; remotes must be private. |
| R14 | High | Reingestion and missing sources could cause destructive replacement or deletion. | Preserve source versions, use Git history, mark missing sources, and require approval for deletion. |
| R15 | Medium | Important visuals could be lost or invisible to retrieval. | Preserve meaningful assets, use Git LFS thresholds, and add provenance-labeled local vision enrichment. |
| R16 | High | “Speech-to-text” conflated chat audio with Windows-wide dictation. | Split chat STT from a dedicated desktop-dictation selection and implementation specification. |
| R17 | High | The full PowerShell installer and maintenance suite was not explicitly gated. | Added it to P10-S008 with analysis, dry-run, idempotency, rollback, and deliverable checks. |
| R18 | High | Sharing one Windows token into WSL would undermine isolation. | Defined one credential store per security environment: Windows once and Ubuntu once, never per repository. |
| R19 | High | Local models might be used too early or never adopted. | Added role qualification and mandatory P03 reassessment of every remaining story, with probation and cloud review. |
| R20 | Medium | Learning content could go stale or become generic courses. | Made targeted lessons blocking and required current official docs plus vetted short/deep materials at activation. |
| R21 | High | RAG acceptance inputs were ambiguous. | Defined nine categories and three owner examples each: 27 private inputs plus public synthetic fixtures. |
| R22 | Medium | Backup destination was prematurely implied. | Kept managed storage provider-neutral; OneDrive, NAS, or both are selected and tested later. |
| R23 | High | Coding-harness and software-factory work competed with real-agent learning. | Deferred both; retained only the evaluation test harness required to measure agents. |
| R24 | Low | Generated browser-workflow folders obscured durable documentation. | Removed temporary preview state and the old workflow-specific tree; retained ordinary Markdown, Mermaid, and tables. |
| R25 | Medium | The draft omitted a stable zero-context entry artifact. | Required a static `START-HERE.md` in P01-S004 that points to `goagentic` and contains no dynamic status. |

## Redundancy removed

- One authority hierarchy replaces repeated precedence descriptions.
- One command contract owns pause, resume, authorization, and next-action behavior.
- One story contract owns fields, sections, lifecycle vocabulary, and risk rules.
- System specs own cross-phase architecture; phase specs contain only gates and order.
- Obsolete specifications and temporary walkthrough plans were removed from the active tree.
- Repeated story sections remain intentionally because each story must execute independently in a fresh LLM context.

## Deliberately deferred decisions

These are controlled gates, not missing requirements:

- Exact versions and image digests: refreshed in phase research stories.
- Final models and contexts: selected by P03 measurement on the RTX 4090.
- Desktop dictation winner: selected by P05 owner benchmark.
- Open WebUI-to-Langflow mechanism: selected from current supported interfaces in P07.
- Durable memory framework: selected through current OSS evaluation and an owner-approved ADR in P09.
- OneDrive, private NAS, or dual backup: selected before P10 backup implementation.
- Knowledge-base Git remotes: absent by default and added only through a private approved action.

## Automated review results

| Check | Result |
|---|---|
| Story count | 124 |
| Unique story IDs | 124 |
| Required properties and 16 sections | Pass |
| Cross-story references | Pass |
| Local Markdown links | Pass after relative-depth correction |
| Placeholder and obsolete terminology scan | Pass; model quantization strings are not risk codes |
| Removed documentation-tree references | Pass |
| Git whitespace validation | Pass |
| Workstation implementation evidence | Not applicable — implementation has not started |

## Residual risks

- The plan is intentionally long; controller reliability and phase gates are essential.
- APIs, models, licenses, and integrations will change; freshness gates must remain blocking.
- WSL is risk reduction, not hostile-code containment. The owner still approves credentials, host access, publication, and privileged changes.
- Personal-agent and memory quality require owner acceptance, not only automated tests.
- Real-document extraction varies; the 27-document set may generate correction stories.

## Review decision

The specification set is internally consistent enough for owner review. It is not authorized for P01 implementation. After owner approval, P01-S001 is the only story eligible to become Ready.
