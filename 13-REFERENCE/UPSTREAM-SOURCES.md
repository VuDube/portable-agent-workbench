# Upstream sources and official documentation

Accessed for this blueprint on 2026-11-24. Recheck before release because repository contents and platform interfaces change.

## Repositories
- Agency Agents: https://github.com/msitarzewski/agency-agents
- REA: https://github.com/morluto/rea
- Craft Anything: https://github.com/storytold/craft-anything
- Agora: https://github.com/newo-ether/Agora

## Important technical references
- Agent Skills specification: https://agentskills.io/specification
- REA guided MCP workflows: https://github.com/morluto/rea/blob/main/docs/getting-started/mcp-prompts.md
- Craft Anything tool catalog: https://github.com/storytold/craft-anything/blob/main/docs/tools.md
- Agora user manual: https://newo-ether.github.io/Agora/
- Agora system prompts: https://newo-ether.github.io/Agora/system-prompts/
- Agora skills: https://newo-ether.github.io/Agora/skills/
- Agora agentic tools: https://newo-ether.github.io/Agora/tools/
- Agora automation: https://newo-ether.github.io/Agora/automation/
- Agora MCP: https://newo-ether.github.io/Agora/mcp/
- Agora privacy: https://newo-ether.github.io/Agora/privacy/
- Gemini Skills transition: https://support.google.com/gemini/answer/18560919
- OpenAI custom GPT migration/retirement: https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq
- Mistral Vibe: https://docs.mistral.ai/vibe
- Manus: https://manus.im/docs

## Important findings
- Agency Agents uses a specialist persona model and a division/catalog structure; its current repository identifies MIT licensing.
- REA uses MCP plus guided investigation prompts, evidence records and tool/provider integrations; native binary analysis may require external analysis engines. REA-authored code is MIT; third-party materials have separate terms.
- Craft Anything documents a Study/Build/Check/Ready lifecycle, Clean Room and Deep modes, and hundreds of native tools. Its repository states MIT OR Apache-2.0, with separate asset/trademark notices.
- Agora is an Android BYOK application with provider integrations, system prompts, Markdown skills, MCP, automation, memory/RAG, local models and optional remote execution. Current releases v2.2.0+ are GPL-3.0; earlier v2.1.0 releases are MIT.
- The Agent Skills specification requires a skill directory containing `SKILL.md`; `name` and `description` are required frontmatter fields, and the name must match the directory name.

This source register records the sources reviewed for the blueprint, not a claim that every source file in every repository has been exhaustively inspected.
