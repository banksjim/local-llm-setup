# P03: Local Inference and Model Foundation

**Depends on:** P02  
**Required outcome:** Native Ollama uses the RTX 4090 with measured, role-qualified model profiles and a remaining-story routing reassessment.  
**Status:** Planned

## Fixed architecture and execution boundary

- Run Ollama natively on Windows so the RTX 4090 uses the supported Windows NVIDIA path. Store model blobs under `H:\ai\models\ollama`; keep generated logs and benchmark artifacts under `H:\ai\logs\ollama` and `H:\ai\benchmarks`.
- Keep Ollama's native listener on Windows loopback. A story-owned Windows gateway exposes only activation-verified inference/read routes required by `AI-Workbench`; it binds an activation-selected private port, restricts the current WSL subnet in Windows Firewall, and rejects Ollama administration routes. A WSL user-level loopback forward presents that gateway on the local address expected by supported clients without changing Ollama's Windows bind. WSL-to-Windows addressing is discovered at activation rather than hard-coded. P04 may add a separate, equally narrow Rancher Desktop source rule only for Open WebUI.
- Treat 24 GB VRAM as a ceiling, not a target. The baseline comparison set is `qwen3.8:27b-q4_K_M` (primary multimodal/agent candidate), `qwen3.5:9b-q4_K_M` (fast multimodal candidate), and `qwen3-embedding:0.6b` (economical embedding baseline). Exact tags, digests, licenses, sizes, and a credible challenger must be refreshed by P03-S001; no floating tag is installed by later stories.
- Benchmark 16K first for interactive use. Test 32K and at least 64K only where the client or role requires it, recording KV-cache VRAM, spill, latency, and quality. Advertised maximum context is never accepted as the workstation default without measurement.
- Preserve at least 3 GB VRAM headroom during normal interactive use and test concurrent service load. A candidate that routinely spills into system RAM or displaces desktop/service headroom is not the default even if it completes the prompt.
- P03 produces reusable `operations/windows/p03`, `operations/ubuntu/p03`, and `tests/p03` preview/apply/verify/rollback operations for later composition; it does not build the final installer.

## Current source baseline (refresh at activation)

- [Ollama Windows documentation](https://docs.ollama.com/windows)
- [Ollama context-length guidance](https://docs.ollama.com/context-length)
- [Ollama Qwen3.8 registry entry](https://ollama.com/library/qwen3.8)
- [Ollama Qwen3.5 tags](https://ollama.com/library/qwen3.5/tags)
- [Ollama Qwen3 Embedding registry entry](https://ollama.com/library/qwen3-embedding)

## Gate

P03-S001 research and P03-S002 learning may run after P02 acceptance without privileged authorization. Before P03-S003 mutates the workstation, the controller presents one revision-bound preview covering the pinned Ollama install, H-drive targets, gateway/firewall, model downloads, benchmark load, and rollback operations; the owner gives one P03 phase authorization. Elevation prompts, learning answers, model preference, and final acceptance remain genuine human actions, not repeated approvals. Material changes to targets, network exposure, model inventory, risk, or operations invalidate the authorization.

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
