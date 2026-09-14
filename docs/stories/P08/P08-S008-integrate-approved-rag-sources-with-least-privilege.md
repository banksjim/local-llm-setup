# P08-S008: Integrate approved RAG sources with least privilege

| Property | Value |
|---|---|
| Story ID | P08-S008 |
| Phase | P08 — Practical Personal Agents |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P08-S007 |
| Unlocks | P08-S009 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: high-reliability security implementation; Effort: high; Fallback: detach all collections and operate agents without RAG. |
| Research freshness | P07 retrieval contract, current Open WebUI/LangChain RAG behavior, and OWASP prompt-injection/vector threats checked within 7 days. |

## 1. User story

As the owner, I want each agent to retrieve only explicitly approved knowledge so useful context never becomes a path to data leakage or policy override.

## 2. Bounded objective

Implement workloads/agents/personal/retrieval/ and operation operations/windows/p08/P08-S008-agent-rag-access/ with an explicit agent-to-knowledge-base allowlist, provenance-preserving citations, and retrieval treated as untrusted data.

## 3. Learning objective

Not applicable — P07 and P08-S002 cover RAG and capability boundaries.

## 4. Current research requirements

Revalidate P07 namespace/authentication semantics, current retrieval APIs, Open WebUI attached-knowledge behavior, model tool reliability, and prompt-injection defenses. Reject implicit global collection access.

## 5. Preconditions and unlock conditions

P08-S007 and P07-S017 are Done. Activation names exact immutable collection versions per agent, principal/credential references, source sensitivity, allowed metadata filters, citation format, query/result limits, and rollback snapshot.

## 6. In scope

Deny-by-default allowlist; separate read-only service identities; collection/version pinning; metadata filters; bounded top-k/query size; provenance; source date/applicability; citations; injection-resistant data framing; policy isolation; audit events without raw content; and detach/revoke operations.

## 7. Out of scope and prohibited changes

No write/update/delete to a knowledge base, wildcard/all-collection access, direct source-root mount, cross-agent result sharing, web browsing, unapproved external source, retrieved instruction execution, P09 memory, or credential in Git/log/prompt.

## 8. Privilege and human approval

The explicit revision-bound P08 phase authorization covers the exact collection/principal matrix. Any added source, widened namespace, or write capability requires a new preview and approval; owner acceptance remains separately required in P08-S010.

## 9. Risk rationale

Critical: this creates an access-control boundary around private knowledge; namespace or authorization failure could disclose owner data across agents. The explicit revision-bound P08 phase authorization, isolated rehearsal, cross-provider review, and genuine owner acceptance in P08-S010 are mandatory.

## 10. Execution contract

Checkpoint agent/runtime/P07 state; rehearse the complete access matrix in an isolated synthetic namespace; create least-privilege principals; attach only pinned collections; wrap retrieved chunks as untrusted evidence; strip active content; enforce policy outside the prompt; preserve citations; validate source freshness; register config; test; and cross-provider security review.

## 11. Automated acceptance tests

First prove the full matrix, detach, revoke, and rollback in an isolated synthetic P07 knowledge base. Then prove each agent reads only its real approved matrix entries; unauthorized/cross-namespace/version-mismatch requests fail; retrieved “ignore policy,” tool-call, secret-exfiltration, false-citation, poisoned metadata, oversize, stale, and deleted-source fixtures cannot alter policy or access. Verify citations map to immutable derivatives, credentials/redacted traces are clean, detach/revoke is immediate, restart and no-op rerun work, and P07 data is unchanged.

## 12. Human validation

Not applicable — technical access and injection testing are automated and independently reviewed. Owner judges answer usefulness in P08-S010.

## 13. Idempotency and rollback

Same matrix produces no change. Rollback detaches collections, revokes P08 principals, restores agent configuration, and leaves P07 source/normalized/Git/index layers unchanged.

## 14. Required evidence

evidence/P08-S008/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, access-matrix.json, isolation-results.json, injection-results.json, citation-results.json, and revocation-results.json.

## 15. Definition of done

Access is explicit and least-privilege, citations preserve provenance, injected retrieval cannot change policy or capability, revocation works, and P07 integrity remains verified.

## 16. Pause-safe boundaries

Update evidence/P08-S008/checkpoint.json after each principal, collection, injection, revocation, and review gate. Detach the affected collection before pausing on any isolation or policy failure.
