# P01: Program Control and Quality Foundation

**Depends on:** None  
**Required outcome:** A trusted, provider-independent goagentic controller, canonical story/evidence contracts, and synchronized GitHub Project.  
**Status:** Planned

## Gate

The phase activates only after its dependencies are accepted and the owner authorizes its first story through the current controller policy. Research and design may occur earlier, but implementation cannot cross this gate.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P01-S001: Confirm current controller interfaces and provider capabilities](../../stories/P01/P01-S001-confirm-current-controller-interfaces-and-provider-capabilities.md) | Research | Low |
| 2 | [P01-S002: Learn the goagentic operating model](../../stories/P01/P01-S002-learn-the-goagentic-operating-model.md) | Learning | Low |
| 3 | [P01-S003: Define machine-readable program and story schemas](../../stories/P01/P01-S003-define-machine-readable-program-and-story-schemas.md) | Implementation | Medium |
| 4 | [P01-S004: Implement read-only orientation commands](../../stories/P01/P01-S004-implement-read-only-orientation-commands.md) | Implementation | Medium |
| 5 | [P01-S005: Implement atomic state and append-only events](../../stories/P01/P01-S005-implement-atomic-state-and-append-only-events.md) | Implementation | High |
| 6 | [P01-S006: Implement mutation lease and concurrency rejection](../../stories/P01/P01-S006-implement-mutation-lease-and-concurrency-rejection.md) | Implementation | High |
| 7 | [P01-S007: Implement pause and resume reconciliation](../../stories/P01/P01-S007-implement-pause-and-resume-reconciliation.md) | Implementation | High |
| 8 | [P01-S008: Implement bounded authorization and human gates](../../stories/P01/P01-S008-implement-bounded-authorization-and-human-gates.md) | Implementation | Critical |
| 9 | [P01-S009: Implement quality, evidence, and review gates](../../stories/P01/P01-S009-implement-quality-evidence-and-review-gates.md) | Implementation | High |
| 10 | [P01-S010: Implement Codex and Claude controller adapters](../../stories/P01/P01-S010-implement-codex-and-claude-controller-adapters.md) | Implementation | High |
| 11 | [P01-S011: Implement GitHub Project synchronization](../../stories/P01/P01-S011-implement-github-project-synchronization.md) | Implementation | High |
| 12 | [P01-S012: Run controller failure-injection suite](../../stories/P01/P01-S012-run-controller-failure-injection-suite.md) | Testing | High |
| 13 | [P01-S013: Perform independent cross-provider controller review](../../stories/P01/P01-S013-perform-independent-cross-provider-controller-review.md) | Review | High |
| 14 | [P01-S014: Complete owner controller acceptance drill](../../stories/P01/P01-S014-complete-owner-controller-acceptance-drill.md) | Human Validation | Critical |

## Completion

The phase is complete only when every non-superseded story is Done, required human evidence is genuine, independent review findings are resolved, rollback evidence exists, and the phase outcome is demonstrated on the reference workstation.

