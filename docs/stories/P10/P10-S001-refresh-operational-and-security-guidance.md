# P10-S001: Refresh operational and security guidance

| Property | Value |
|---|---|
| Story ID | P10-S001 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 1 |
| Status | Planned |
| Step | Research |
| Hold reason | Phase Not Activated |
| Risk | Low |
| Actor | LLM |
| Dependencies | P09-S012 |
| Unlocks | P10-S002 |
| Preferred route | Interface: web-capable coding agent through goagentic; Provider: controller-selected cloud provider; Model class: economical research with synthesis; Effort: medium; Fallback: second cloud provider verifies unresolved or security-significant claims. |
| Research freshness | Official documentation, stable releases, migration notes, and security advisories checked within 7 days of activation. |

## 1. User story
As the owner, I want one current operational baseline so later work does not rely on stale model memory or scattered web notes.
## 2. Bounded objective
Create `docs/research/P10/source-register.yaml`, `component-lifecycle-matrix.yaml`, `risk-register.yaml`, and `operational-security-baseline.md` for every accepted P02–P09 component and data class.
## 3. Learning objective
Not applicable — P10-S002 teaches the owner from these results.
## 4. Current research requirements
Use primary Windows/WSL, PowerShell, Rancher Desktop, Ollama, Open WebUI, NVIDIA, container-image, database, and selected-framework sources. Record retrieval date, applicable installed/planned version, direct URL, supported claim, conflicts, and inference. Security advisories override general guides.
## 5. Preconditions and unlock conditions
P09-S012 is Done. The activation packet fixes the accepted component inventory and rejects a zero-item scan.
## 6. In scope
Install/update/removal interfaces; database migrations; configuration/data locations; listeners; telemetry; credentials; backup consistency; restore prerequisites; driver/runtime compatibility; and known rollback limits.
## 7. Out of scope and prohibited changes
No downloads, installation, authentication, workstation probing beyond accepted read-only inventory, component replacement, private-data access, or architecture change.
## 8. Privilege and human approval
Not applicable — public research and sanitized read-only inventory only.
## 9. Risk rationale
Low: reversible documentation only. A finding that changes scope or architecture blocks unlock and becomes a design-change story.
## 10. Execution contract
Reconcile the accepted inventory with live read-only versions; research every row; distinguish stable from preview releases; never treat marketing, a search snippet, or an LLM assertion as authority; map every material finding to a later P10 story.
## 11. Automated acceptance tests
The component matrix contains every accepted component and data class; every changeable claim has a dated primary URL; every row names update, backup, rollback, and removal behavior or a justified unsupported value; URLs resolve; no source is older than the freshness window; and no secret/private content appears.
## 12. Human validation
Not applicable — independent lightweight review checks coverage and citations.
## 13. Idempotency and rollback
Rerun replaces dated research deterministically for the same cutoff and inventory. Git reversion removes this story’s records.
## 14. Required evidence
Commit the four research artifacts plus `evidence/P10-S001/activation.json`, `inventory.json`, `source-check.json`, `coverage.json`, `review.md`, and `checkpoint.json`.
## 15. Definition of done
Every component and data class has current, traceable operating facts; conflicts are resolved or blocking; downstream story mappings are complete; checks pass; and P10-S002 unlocks.
## 16. Pause-safe boundaries
Pause after any completed source row and committed checkpoint; never report a partial inventory as complete.
