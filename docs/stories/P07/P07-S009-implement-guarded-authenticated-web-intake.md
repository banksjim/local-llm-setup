# P07-S009: Implement guarded authenticated web intake

| Property | Value |
|---|---|
| Story ID | P07-S009 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P07-S008 |
| Unlocks | P07-S010 |
| Preferred route | Interface: owner-visible browser plus WSL coding agent; Provider: controller-selected cloud provider; Model class: high-reliability coding/security; Effort: high; Fallback: documented unsupported result and manual export intake. |
| Research freshness | Current Crawl4AI authentication/session docs, site authorization constraints, and browser credential-isolation guidance checked within 7 days. |

## 1. User story

As the owner, I want an explicitly guarded authenticated capture path so an authorized private page can be ingested without giving credentials or reusable sessions to an LLM.

## 2. Bounded objective

Implement an opt-in profile under workloads/rag/adapters/web/authenticated/ and reusable operation operations/windows/p07/P07-S009-authenticated-web-intake using an owner-operated disposable browser context and the same bounded one-page capture pipeline, with a manual-export fallback.

## 3. Learning objective

The guided checklist teaches what the session can access, where credentials stay, how to revoke it, and when to choose manual export.

## 4. Current research requirements

Verify the current supported browser-session mechanism and declarative hook security. For any live target, record owner authorization, applicable site terms/robots constraints, and a target-specific allowed URL boundary before execution.

## 5. Preconditions and unlock conditions

P07-S008 is Done. The generic implementation uses only a local mock. A live use requires a separate target packet naming one authorized origin, capture purpose, data classification, session lifetime, output destination, and fallback.

## 6. In scope

Disposable isolated browser profile, interactive owner login, origin allowlist, cookie/session lifetime, one-page capture, automatic profile destruction/revocation steps, redacted logs, and manual export through P07-S005 when automation is unsafe.

## 7. Out of scope and prohibited changes

No password/token input to prompts or scripts; no saved default profile; no cross-origin navigation; no CAPTCHA, MFA, paywall, anti-bot, access-control, or robots bypass; no bulk crawl; no credential logging; no claim that every site is supported.

## 8. Privilege and human approval

Critical access boundary. P07 phase authorization covers the mock and framework only. The owner must separately confirm authorization for each live origin and personally authenticate; the LLM never sees or stores the credential.

## 9. Risk rationale

Critical: a browser session can expose private content and transferable authentication material.

## 10. Execution contract

Start a clean profile with no private mounts, display the exact origin and capture preview, let the owner authenticate, capture only after origin validation, redact before logging, close all pages, destroy the profile, and verify revocation/destruction. If any session artifact cannot be isolated, stop and instruct manual export.

## 11. Automated acceptance tests

A local authenticated mock proves login handoff, allowed capture, session expiry, profile destruction, and redaction. Deny wrong origin, redirect off-origin, missing authorization record, credential in input, cookie/header in logs, reused profile, expired session, CAPTCHA marker, denied robots policy, private-network target, and profile-destruction failure. No live credential is required for tests.

## 12. Human validation

The owner performs mock login and verifies the profile is visibly separate and unusable after completion. Live acceptance is optional per target; lack of a live private site does not block the safe framework.

## 13. Idempotency and rollback

Each attempt uses a new profile and request ID. Repeating never reuses credentials. Rollback disables authenticated mode and destroys story-created profiles; accepted snapshots remain append-only.

## 14. Required evidence

The directory evidence/P07-S009/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Authorization schema, mock target/config, eleven denial results, redaction scan, profile lifecycle proof, manual-export fallback, owner mock result, rollback rehearsal, and cross-provider security review at evidence/P07-S009/.

## 15. Definition of done

The mock path passes, every credential/exposure denial works, disposable-profile destruction is proven, manual fallback is documented, and P07-S010 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S009/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Never pause with an authenticated session open. Pause before login or only after browser closure, profile destruction, and durable job-state recording.
