# P06-S003: Create the agent development workspace

| Property | Value |
|---|---|
| Story ID | P06-S003 |
| Phase | P06 — Agent Engineering Foundation |
| Sequence | 3 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P06-S002 |
| Unlocks | P06-S004 |
| Preferred route | Interface: goagentic using Codex or Claude Code inside AI-Workbench; Provider: qualified Ollama model for mechanical scaffolding with OpenAI or Anthropic fallback; Model class: economical coding model; Effort: medium; Fallback: current Terra- or Sonnet-class implementation route with independent review. |
| Research freshness | Current Python packaging and selected framework docs checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to create a tested Python-first workspace with pinned dependencies, formatting, typing, tests, configuration, and secret handling, so progress is inspectable and independent of chat memory.

## 2. Bounded objective

Create a tested Python-first workspace with pinned dependencies, formatting, typing, tests, configuration, and secret handling.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P06-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Python packaging and selected framework docs checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not use training memory for changeable facts.

## 5. Preconditions and unlock conditions

P06-S002. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create `operations/ubuntu/p06/P06-S003-create-agent-workspace` and `workloads/agents/foundation/` with locked dependencies, `src/`, typed settings, tests, formatting/lint/type checks, `.env.example`, ignore rules, and clean-clone bootstrap/verify/rollback operations; deploy beneath the AI-Workbench Linux home.

## 7. Out of scope and prohibited changes

Do not use `/mnt/c` or `/mnt/h`, install global packages, store credentials, add LangSmith, expose a service, create agent powers, alter P02 toolchains, or overwrite a collision target.

## 8. Privilege and human approval

Before mutation, present the revision-bound P06 preview and obtain its single authorization. Changed roots, elevation, or dependency major versions require a new preview.

## 9. Risk rationale

Executable dependencies and a user workspace are added, but the change is confined to a new collision-checked Linux-home directory and removable environment.

## 10. Execution contract

Resolve the Linux path and accepted lock; reject collisions; verify provenance; create the skeleton; install locked project dependencies; run every development check from a clean clone; repeat apply; rehearse removal in a disposable clone; and checkpoint each unit.

## 11. Automated acceptance tests

Assert nonzero tests and required files. Reproduce the lock from a clean clone; pass import, format, lint, type, and smoke tests; prove Linux filesystem placement and absence of real secrets and `/mnt/*` roots. Fail on unlocked/global installs, collision, zero tests, or runtime network calls.

## 12. Human validation

Not applicable — filesystem, dependency, and clean-clone assertions require no credential or subjective owner judgment.

## 13. Idempotency and rollback

Second apply produces no diff. Rollback removes only the verified story-created disposable target or restores the workspace Git revision; it refuses unknown/nonempty paths and preserves P02 toolchains.

## 14. Required evidence

Commit the skeleton and operation plus `evidence/P06-S003/` activation, dependency manifest, path/collision proof, clean-clone results, idempotency, rollback rehearsal, secret scan, checkpoint, and review.

## 15. Definition of done

The Linux-home workspace reproduces from lock, all checks pass, secrets and Windows mounts are excluded, rollback is proven, review resolves, and P06-S004 unlocks.

## 16. Pause-safe boundaries

Pause after preflight, skeleton commit, lock, install, test group, or disposable rollback. Never pause during lock replacement; record the next command in `evidence/P06-S003/checkpoint.json`.
