# Capability matrix

Before a task begins, report availability for each capability:

| Capability | Available? | Evidence |
|---|---|---|
| Web search/browser | Yes / No / Unknown | Tool or user-provided source |
| File upload/read | Yes / No / Unknown | Attached file or connector |
| Repository browsing | Yes / No / Unknown | Accessible URL/tool |
| Code execution | Yes / No / Unknown | Actual execution tool |
| File creation/editing | Yes / No / Unknown | Actual artifact tool |
| External integrations | Yes / No / Unknown | Connected app and permissions |
| Persistent memory | Yes / No / Unknown | Host setting/feature |
| Scheduled/background execution | Yes / No / Unknown | Native feature |
| Multi-agent instances | Yes / No / Unknown | Actual independent agents |
| MCP | Yes / No / Unknown | Configured MCP client/server |

Rules:
1. Unknown is not Yes.
2. A prompt cannot grant a capability.
3. Do not assume one product's features exist in another product.
4. Never claim code was run, a website was opened, a file was written or an integration was invoked unless the host confirms the action.
5. If capability is absent, switch to a transparent fallback.
