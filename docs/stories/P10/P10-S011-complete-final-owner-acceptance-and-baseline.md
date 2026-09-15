# P10-S011: Complete final owner acceptance and baseline

| Property | Value |
|---|---|
| Story ID | P10-S011 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 15 |
| Status | Planned |
| Step | Human Validation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P10-S010 |
| Unlocks | Not applicable — this completes the current Windows program; future work receives a new phase/story dependency. |
| Preferred route | Interface: goagentic guided owner checklist in the preferred coding interface; Provider: controller-selected cloud provider; Model class: clear acceptance facilitator; Effort: medium; Fallback: equivalent cloud assistant using the identical committed checklist; no model may answer for the owner. |
| Research freshness | Frozen accepted release, guides, commands, evidence, and residual-risk record; changed behavior blocks and returns to the owning story. |

## 1. User story
As the owner, I want a practical final walkthrough and immutable baseline so I know the system is useful, recoverable, and ready for ordinary use.
## 2. Bounded objective
Complete `release/windows/OWNER-ACCEPTANCE.md`, generate `release/windows/release-manifest.yaml` and `evidence-index.yaml`, record residual risks, and create an immutable annotated Git tag only after acceptance.
## 3. Learning objective
Demonstrate—not memorize—how to find next work, start/stop/check health, choose a task model, use Open WebUI, locate tool/agent/RAG/memory guidance, preview an update, locate backup/restore/removal safeguards, pause/resume after a zero-context restart, and identify when to stop/escalate.
## 4. Current research requirements
Not applicable — this validates the frozen release. Any detected drift reopens its owner story rather than being researched or repaired here.
## 5. Preconditions and unlock conditions
P10-S010 verdict is Accept with no Critical/High residual and owner-readable Medium/Low dispositions. Release commit, guides, safe commands, restored sample, and all genuine prior human evidence are available.
## 6. In scope
One normal chat/vision or voice workflow; one model-choice lookup; one safe status/start-stop cycle; one VS Code/WSL lookup; one accepted agent and RAG query with citation; memory inbox decision using synthetic content; update preview; backup-generation and isolated-restore evidence lookup; uninstall retention preview; incident stop choice; fresh-session `goagentic resume/next`; and release/tag verification.
## 7. Out of scope and prohibited changes
No technical architecture certification, private-data deletion, live restore overwrite, real crisis/medical/financial decision, new feature, defect repair, scope waiver, fabricated observation, or tag before all checks pass.
## 8. Privilege and human approval
The owner performs the checklist and explicitly accepts or rejects the release. An LLM may guide and record selections but cannot produce human observations. Acceptance is also the Critical-risk owner control.
## 9. Risk rationale
Critical: this decision establishes the trusted baseline for the entire workstation; false or coerced acceptance would hide material defects. It verifies P10 phase authorization and isolated/disposable rehearsal evidence, then supplies the required final owner acceptance.
## 10. Execution contract
Present one plain-language task at a time with expected result and safe stop; load state only from committed controller/release records; record pass/fail/ambiguous exactly; return defects to owner stories; regenerate manifests after corrections; verify clean synchronized main; request final acceptance; then create and verify the annotated tag without secrets.
## 11. Automated acceptance tests
Checklist has all declared scenarios; every linked artifact/evidence hash resolves; release manifest matches installed versions/digests/config profiles and candidate commit; residual risks match P10-S010; human evidence fields cannot be auto-filled; rejection blocks tag; tag points to accepted commit; clean-state `goagentic resume` identifies program completion and a future-phase route.
## 12. Human validation
Owner personally marks each scenario pass/fail/ambiguous, confirms documentation can be used without this chat, acknowledges residual risks, and states Accept or Reject. Any fail/ambiguous result blocks completion.
## 13. Idempotency and rollback
Rerun does not duplicate records or retag a different commit. Before tag, acceptance may be reset for corrections; after tag, change requires a new release/version and history remains immutable. No live data is rolled back here.
## 14. Required evidence
Commit release artifacts plus `evidence/P10-S011/activation.json`, scenario-results.json, genuine `human-validation.md`, residual-risk-acknowledgment.md, manifest-verification.json, Git/remote/tag verification, completion-state.json, and `checkpoint.json`.
## 15. Definition of done
Every scenario genuinely passes, no ambiguity remains, owner explicitly accepts, manifests and evidence resolve, tag is verified on synchronized main, controller reports current Windows program complete, and no future phase is implied complete.
## 16. Pause-safe boundaries
Pause between scenarios before acceptance/tagging. If interrupted after acceptance but before tag, revalidate release hash and owner record; never infer consent from prior chat.
