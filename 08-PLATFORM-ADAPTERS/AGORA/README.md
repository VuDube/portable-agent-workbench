# Agora adapter — newo-ether/Agora

Official repository: https://github.com/newo-ether/Agora  
User manual: https://newo-ether.github.io/Agora/

## Product profile

Agora is an Android BYOK client for provider-hosted and on-device models. Its documented capabilities include reusable system prompts, Markdown skills, web search, memory, conversation search/RAG, MCP servers, Tasks/Loops automation, local models, image generation and optional remote shell/file tools.

## PAW usage strategy

1. Keep PAW's canonical agent and skill files in the GitHub repository.
2. Use Agora's supported system-prompt configuration for the compact universal operating instructions when appropriate.
3. Add PAW skills through Agora's supported skill-management/import path only after confirming the installed app version's current workflow.
4. Keep individual skills focused; allow the model to read a skill on demand rather than injecting the entire library into every request.
5. Use Tasks/Loops only for explicitly requested repeatable or scheduled workflows and verify background execution/permission settings.
6. Use web search, MCP, RAG and memory only when enabled and necessary.
7. Prefer no-shell workflows. Do not configure Conch, SSH, remote shell, PRoot or local server as a PAW prerequisite.

## Capability caveats

- Agora is an Android app; its app features do not transfer to Gemini, ChatGPT or other clients.
- Provider/API credentials may be required for cloud models. PAW itself does not require an API key, but a user's chosen cloud provider may.
- Local models can avoid remote inference credentials but require compatible device resources and model storage; no performance guarantee is made.
- MCP requires an actual compatible server and user configuration. PAW does not ship one.
- Tasks/Loops and background execution depend on app settings, Android restrictions and the current build.
- Do not put secrets in PAW Markdown files or GitHub.
- Agora's `.agora` export can contain sensitive information; review export contents before sharing.

## Licensing boundary

Do not copy Agora application source into PAW. Current Agora releases v2.2.0+ are GPL-3.0; historical v2.1.0 and earlier are MIT. Recheck upstream LICENSE before any code reuse. This adapter is documentation only and does not imply endorsement.
