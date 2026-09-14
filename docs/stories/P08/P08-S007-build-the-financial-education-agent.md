# P08-S007: Build the financial-education agent

| Property | Value |
|---|---|
| Story ID | P08-S007 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P08-S006 |
| Unlocks | P08-S008 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability safety implementation; Effort: high; Fallback: disable preset and expose only deterministic calculators plus official education links. |
| Research freshness | Current CFPB, Investor.gov/SEC, IRS or other applicable primary guidance checked within 24 hours; runtime/model docs within 7 days. |

## 1. User story

As the owner, I want a financial-education agent that explains concepts and compares owner-entered scenarios without acting as an adviser or moving money.

## 2. Bounded objective

Implement workloads/agents/personal/financial_education/ and operation operations/windows/p08/P08-S007-financial-education/; register a private Open WebUI preset on the accepted primary model with deterministic calculators.

## 3. Learning objective

Not applicable — P08-S010 covers appropriate use and interpretation.

## 4. Current research requirements

Use current official consumer/investor/tax sources for factual claims; record jurisdiction, effective date, applicability, and expiry. Validate calculation formulas against independent fixtures. Do not treat social-media content as authority.

## 5. Preconditions and unlock conditions

P08-S006 is Done. Activation fixes owner jurisdiction, model profile, source allowlist, calculator schemas, role boundary, no-account-access rule, session retention, and export policy.

## 6. In scope

Versioned official source cards under workloads/agents/personal/financial_education/sources/; budget organization; cash-flow and debt education; emergency-fund concepts; compound-interest, amortization, savings, and scenario calculations; tradeoff questions; assumptions; uncertainty; current citations; and owner-confirmed Markdown/CSV export of owner-entered scenarios.

## 7. Out of scope and prohibited changes

No personalized security recommendation, prediction, trade, transfer, account/credential connection, fiduciary relationship, tax return, legal/tax/investment advice, regulatory determination, credit application, real-time price claim without approved source, RAG until P08-S008, durable memory, or silent write.

## 8. Privilege and human approval

Covered by P08 activation. Calculators are read-only pure functions. Every export requires preview/confirmation; any future account or transaction capability requires a new phase and approval.

## 9. Risk rationale

High: inaccurate or advice-like output can cause material financial harm despite no transaction privilege.

## 10. Execution contract

Apply deterministic intent classification and advice boundary; use decimal-safe versioned calculators with shown inputs/formula/result; require jurisdiction/effective-date metadata for sourced claims; label illustrations; cite primary sources; register privately; and cross-provider review.

## 11. Automated acceptance tests

Test budgets, compound interest, amortization, missing/invalid inputs, rounding, conflicting goals, specific-stock/crypto/tax/legal requests, guaranteed returns, fraud/impersonation, account credentials, transaction requests, stale/jurisdiction-mismatched facts, prompt injection, invented citations, no-memory disclosure, export controls, redaction, restart, rollback, and no-op rerun. Compare arithmetic with golden fixtures; an LLM judge cannot establish numeric correctness.

## 12. Human validation

Deferred to P08-S010. The owner judges clarity and usefulness using synthetic numbers, not professional correctness.

## 13. Idempotency and rollback

Same version is a no-op; identical calculator inputs yield identical outputs. Rollback removes the preset/graph/calculator version and restores runtime state without deleting approved exports.

## 14. Required evidence

evidence/P08-S007/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, calculator-golden-results.json, advice-boundary-matrix.json, citation-results.json, and open-webui-registration.json.

## 15. Definition of done

The agent explains and calculates accurately within its educational role, refuses transactions/advice, cites current applicable sources, protects private inputs, and passes independent review.

## 16. Pause-safe boundaries

Update evidence/P08-S007/checkpoint.json after calculator, boundary, citation, preset, and review gates. Disable the preset before pausing on any arithmetic, advice-boundary, or privacy failure.
