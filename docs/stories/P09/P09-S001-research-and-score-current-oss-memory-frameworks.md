# P09-S001: Research and score current OSS memory frameworks

| Property | Value |
|---|---|
| Story ID | P09-S001 |
| Phase | P09 — Durable Agent Memory |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P08-S010 |
| Unlocks | P09-S002 |
| Preferred route | Interface: WSL coding agent through goagentic; Provider: controller-selected cloud provider; Model class: research-capable; Effort: high; Fallback: second provider for disputed license, security, or feature claims. |
| Research freshness | Official repositories, docs, releases, issues, licenses, benchmarks, and advisories checked within 7 days. |

## 1. User story
As the owner, I want a reproducible current comparison so the memory layer is chosen from evidence rather than popularity.
## 2. Bounded objective
Create docs/research/p09/P09-S001-oss-memory-scorecard.md plus sources.json and scores.json comparing Mem0, LangGraph Store/LangMem, Graphiti, Letta, Cognee, Hindsight, Supermemory, and credible new alternatives.
## 3. Learning objective
Not applicable — P09-S003 teaches the selected design after selection.
## 4. Current research requirements
Verify repository and release activity, exact license, self-hosted feature parity, local Ollama compatibility, telemetry, dependencies, resource needs, security disclosures, export/deletion, and benchmark methodology from primary sources. Separate managed-product claims from OSS evidence.
## 5. Preconditions and unlock conditions
P08-S010 is Done and SYS-MEM is current. The activation packet fixes weighted criteria, minimum gates, hardware budget, and research cutoff before scoring.
## 6. In scope
Runnable isolated smoke tests with synthetic data; license and maintenance health; WSL/Rancher fit; LangGraph integration; provenance; owner-review overlay feasibility; namespaces; deletion/export; offline behavior; migration; observability; and total resource cost.
## 7. Out of scope and prohibited changes
No winner chosen in advance, persistent install, private data, cloud signup, paid key, vendor benchmark accepted without reproduction, or SaaS feature counted as OSS.
## 8. Privilege and human approval
No privilege. Disposable local test processes require no phase authorization and are removed after evidence capture.
## 9. Risk rationale
Medium: research executes untrusted packages in isolation but creates no persistent service or private data.
## 10. Execution contract
Freeze criteria; verify primary sources; test each viable candidate in an isolated network/storage namespace; reproduce a small common retain/recall/update/delete/export suite; score with uncertainty; document rejected candidates and a composable baseline; and obtain fresh-session review.
## 11. Automated acceptance tests
Require all eight named candidates or an evidence-backed disqualification; validate score arithmetic, licenses, source dates, feature provenance, synthetic smoke-test parity, cleanup, and contradictions. Fail any candidate needing cloud service, unexplained telemetry, missing export/delete, or opaque sole storage.
## 12. Human validation
Not applicable — technical comparison is independently reviewed; P09-S002 presents only owner-relevant tradeoffs.
## 13. Idempotency and rollback
Reruns preserve prior scores and append superseding evidence. Rollback removes disposable environments and restores the prior research record.
## 14. Required evidence
evidence/P09-S001/ must contain activation.json, change-inventory.json, test-results.json, rollback.json, checkpoint.json, review.md, sources.json, scores.json, licenses.json, smoke-tests.json, and contradictions.json.
## 15. Definition of done
Every candidate has a reproducible result, no managed claim is misrepresented, uncertainty is explicit, and P09-S002 has a ranked recommendation plus fallback.
## 16. Pause-safe boundaries
Update evidence/P09-S001/checkpoint.json after each candidate; remove its disposable process/network before pausing.
