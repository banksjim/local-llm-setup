# P01-S010: Implement Codex and Claude controller adapters

| Property | Value |
|---|---|
| Story ID | P01-S010 |
| Phase | P01 — Program Control and Quality Foundation |
| Sequence | 11 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | High |
| Actor | LLM |
| Dependencies | P01-S009 |
| Unlocks | P01-S011 |
| Preferred route | Interface: Codex CLI in the repository; Provider: OpenAI; Model class: architecture-capable implementation; Effort: medium; Fallback: Claude Code with an Anthropic architecture-capable model at medium effort; each provider adapter requires review using the other provider. |
| Research freshness | Current official Codex skills and Claude Code skills/commands documentation checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to provide provider-independent Codex instructions and Claude Code command skills using the same controller core, so that the program advances with inspectable quality and without relying on chat memory.

## 2. Bounded objective

Provide provider-independent Codex instructions and Claude Code command skills using the same controller core. P01 validates portable packages and fixture contracts; live authenticated client validation is explicitly deferred to P05-S007 and P05-S008.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P01-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current official Codex skills and Claude Code skills/commands documentation checked within 7 days. Record access date, version, direct links, material claims, conflicts, and inferences. Do not rely on model training memory for changeable facts.

## 5. Preconditions and unlock conditions

P01-S009. Applicable specifications, clean Git state, current research, required model route, and the accepted bootstrap-or-controller checks must pass.

## 6. In scope

Create thin packages under `goagentic/adapters/codex/` and `goagentic/adapters/claude/` that translate each interface's command or skill convention into the same controller command schema; include installation instructions, generated-command fixtures, conformance tests, and an adapter-version manifest.

## 7. Out of scope and prohibited changes

Duplicating controller policy inside adapters, storing credentials, live authenticated Codex or Claude execution before P05, provider-specific changes to story semantics, unsupported model switching, and publishing private user configuration.

## 8. Privilege and human approval

Not applicable — P01 performs repository and isolated-target work under its phase authorization; live client login and configuration are deferred to P05.

## 9. Risk rationale

The story is High risk because divergent adapters could bypass approval, route, or evidence controls even though they share a core. Provider-to-provider conformance tests and reciprocal review are required; live client validation remains explicitly deferred to P05.

## 10. Execution contract

Preview changes and tests; verify preconditions; acquire the currently accepted P01 mutation guard—the bootstrap lock through P01-S006 and the controller lease only after P01-S006 is accepted; execute the smallest reversible operations; stop on drift; test; record sanitized evidence; release the guard; and route to review or human validation. Fixture contract tests prove equivalent structured requests and results; they do not claim live client acceptance.

## 11. Automated acceptance tests

Fixture contract tests prove equivalent requests, state, and next-action results from both adapter packages. Live Codex CLI and Claude Code tests are deferred to P05-S007 and P05-S008 and therefore cannot be used to mark Cross-Interface Trusted in P01. Applicable schema, scope, secret, link, static, idempotency, rollback, and dependency checks also pass.

## 12. Human validation

Not applicable — P01 validates isolated adapter conformance only. The owner performs live Codex and Claude client validation in P05-S007 and P05-S008.

## 13. Idempotency and rollback

Generating or installing the same adapter version into an isolated fixture target produces no duplicate command and no content drift. Rollback removes only files listed in that adapter's manifest and leaves controller core, user-created commands, and credentials untouched.

## 14. Required evidence

Story revision; current interface documentation; adapter manifests and hashes; command-by-command normalized request and response comparisons; bypass-denial results; isolated install, rerun, and uninstall evidence; deferred live-test declaration; secret scan; and reciprocal provider-review verdicts.

## 15. Definition of done

Both adapters produce the same normalized controller behavior for every command and denial fixture, contain no independent policy or secrets, install and remove cleanly in fixtures, document the P05 live-validation hold, and unblock P01-S011.

## 16. Pause-safe boundaries

Pause after each adapter package is generated, after isolated install, after conformance fixtures, and after isolated uninstall. Never pause with an adapter half-installed into a target; finish its manifest transaction or roll it back.
