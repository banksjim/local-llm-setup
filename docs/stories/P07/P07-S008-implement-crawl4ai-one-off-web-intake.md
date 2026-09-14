# P07-S008: Implement Crawl4AI one-off web intake

| Property | Value |
|---|---|
| Story ID | P07-S008 |
| Phase | P07 — RAG, Ingestion, and Knowledge-Base Capstone |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | Human + LLM |
| Dependencies | P07-S007 |
| Unlocks | P07-S009 |
| Preferred route | Interface: WSL coding agent plus isolated crawler service; Provider: controller-selected cloud provider; Model class: high-reliability coding; Effort: high; Fallback: second provider and static-HTML adapter. |
| Research freshness | Current Crawl4AI stable docs/releases, browser security notes, robots/legal guidance, and target-independent web standards checked within 7 days. |

## 1. User story

As the owner, I want safe one-off URL capture without LLM scraping so selected web pages become reproducible knowledge documents at low cost.

## 2. Bounded objective

Implement a public-web adapter under workloads/rag/adapters/web/ and reusable operation operations/windows/p07/P07-S008-crawl4ai-web-intake using Crawl4AI deterministic Markdown plus raw HTML or MHTML snapshot, bounded browser rendering, response metadata, links/media inventory, and the standard snapshot/derivative contracts.

## 3. Learning objective

Not applicable — P07-S002 covers the RAG concepts; this story implements the approved Crawl4AI adapter.

## 4. Current research requirements

Pin the current compatible release; verify current cache defaults, safe declarative hooks, session behavior, SSRF controls, redirect handling, and raw/MHTML capture. Record security advisories and license.

## 5. Preconditions and unlock conditions

P07-S007 is Done. Activation resolves crawler image digest, URL allow/deny policy, resource/time limits, user agent, capture profile, permitted outbound network, and synthetic/local test site.

## 6. In scope

Owner-supplied HTTP(S) URL; DNS/IP validation before and after redirects; public-address-only default; fresh bounded retrieval; deterministic non-LLM Markdown; CSS/XPath selection; raw capture; response/final-URL provenance; restart and quarantine.

## 7. Out of scope and prohibited changes

No crawling discovered links, scheduled scraping, LLM extraction/filtering, stealth/evasion defaults, proxy rotation, file/data URLs, localhost/private/link-local/cloud-metadata access, downloads/executables, authentication, CAPTCHA/paywall bypass, or arbitrary Python hooks.

## 8. Privilege and human approval

P07 authorization covers bounded outbound retrieval from the isolated crawler. Each live URL is owner supplied or explicitly allowlisted; no technical sign-off is requested.

## 9. Risk rationale

High: browser-rendered outbound content is untrusted and could target internal services or leak data.

## 10. Execution contract

Validate scheme/host, resolve and reject prohibited addresses, fetch with size/time/redirect limits, revalidate every redirect, preserve allowed raw content and metadata, convert without LLM, scan outputs, then enter the common validation pipeline. Dynamic code runs only inside the isolated browser with no private mounts or credentials.

## 11. Automated acceptance tests

Local controlled fixtures prove static HTML, JavaScript-rendered text, CSS selection, redirect provenance, image/link capture, and unchanged reingest. Denials cover localhost, RFC1918, link-local/metadata IP, DNS rebinding simulation, non-HTTP scheme, redirect to denied host, oversized body, timeout, executable download, malicious filename, arbitrary hook code, and network failure. All failures leave the active corpus unchanged.

## 12. Human validation

The owner supplies one public test URL and confirms the captured page title and useful body match the page. The LLM owns security and fidelity review.

## 13. Idempotency and rollback

Same captured bytes/profile reuse the snapshot and derivative. Rollback disables the adapter and removes synthetic/staged derivatives; immutable accepted captures remain.

## 14. Required evidence

The directory evidence/P07-S008/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, and review.md in addition to the story-specific artifacts below.

Pinned image/license, network policy, fixture results, at least twelve denial results, final/requested URL record, raw/Markdown hashes, no-LLM proof, second-run result, owner test outcome, rollback, and review at evidence/P07-S008/.

## 15. Definition of done

Bounded one-off public capture works; SSRF and code-execution denials pass; no LLM is invoked; failures do not publish; and P07-S009 becomes Ready.

## 16. Pause-safe boundaries

Before every pause, update evidence/P07-S008/checkpoint.json with completed unit, verified state, active model/provider, safe rollback point, and exact next operation.

Pause before outbound fetch or after immutable snapshot/manifest commit. An open browser session is closed before pausing.
