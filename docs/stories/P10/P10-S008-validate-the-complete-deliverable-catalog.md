# P10-S008: Validate the complete deliverable catalog

| Property | Value |
|---|---|
| Story ID | P10-S008 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 12 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S015 |
| Unlocks | P10-S009 |
| Preferred route | Interface: fresh coding-agent session through goagentic; Provider: different cloud provider from the primary P10 documentation author; Model class: release/catalog verification; Effort: high; Fallback: another independent cloud provider with the same frozen candidate and no repair permission. |
| Research freshness | Producing-story sources must remain inside their declared windows; affected claims are refreshed before validation if expired. |

## 1. User story
As the owner, I want a machine-enforced catalog gate so an attractive but incomplete repository cannot be called delivered.
## 2. Bounded objective
Create `release/windows/deliverable-catalog.yaml` and `tests/p10/Test-DeliverableCatalog.ps1`, then validate the frozen release-candidate revision without authoring missing content in the reviewer context.
## 3. Learning objective
Not applicable — this is an independent technical gate.
## 4. Current research requirements
Use accepted source/version maps. Refresh only expired product claims; no product reselection or undocumented waiver.
## 5. Preconditions and unlock conditions
P10-S015 and all producers are Done; expected catalog is derived from the master, system, phase, and story authority chain; candidate commit is fixed and Git-clean.
## 6. In scope
All specifications and active stories (137 in the current P01–P10 baseline), operations, installer, maintenance wrappers, tests, configs, guides, Mermaid diagrams, model/usage tables, integration instructions, prompts, licenses/attribution, research metadata, and sanitized evidence indexes required by the active master manifest.
## 7. Out of scope and prohibited changes
No silent repair, workstation mutation, waiver, reducing expected counts to actual counts, accepting docs as execution evidence, or reading private content.
## 8. Privilege and human approval
Not applicable — frozen-revision, read-only validation. Defects return to their owning story and approval boundary.
## 9. Risk rationale
High: a false pass would hide missing safety/recovery deliverables across the workstation.
## 10. Execution contract
Generate expected items independently from requirements; assert nonzero counts; compare path, type, owner story, checksum, source freshness, test/evidence linkage, privacy class, and platform; run static/safe validators; emit defects only; fail on unknown or missing items.
## 11. Automated acceptance tests
The active master manifest’s exact story count and reciprocal acyclic graph validate, with 137 as the nonzero minimum baseline for the currently approved P01–P10 program; every catalog row exists and every required file is cataloged; PowerShell parses and analyzes; help/dry-run contracts exist; Markdown links and Mermaid syntax validate; commands/platform labels/model registry/prompts/freshness/terminology/licenses match; secrets/private paths/content are absent; zero applicable tests fails; deterministic rerun is byte-equivalent except timestamps.
## 12. Human validation
Not applicable — P10-S014/S015 contain usability checks and P10-S011 owns final acceptance.
## 13. Idempotency and rollback
Repeated validation never changes candidate files. Revert or delete generated evidence only; fixes occur in producer stories.
## 14. Required evidence
Commit catalog/test plus `evidence/P10-S008/activation.json`, expected-vs-actual.json, counts.json, freshness.json, static-results.json, privacy-scan.json, defects.json, rerun.json, independent-review.md, and `checkpoint.json`.
## 15. Definition of done
The complete nonzero catalog validates without waiver, all defects are resolved through owners, independent reviewer accepts the rerun, and P10-S009 unlocks.
## 16. Pause-safe boundaries
Pause between deterministic test groups; discard and rerun an interrupted group. Never combine partial results into a pass.
