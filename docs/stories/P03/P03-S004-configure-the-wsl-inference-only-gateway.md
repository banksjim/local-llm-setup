# P03-S004: Configure the WSL inference-only gateway

| Property | Value |
|---|---|
| Story ID | P03-S004 |
| Phase | P03 — Local Inference and Model Foundation |
| Sequence | 4 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Critical |
| Actor | Human + LLM |
| Dependencies | P03-S003 |
| Unlocks | P03-S005 |
| Preferred route | Interface: goagentic in the designated cloud IDE or CLI; Provider: OpenAI or Anthropic, different from the implementer for acceptance review; Model class: current quality or review model; Effort: high; Fallback: stop and switch to the current Sol or Sonnet-class route; qualified local models remain advisory during probation. |
| Research freshness | Current Ollama APIs, Windows Firewall, and WSL networking checked within 7 days. |

## 1. User story

As the workstation owner, I want this story to expose only required inference and read routes from Ubuntu through a dedicated port and WSL-subnet firewall rule, so that progress is inspectable and independent of chat memory.

## 2. Bounded objective

Expose only required inference and read routes from Ubuntu through a dedicated port and WSL-subnet firewall rule.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P03-S002; this story introduces no separate learning objective.

## 4. Current research requirements

Current Ollama APIs, Windows Firewall, and WSL networking checked within 7 days. Record dates, versions, direct links, claims, conflicts, and inferences; do not rely on training memory for changeable facts.

## 5. Preconditions and unlock conditions

P03-S003. Applicable specs, clean Git, valid controller state, current research, route, and lease checks pass.

## 6. In scope

Create and verify the story-owned Windows reverse-proxy configuration, private activation-selected listener port, Windows Firewall rule scoped to the discovered AI-Workbench subnet, deny-by-default inference/read route allowlist, WSL user-level 127.0.0.1:11434 forward, client identity probes, LAN and administration-route negative probes, and complete proxy, forward, and firewall removal. Store the operation at operations/windows/p03/P03-S004-configure-the-wsl-inference-only-gateway with its Ubuntu companion under operations/ubuntu/p03/P03-S004-configure-the-wsl-inference-only-gateway and evidence under evidence/P03-S004/.

## 7. Out of scope and prohibited changes

Do not install containers or desktop clients, expose Ollama to the LAN, delete existing models, change BIOS or GPU drivers, accept floating model tags, or route unqualified controller work to a local model.

## 8. Privilege and human approval

No new approval is required while the revision-bound P03 phase authorization still matches the work. The owner must personally perform the named GUI, authentication, elevation, microphone, preference, or acceptance actions; changed scope stops for a new preview.

## 9. Risk rationale

A Windows-to-WSL gateway and firewall rule create a security boundary; an overbroad bind could expose unauthenticated model administration.

## 10. Execution contract

Discover current Windows and WSL addressing; select and prove a free private port; generate an explicit allowlist from the current Ollama, Codex, and Claude client contracts; preview the proxy, forward, and firewall changes; confirm P03 authorization; apply one reversible unit at a time; prove allowed inference/read calls through WSL loopback and denied administration/LAN calls; remove and reapply the boundary; record evidence and release the lease.

## 11. Automated acceptance tests

Assert a nonempty, deny-by-default route fixture set. Verify approved Ollama native, OpenAI-compatible Responses, and Anthropic-compatible inference/read routes required by the accepted clients; reject model pull, create, copy, push, and delete routes, unknown routes, non-AI-Workbench WSL sources, and LAN sources; confirm Ollama itself remains loopback-only; prove forward/proxy/firewall removal and reapply. Any unclassified route or zero negative fixtures fails.

## 12. Human validation

The owner handles the Windows Firewall elevation prompt, inspects the resolved listener address, port, WSL source range, and route allowlist, and records whether those boundaries match the preview in evidence/P03-S004/human-validation.md. No credential or microphone action is required. The LLM cannot claim that the displayed boundary matched or write the owner's decision.

## 13. Idempotency and rollback

The operation at operations/windows/p03/P03-S004-configure-the-wsl-inference-only-gateway must implement preview, apply, verify, and story-owned rollback. A second apply is a no-op; rollback restores the recorded pre-story configuration without deleting user models, databases, documents, repositories, or unrelated settings.

## 14. Required evidence

Commit operations/windows/p03/P03-S004-configure-the-wsl-inference-only-gateway or its versioned result plus evidence/P03-S004/activation.json, evidence/P03-S004/change-inventory.json, evidence/P03-S004/test-results.json, evidence/P03-S004/rollback.json, and evidence/P03-S004/review.md; include exact versions or digests, sanitized commands or observations, timestamps, and genuine owner-authored human validation.

## 15. Definition of done

P03-S004 is Done only when AI-Workbench can perform approved inference and model-read calls; LAN clients, disallowed administration routes, and traffic outside the current WSL subnet fail; rollback removes the gateway and firewall rule; the story-owned output and evidence inventory exist, independent review has no unresolved material finding, rollback and idempotency evidence is accepted, and controller state unlocks the declared next story.

## 16. Pause-safe boundaries

Pause after the activation packet, after each download, install, configuration backup, or other atomic unit, after tests, and after evidence is committed. Before pausing, finish or roll back the active unit and record the exact next command plus current model and provider in evidence/P03-S004/checkpoint.json.
