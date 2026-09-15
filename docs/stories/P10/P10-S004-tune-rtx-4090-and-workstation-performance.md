# P10-S004: Tune RTX 4090 and workstation performance

| Property | Value |
|---|---|
| Story ID | P10-S004 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 4 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P10-S003 |
| Unlocks | P10-S005 |
| Preferred route | Interface: Codex CLI across Windows and AI-Workbench through goagentic; Provider: controller-selected cloud provider; Model class: performance engineering; Effort: high; Fallback: second provider reviews measurements and profile choice before activation. |
| Research freshness | Current Ollama context/concurrency/keep-alive and NVIDIA NVSMI guidance checked within 7 days; exact model registry and drivers read at execution. |

## 1. User story
As the owner, I want measured RTX 4090 profiles that balance quality, speed, agent concurrency, thermals, and room for normal desktop work.
## 2. Bounded objective
Create `operations/windows/p10/P10-S004-performance/Measure-WorkstationProfile.ps1`, `Set-WorkstationProfile.ps1`, and `Restore-WorkstationProfile.ps1`; `config/performance/windows-4090-profiles.yaml`; and reproducible `tests/p10/performance/` workloads.
## 3. Learning objective
Not applicable — profile selection concepts were taught in P03 and reinforced in P10-S002.
## 4. Current research requirements
Verify Ollama memory scaling, parallel-request behavior, context controls, keep-alive, processor reporting, and current NVIDIA metric semantics. Local measurements override generic tuning claims.
## 5. Preconditions and unlock conditions
P10-S003 is Done; accepted model hashes and task suite exist; background workload is controlled; ambient/test conditions, driver, Ollama, and service versions are recorded.
## 6. In scope
`fast`, `balanced`, `quality`, and `constrained` profiles; warm/cold latency; tokens/second; time-to-first-token; task success; context size; parallel requests; model residency/offload; VRAM/RAM; GPU utilization, temperature, power, and throttle reason; service overhead; and desktop responsiveness.
## 7. Out of scope and prohibited changes
No GPU overclock, voltage/firmware modification, unsupported driver tweak, disabling thermal protection, invented benchmark, public benchmark claim, or making maximum advertised context the default without measurement.
## 8. Privilege and human approval
No new approval for bounded user/service settings covered by P10 authorization. Stop and request a new preview for driver, firmware, power-limit, or admin changes.
## 9. Risk rationale
High: sustained GPU load and multi-service tuning can destabilize the workstation or hide CPU spill; failure injection and cross-provider review are required.
## 10. Execution contract
Run a recorded idle baseline; execute the same fixed prompt/task corpus for each profile with repetitions; sample metrics to machine-readable logs; reject thermal throttling, OOM, unexplained queueing, silent CPU spill, or desktop-headroom failure; choose defaults from measured tradeoffs; preserve prior settings.
## 11. Automated acceptance tests
Each profile has at least three valid runs; normal profiles retain at least 3 GB free VRAM at steady state, show the intended processor placement in `ollama ps`, avoid OOM/throttle events and unintended CPU spill, and pass an activation-defined desktop responsiveness threshold. Results include median and dispersion, invalid-run reasons, service-concurrency and overload/503 behavior, no-op apply, and rollback equality.
## 12. Human validation
Owner compares blinded plain-language `fast`, `balanced`, and `quality` samples and confirms the selected default remains comfortable during normal desktop use.
## 13. Idempotency and rollback
Measurement never mutates persistent settings. Reapplying an active profile no-ops; rollback restores the exact captured Ollama/service settings.
## 14. Required evidence
Commit operations/config/tests plus `evidence/P10-S004/activation.json`, `baseline.json`, `corpus-manifest.json`, raw sanitized measurements, `profile-comparison.json`, `selection.md`, `second-run.json`, `rollback.json`, `human-validation.md`, `cross-provider-review.md`, and `checkpoint.json`.
## 15. Definition of done
All four profiles are reproducible, unsafe configurations are rejected, the default is justified by measurements and owner experience, rollback/no-op tests pass, and P10-S005 unlocks.
## 16. Pause-safe boundaries
Pause between benchmark runs or after restoring captured settings; never leave an unattended stress workload running.
