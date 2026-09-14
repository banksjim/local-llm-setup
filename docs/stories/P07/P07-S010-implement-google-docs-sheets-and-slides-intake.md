# P07-S010: Implement Google Docs, Sheets, and Slides intake

| Property | Value |
|---|---|
| Story ID | P07-S010 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 12 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S009 |
| Unlocks | P07-S011 |
| Preferred route | Interface: WSL coding agent plus owner-visible OAuth browser; Provider: controller-selected cloud provider; Model class: high-reliability coding/security; Effort: high; Fallback: owner manual export through file intake. |
| Research freshness | Current Google Drive API v3 export, download, OAuth desktop-app, scope, quota, and token-storage documentation checked within 7 days. |

## 1. User story

As the owner, I want to provide Google Docs, Sheets, and Slides URLs and authenticate myself so all three types are preserved and converted without sharing OAuth material with an LLM.

## 2. Bounded objective

Implement the Drive adapter under workloads/rag/adapters/google-drive/ and reusable operation operations/windows/p07/P07-S010-google-workspace-intake for URL parsing, read-only OAuth, Drive metadata/download-capability lookup, type-specific export, immutable export snapshots, revocation, and deterministic handoff.

## 3. Learning objective

The guided step explains requested scope, browser consent, where the token lives, how to revoke it, and why Google-native files are preserved as metadata plus exports rather than a nonexistent native binary.

## 4. Current research requirements

Confirm exact current read-only scope, desktop OAuth flow, token refresh/revocation, canDownload field, export MIME types, size limits, revision metadata availability, and error/quota behavior. Compare Docs Markdown and DOCX fidelity on qualification fixtures.

## 5. Preconditions and unlock conditions

P07-S009 is Done. Activation names the OAuth client method, approved secret store, redirect URI, Drive scope, three synthetic/test-owned Google files, export profiles, and token removal operation. Owner consent is performed only after the preview.

## 6. In scope

Recognized URL forms; stable file ID; MIME/type validation; metadata; canDownload; Docs Markdown-versus-DOCX qualification; Sheets XLSX; Slides PPTX and optional reference PDF; export hashes; read-only token lifecycle; retry/backoff; changed/missing access behavior.

## 7. Out of scope and prohibited changes

No edit/delete/share permissions, broad Drive enumeration, service accounts, credential files in Git or WSL-agent context, CSV as canonical Sheets export, automatic permission changes, or processing arbitrary unsupported Drive items.

## 8. Privilege and human approval

Critical credential boundary. The owner reviews Google's consent screen and authenticates interactively. The LLM may guide and inspect sanitized status only; it never receives client secrets, authorization codes, refresh tokens, cookies, or raw private content.

## 9. Risk rationale

Critical: OAuth creates transferable access to private cloud documents; scope or token leakage crosses an external access-control boundary.

## 10. Execution contract

Parse URL locally, request only the resolved read-only scope, verify file identity/type/canDownload, export to staging, hash, atomically store metadata plus bytes as one snapshot, hand off by snapshot ID, and redact all logs. Revoked access or changed permissions fail closed and preserve the last accepted version.

## 11. Automated acceptance tests

API mocks cover three URL types, all required metadata, multi-sheet XLSX, multi-slide PPTX, Docs export comparison, changed modified time, unchanged export, quota retry, and token refresh. Denials cover malformed URL, wrong MIME, canDownload false, revoked token, excess scope, token/log leak, unsupported item, first-sheet-only CSV attempt, partial export, hash mismatch, and API outage; no active state changes on failure.

## 12. Human validation

The owner authenticates once to test-owned or selected files, confirms the consent scope is read-only, inspects sanitized names/counts for one of each type, and completes the revocation check. The LLM owns implementation review.

## 13. Idempotency and rollback

Same file/export/profile hash creates no new version. Rollback disables the adapter, revokes/removes tokens, and removes staged test exports; accepted immutable snapshots remain pending explicit deletion.

## 14. Required evidence

The directory evidence/P07-S010/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Primary-source scope/export record, OAuth storage boundary, mock test inventory, at least eleven denial results, three-type live sanitized result, all-sheet/all-slide counts, token leak scan, revocation proof, second-run result, rollback, and security review at evidence/P07-S010/.

## 15. Definition of done

All three Google categories export and hand off correctly; credential boundaries and denials pass; owner consent/revocation evidence is genuine; and P07-S011 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S010/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before OAuth or after tokens are secured and no interactive browser remains. Never pause with authorization codes, temporary exports, or consent prompts exposed.
