# P10-S010: Perform independent final architecture review

| Property | Value |
|---|---|
| Story ID | P10-S010 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 14 |
| Status | Planned |
| Step | Review |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P10-S009 |
| Unlocks | P10-S011 |
| Preferred route | Interface: fresh Codex CLI or Claude Code session through goagentic; Provider: different from the primary P10 implementation provider; Model class: architecture/security/recovery review; Effort: high; Fallback: another independent cloud provider; the author and reviewer must remain distinct. |
| Research freshness | Provider availability and any security/release claim questioned by the reviewer checked at review time. |

## 1. User story
As the owner, I want a genuinely independent technical review so I am not asked to detect defects outside my expertise.
## 2. Bounded objective
Produce `reviews/P10/final-architecture-review.md` and `reviews/P10/findings.json` against the frozen candidate, full specification authority chain, implementation, and evidence.
## 3. Learning objective
Not applicable — the owner receives a plain-language disposition, not a technical examination.
## 4. Current research requirements
Verify questioned current claims from primary sources; cite them. Do not reopen accepted choices merely from preference.
## 5. Preconditions and unlock conditions
P10-S009 is Done; candidate hash and complete evidence index are fixed; reviewer provider/session differs from material authorship; reviewer has read-only scope and no prior conclusion prompt.
## 6. In scope
Requirements traceability; architecture/trust boundaries; privilege/approval; privacy/secrets; Windows/WSL/container isolation; idempotency; migration; backup/restore; deletion; performance evidence; agent/RAG/memory safety; observability redaction; supply chain; docs usability evidence; residual risk; and negative-test sufficiency.
## 7. Out of scope and prohibited changes
No implementation repair, workstation mutation, private-content inspection, accepting missing evidence on author assertion, style-only churn, or claiming provider independence when it is absent.
## 8. Privilege and human approval
Read-only review; the existing P10 authorization covers the candidate. Critical control still requires isolated rehearsal evidence and P10-S011 owner acceptance. Owner decides only explicitly explained residual-risk tradeoffs.
## 9. Risk rationale
Critical: a false final verdict could accept architecture-invalidating security, privacy, loss, or recovery defects across the workstation. The reviewer must verify P10 phase authorization and isolated/disposable rehearsal evidence; P10-S011 supplies final owner acceptance.
## 10. Execution contract
Review parent-to-leaf and system-to-evidence; independently sample/reproduce tests; threat-model misuse/failure; grade findings Critical/High/Medium/Low with file/evidence references; prohibit self-dismissal; send fixes to owner stories; rerun affected and regression tests; issue a new verdict only after closure.
## 11. Automated acceptance tests
Reviewer identity/provider/session differs; all ten phases and master criteria are traced; every Critical/High control has evidence and negative/failure coverage; sampled checks reproduce; finding schema is valid; no unresolved Critical/High finding, unowned Medium, unsupported waiver, missing source, or private-data exposure remains.
## 12. Human validation
Owner receives a one-page plain-language summary and may accept only explicitly documented residual Medium/Low risks; no code or architecture judgment is requested.
## 13. Idempotency and rollback
Review does not mutate candidate. Rerun on the same hash preserves findings unless new evidence is cited; superseded verdicts remain in Git history and cannot be overwritten as if never issued.
## 14. Required evidence
Commit review/findings plus `evidence/P10-S010/activation.json`, candidate hash, reviewer-independence proof, trace matrix, reproduced-test sample, threat model, finding dispositions, residual-risk summary, owner decisions if any, final verdict, and `checkpoint.json`.
## 15. Definition of done
Two clean full review passes follow the last material correction, Critical/High findings are zero, remaining risks are owned and explained, independent verdict is Accept, and P10-S011 unlocks.
## 16. Pause-safe boundaries
Pause after a completed review domain or durable finding set; never issue a final verdict from a partial pass.
