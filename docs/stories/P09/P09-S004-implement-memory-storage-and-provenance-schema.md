# P09-S004: Implement memory storage and provenance schema

| Property | Value |
|---|---|
| Story ID | P09-S004 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 5 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P09-S013 |
| Unlocks | P09-S005 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability data engineering; Effort: high; Fallback: framework-neutral PostgreSQL ledger with projection disabled. |
| Research freshness | ADR-selected storage, transaction, migration, encryption, and projection docs checked within 7 days. |

## 1. User story
As the owner, I want an authoritative, portable ledger so approved memory never depends on an opaque derived index.
## 2. Bounded objective
Implement workloads/agents/memory/ledger/ and operations/ubuntu/p09/P09-S004-memory-ledger/ with the SYS-MEM record, append-only versions, decision receipts, content tombstones, and rebuildable projections.
## 3. Learning objective
Not applicable — P09-S003 covers the data layers.
## 4. Current research requirements
Confirm selected transaction, migration, indexing, encryption, and deletion semantics; record deviations from the ADR.
## 5. Preconditions and unlock conditions
P09-S013 is Done. Activation fixes schema version, namespace grammar, canonical serialization, retention, integrity algorithm, embedding profile/dimension, and migration checkpoint.
## 6. In scope
Typed schemas; candidate/durable tables; immutable versions; provenance; anti-replay decision receipt; sensitivity/access policy; supersession; content purge plus non-content tombstone; export format; projection outbox; migrations; and synthetic fixtures.
## 7. Out of scope and prohibited changes
No extraction, owner UI, agent recall, mutable history, raw chat archive, secret storage, automatic approval, framework-only canonical state, or real personal data.
## 8. Privilege and human approval
Covered by P09 authorization; schema or deletion-semantic change invalidates it.
## 9. Risk rationale
Critical: this establishes authoritative private-data and deletion boundaries. Revision-bound authorization, isolated migration rehearsal, cross-provider review, and P09-S012 owner acceptance are mandatory.
## 10. Execution contract
Define schemas/validators; rehearse forward/back migration in isolation; implement transactional ledger/outbox; verify canonical hashes, version/supersession, purge/tombstone, export/import, projection rebuild, concurrency, restore, and no-op; review independently.
## 11. Automated acceptance tests
Reject missing provenance/decision/scope, mutable version, forged/replayed receipt, invalid transition, secret canary, cross-owner ID, dimension mismatch, resurrection, and partial outbox commit. Prove concurrent writes, migration round trip, projection rebuild equivalence, purge, backup restore, and exact export.
## 12. Human validation
Not applicable — synthetic data and independent data/security review suffice.
## 13. Idempotency and rollback
Migrations are versioned and repeat-safe. Rollback restores the isolated rehearsal or pre-migration checkpoint; it never rewrites accepted history.
## 14. Required evidence
evidence/P09-S004/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, schemas.json, migration-results.json, integrity-results.json, purge-results.json, and projection-rebuild.json.
## 15. Definition of done
The ledger is authoritative, append-only except explicit purge, portable, integrity-checked, projection-independent, migration-safe, and independently reviewed.
## 16. Pause-safe boundaries
Update evidence/P09-S004/checkpoint.json after schema and each migration/transaction/restore gate; never pause mid-migration or partial ledger/outbox transaction.
