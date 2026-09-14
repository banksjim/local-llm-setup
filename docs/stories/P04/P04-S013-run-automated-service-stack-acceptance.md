# P04-S013: Run automated service-stack acceptance

| Property | Value |
|---|---|
| Story ID | P04-S013 |
| Phase | P04 — Open WebUI and Supporting AI Services |
| Sequence | 13 |
| Status | Planned |
| Step | Testing |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | LLM |
| Dependencies | P04-S012 |
| Unlocks | P04-S014 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Not applicable — tests execute the accepted P04 versions and contracts; version drift returns the story to research. |

## 1. User story

As the workstation owner, I want an automated stack-wide failure and recovery suite before human acceptance, so that the destructive portions of validation are repeatable and bounded.

## 2. Bounded objective

Verify service health, integration, restart, dependency failure, backup, isolated restore, resource ceilings, and network denial with synthetic data.

## 3. Learning objective

Not applicable — this is an automated quality gate using the P04-S002 concepts already completed by the owner.

## 4. Current research requirements

Not applicable — no recommendation is made. Record accepted versions; any mismatch blocks the suite and routes to P04-S001 rather than silently adapting.

## 5. Preconditions and unlock conditions

P04-S012 is Done; all P04 service manifests and accepted integration settings are committed; a current backup target and isolated restore target pass preflight.

## 6. In scope

Create tests/p04/P04-S013-run-automated-service-stack-acceptance with a nonzero test manifest covering every P04 service, synthetic chat/search/document/vector/trace/STT fixtures, ordered restart, one-service failure isolation, resource limits, host and LAN denials, full backup, isolated restore, checksum comparison, and cleanup. Store sanitized results under evidence/P04-S013/.

## 7. Out of scope and prohibited changes

Do not use owner documents or chats, overwrite live volumes during restore, factory-reset Rancher Desktop, alter accepted configuration, expose a port, test cloud providers, or repair a failure inside the test run.

## 8. Privilege and human approval

The revision-bound P04 authorization must explicitly include service stop/start, synthetic writes, backup, and isolated restore. Any live-volume restore or new target requires a new preview and authorization.

## 9. Risk rationale

The suite deliberately stops multiple services and exercises persistent backup/restore; a target-selection defect could affect the entire local AI service stack.

## 10. Execution contract

Assert the service and test inventory; snapshot state; create unique fixtures; run health and integration cases; stop one dependency at a time and verify isolation; restart in dependency order; export a complete backup; restore only to a new isolated target; compare checksums; run network/resource negatives; remove fixtures; restore baseline; record evidence and release the lease.

## 11. Automated acceptance tests

Assert at least one test per service and integration plus explicit negative cases. All tests must pass; zero-test, skipped critical test, unexpected version, live restore target, secret in output, checksum mismatch, LAN success, unrecovered service, or fixture residue is a hard failure.

## 12. Human validation

Not applicable — the owner performs the experiential workflow and restore observation in P04-S014 after this deterministic gate passes.

## 13. Idempotency and rollback

Each run uses unique fixtures and an empty isolated restore target, then removes both. Failure handling restores the pre-test service state from the snapshot and never imports backup data into live volumes.

## 14. Required evidence

Commit the test suite and manifest plus activation.json, pre/post inventories, per-test result, failure-injection timeline, backup manifest, isolated-restore location and checksums, network/resource results, cleanup proof, rollback.json, and independent review under evidence/P04-S013/.

## 15. Definition of done

The asserted nonzero suite passes without skip or residue, baseline state is restored, backup and isolated restore checksums match, all network negatives hold, independent review has no unresolved material finding, and P04-S014 unlocks.

## 16. Pause-safe boundaries

Pause only at the pre-test snapshot, after baseline restoration following each failure case, after backup completion, after isolated restore verification and cleanup, and after evidence commit. Never pause with a dependency intentionally stopped or restore incomplete; record the next command in evidence/P04-S013/checkpoint.json.
