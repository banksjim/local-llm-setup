# P10-S014: Write the core operator and usage guides

| Property | Value |
|---|---|
| Story ID | P10-S014 |
| Phase | P10 — Operations and Final Acceptance |
| Sequence | 10 |
| Status | Planned |
| Step | Implementation |
| Hold reason | Dependency |
| Risk | Medium |
| Actor | LLM |
| Dependencies | P10-S013 |
| Unlocks | P10-S015 |
| Preferred route | Controller-selected value route; qualified local documentation model allowed with independent factual review. |
| Research freshness | All product-specific instructions checked against current official documentation within the freshness window of the owning component. |

## 1. User story

As the workstation owner, I want focused install, architecture, model, usage, integration, agent, RAG, memory, and prompt guides, so that I can use the system without reconstructing decisions from implementation history.

## 2. Bounded objective

Write and cross-link the core conceptual and daily-use guides, including Mermaid architecture diagrams, platform boundaries, model-selection tables, tool integration instructions, and reusable Codex CLI prompts.

## 3. Learning objective

Not applicable — the owner preparation for this story is explicitly covered and evidenced by P10-S002; this story consolidates previously taught workflows.

## 4. Current research requirements

Recheck every product-specific instruction against official documentation and the accepted installed versions. Date sources and identify any instruction derived from measured local behavior rather than documentation.

## 5. Preconditions and unlock conditions

P10-S013 is accepted; the installed architecture and model registry are stable; all earlier usage and learning evidence is available; links, Git, controller, route, and lease checks pass.

## 6. In scope

Install overview, architecture, model guide, task-to-model usage recommendations, Open WebUI and tool integrations, VS Code/Codex/Claude workflows, agent/RAG/memory usage, security boundaries, Mermaid diagrams, and prompts folder documentation.

## 7. Out of scope and prohibited changes

Operations recovery procedures owned by P10-S015, new architecture decisions, unsupported product claims, copied long-form third-party content, secrets, and workstation mutation.

## 8. Privilege and human approval

Not applicable — this story changes versioned documentation and prompts only; external publication beyond the existing repository requires separate approval.

## 9. Risk rationale

Documentation is reversible, but inaccurate instructions could cause later unsafe actions. Current-source verification, measured-command validation, and independent review make Medium risk appropriate.

## 10. Execution contract

Derive instructions from accepted evidence, write for a nonexpert operator, separate Windows and WSL contexts, mark optional paths, use copy-safe commands, link authoritative sources, and keep prompts provider-independent where possible.

## 11. Automated acceptance tests

Required-file inventory, Markdown links, heading structure, Mermaid syntax, command parsing or safe validation, model-table registry consistency, platform-label checks, prompt presence, freshness metadata, secret scan, and terminology checks pass.

## 12. Human validation

The owner follows one model-selection workflow and one tool-integration lookup from the documentation without using this chat and reports any ambiguity.

## 13. Idempotency and rollback

Regeneration with unchanged accepted evidence produces no semantic change. Git reversion restores documentation without changing workstation state.

## 14. Required evidence

Guide inventory; source and measurement map; generated diagrams; link, command, prompt, freshness, terminology, and secret checks; changed-file list; independent review; and owner usability notes.

## 15. Definition of done

The complete core guide set and prompts are accurate, navigable, current, and usable independently; all checks pass; and P10-S015 is unblocked.

## 16. Pause-safe boundaries

Pause between individual guides, after each validated diagram or command set, and after durable commits. Do not leave a moved or renamed guide with broken incoming links.
