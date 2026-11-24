# Portable Agent Workbench (PAW)

**Universal AI instructions, specialist agents, portable skills and evidence-led workflows.**

- **Repository:** `portable-agent-workbench`
- **Initial package:** v0.1.0 implementation blueprint
- **Primary formats:** Markdown, YAML frontmatter, JSON, JSON Schema
- **Operating model:** instructions-first; host-native tools are optional
- **Hard constraints:** no mandatory CLI, terminal, VPS, local server, API key, paid API, or proprietary coding-agent runtime.

## What this is

PAW is a portable library of instructions and structured skills. It is designed to be copied, uploaded, or imported into supported AI applications. It does not install tools, grant permissions, run code, browse websites, or create autonomous model instances by itself.

## Start here

1. Read [`00-START-HERE/QUICK-START.md`](00-START-HERE/QUICK-START.md).
2. Copy [`01-CORE-SYSTEM/MASTER-SYSTEM-INSTRUCTIONS.md`](01-CORE-SYSTEM/MASTER-SYSTEM-INSTRUCTIONS.md) into the host's system-instruction field when available, or paste it at the start of a conversation.
3. Use [`02-MASTER-ORCHESTRATION/MASTER-ORCHESTRATOR.md`](02-MASTER-ORCHESTRATION/MASTER-ORCHESTRATOR.md) for multi-stage tasks.
4. Activate only the relevant skill from `04-SKILLS/`.
5. Use the `08-PLATFORM-ADAPTERS/` guide for the host application.
6. Preserve project continuity using `09-TEMPLATES/PROJECT-STATE-TEMPLATE.md`.

## Capability tiers

| Tier | Meaning | Examples |
|---|---|---|
| T0 | Instruction-only | planning, analysis of supplied text, drafting |
| T1 | File-enabled | analyzing uploaded documents, screenshots, code |
| T2 | Tool-enabled | web search, browser, connected apps, code execution |
| T3 | Runtime-dependent | persistent automation, MCP, local models, native instrumentation |

A workflow must disclose its required tier. If a tier is unavailable, it must switch to a lower-tier method or report the limitation. It must never claim that a tool action occurred unless it actually occurred.

## Core lifecycle

**Discover → Specify → Plan → Execute → Verify → Refine → Deliver**

A specification gate separates discovery from implementation. No implementation begins while material requirements remain ambiguous unless the user explicitly authorizes assumptions.

## Repository status

This package is an initial, usable foundation and implementation specification. It is not a claim that the entire proposed future agent/skill catalog has already been built or cross-platform tested. See `docs/FILE-CREATION-PLAN.md`, `docs/SOURCE-TRACEABILITY.md`, and `docs/ACCEPTANCE-TESTS.md`.

## Sources and attribution

PAW uses original, independently written instructions informed by public project documentation and interface concepts. It does not bundle upstream source code, agent prompt files, logos, trademarks, binaries, or assets.

See [`13-REFERENCE/UPSTREAM-SOURCES.md`](13-REFERENCE/UPSTREAM-SOURCES.md) and [`NOTICE.md`](NOTICE.md).

## License

Original PAW-authored text and schemas in this repository are offered under MIT unless a file states otherwise. Referenced upstream projects retain their own licenses. No upstream license is transferred to PAW by reference.
