# Platform compatibility policy

PAW's canonical distribution is plain Markdown plus optional YAML and JSON metadata. Platform compatibility is assessed by capability, not by brand name.

| Platform | Portable baseline | Optional native integration | Verification status |
|---|---|---|---|
| Google Gemini | Paste instructions; upload supported references; use Skills where available | Gemini Skills and app-specific capabilities | Not independently tested by PAW |
| Google AI Studio | System instructions and manually configured tools | Function calling/API-backed tools | Not independently tested by PAW |
| ChatGPT | Paste instructions; upload knowledge files; use available tools/apps | Product-specific customizations and connectors | Not independently tested by PAW |
| Manus | Task instructions and explicit approval gates | Browser/agent execution where enabled | Not independently tested by PAW |
| Mistral Vibe | Portable Markdown instructions | Agent Skills-compatible workflow | Not independently tested by PAW |
| Qwen | Paste instructions and provide skill text | Depends on the specific Qwen app/client | Not independently tested by PAW |
| DeepSeek | Paste instructions and provide skill text | Depends on the specific DeepSeek app/client | Not independently tested by PAW |
| Agora (newo-ether/Agora) | Import/paste Markdown system prompts and skills where the app supports them | Skills, MCP, Tasks/Loops, web search, memory/RAG, providers, local models | Interface documented; PAW integration not yet tested |

## Status vocabulary

- **Documented:** a public official manual describes the capability.
- **Designed:** PAW provides an adapter guide but has not tested it.
- **Tested:** a named test was run on a specific app version/build and date.
- **Unavailable:** required capability is absent or inaccessible.
- **Unknown:** evidence is insufficient.

Never describe a platform as fully compatible merely because it accepts text.
