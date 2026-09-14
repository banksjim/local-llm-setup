# P03: Local Inference and Model Foundation

**Depends on:** P02  
**Required outcome:** Native Ollama uses the RTX 4090 with measured, role-qualified model profiles and a remaining-story routing reassessment.  
**Status:** Planned

## Gate

The phase activates only after dependencies are accepted and the owner authorizes its first story. Research and design may occur earlier, but implementation cannot cross this gate.

## Story sequence

| Seq. | Story | Step | Risk |
|---:|---|---|---|
| 1 | [P03-S001: Research current Ollama and local model landscape](../../stories/P03/P03-S001-research-current-ollama-and-local-model-landscape.md) | Research | Low |
| 2 | [P03-S002: Learn local inference, parameters, quantization, and context](../../stories/P03/P03-S002-learn-local-inference-parameters-quantization-and-context.md) | Learning | Low |
| 3 | [P03-S003: Install native Ollama with H drive model storage](../../stories/P03/P03-S003-install-native-ollama-with-h-drive-model-storage.md) | Implementation | High |
| 4 | [P03-S004: Configure the WSL inference-only gateway](../../stories/P03/P03-S004-configure-the-wsl-inference-only-gateway.md) | Implementation | Critical |
| 5 | [P03-S005: Pull candidate models with storage guards](../../stories/P03/P03-S005-pull-candidate-models-with-storage-guards.md) | Implementation | High |
| 6 | [P03-S006: Benchmark primary and fast candidates](../../stories/P03/P03-S006-benchmark-primary-and-fast-candidates.md) | Testing | High |
| 7 | [P03-S007: Evaluate embedding candidates](../../stories/P03/P03-S007-evaluate-embedding-candidates.md) | Testing | High |
| 8 | [P03-S008: Publish model usage recommendations](../../stories/P03/P03-S008-publish-model-usage-recommendations.md) | Implementation | Medium |
| 9 | [P03-S009: Qualify local models for controller roles](../../stories/P03/P03-S009-qualify-local-models-for-controller-roles.md) | Testing | High |
| 10 | [P03-S010: Reassess every remaining story for local execution](../../stories/P03/P03-S010-reassess-every-remaining-story-for-local-execution.md) | Review | High |
| 11 | [P03-S011: Complete model selection human acceptance](../../stories/P03/P03-S011-complete-model-selection-human-acceptance.md) | Human Validation | High |

## Completion

Every non-superseded story is Done; human evidence is genuine; review findings resolve; rollback evidence exists; and the outcome is demonstrated on the reference workstation.

