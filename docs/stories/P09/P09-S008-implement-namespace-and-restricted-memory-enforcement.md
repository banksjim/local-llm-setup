# P09-S008: Implement namespace and restricted-memory enforcement

| Property | Value |
|---|---|
| Story ID | P09-S008 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 9 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S007 |
| Unlocks | P09-S009 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: different cloud provider from P09-S007 implementer; Model class: high-reliability security; Effort: high; Fallback: disable all recall and retain ledger-only administration. |
| Research freshness | Current authorization, encryption, selected-framework namespace/filter, logging, and backup docs checked within 7 days. |

## 1. User story
As the owner, I want deterministic least-privilege recall so one agent, query, log, export, or backup cannot cross a memory boundary.
## 2. Bounded objective
Implement workloads/agents/memory/policy/ and operations/ubuntu/p09/P09-S008-memory-policy/ with owner/agent/class/namespace/purpose enforcement before both projection query and ledger fetch.
## 3. Learning objective
Not applicable — P09-S003 covers namespaces and Restricted memory.
## 4. Current research requirements
Verify framework filter behavior rather than assuming it is authorization; confirm encryption, key separation, cache/log/backup behavior, and known bypasses.
## 5. Preconditions and unlock conditions
P09-S007 is Done. Activation fixes principals, exact matrix, namespace grammar, Restricted defaults, purpose taxonomy, result/token limits, retention, export/backup exclusions, and keys.
## 6. In scope
Deny-by-default authorization; separate service identities; pre-query and post-result enforcement; Restricted isolation; retention/expiry; cache control; redaction; export/backup policy; audit; revocation; and synthetic namespaces.
## 7. Out of scope and prohibited changes
No wildcard/global recall, model-chosen identity/purpose, filter-only authorization, shared credentials, candidate access, cross-owner/agent cache, raw value logging/tracing, or policy from memory content.
## 8. Privilege and human approval
Covered by P09 authorization; any expanded principal, namespace, purpose, or export requires new preview and approval.
## 9. Risk rationale
Critical: this is an access-control boundary for sensitive private data. Revision-bound authorization, isolated rehearsal, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Rehearse matrix in isolated synthetic namespaces; enforce identity/purpose outside model/framework; query least privilege; post-filter ledger IDs; cap results; test keys/caches/logs/backups/revocation; verify outage closed; and cross-provider security review.
## 11. Automated acceptance tests
Test every allowed/denied matrix cell plus forged identity/purpose, wildcard, path/filter injection, namespace collision, candidate/rejected/superseded/deleted/expired record, Restricted export/backup, cache bleed, trace/log leak, key rotation, revocation, framework bypass, and projection poisoning. Any cross-boundary result fails the gate.
## 12. Human validation
Not applicable — P09-S012 demonstrates owner controls; engineering isolation uses synthetic canaries and independent review.
## 13. Idempotency and rollback
Same matrix is no-op. Rollback disables recall, restores prior policy/keys/config, flushes tagged caches, and preserves the ledger.
## 14. Required evidence
evidence/P09-S008/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, access-matrix.json, canary-results.json, leak-scan.json, key-rotation.json, and revocation-results.json.
## 15. Definition of done
Every denied path fails before disclosure, allowed recall returns only approved current provenance, Restricted data stays isolated, and review resolves.
## 16. Pause-safe boundaries
Update evidence/P09-S008/checkpoint.json after matrix, canary, key, cache, backup, revocation, and review gates; disable recall before pausing on any leak.
