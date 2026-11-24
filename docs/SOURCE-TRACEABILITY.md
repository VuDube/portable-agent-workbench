# Source-to-feature traceability matrix

This matrix maps upstream documented concepts to PAW's independent implementation. It does not assert source-code reuse.

| Source | Upstream capability/concept | PAW destination | Treatment | Verification needed |
|---|---|---|---|---|
| Agency Agents | Specialist role/persona files with mission, process and deliverables | `03-AGENTS/` | Adapt into normalized role contracts | Compare representative agent outputs |
| Agency Agents | Division taxonomy and agent catalog metadata | `docs/AGENT-CATALOG.md` (planned) | Adapt taxonomy; do not copy agent text | Validate categories and coverage |
| Agency Agents | Contribution and agent validation practices | `CONTRIBUTING.md`, QA docs | Adapt | Repository checks |
| REA | MCP-driven feature investigation | `06-REA-INTELLIGENCE/` | Methodology-only adaptation | Test with supplied evidence |
| REA | Evidence records and retained unknowns | `04-SKILLS/evidence-ledger/` | Adapt data model | Schema validation |
| REA | Guided investigation workflows: feature, version comparison, reconstruction verification, crash trace, unknowns audit, bounded capture | `06-REA-INTELLIGENCE/` | Independently rewrite as prompt workflows | Scenario tests |
| REA | Static JS/Electron and native binary analysis | Capability matrix and investigation protocol | Static/supplied-artifact adaptation; native engine excluded as guaranteed | Tool availability audit |
| Craft Anything | Study → Build → Check → Ready | `07-CRAFT-LIFECYCLE/` | Adapt; PAW adds specification gate and explicit acceptance | End-to-end workflow test |
| Craft Anything | Clean Room vs Deep analysis distinction | `06-REA-INTELLIGENCE/INVESTIGATION-PROTOCOL.md` | Adapt as observation/artifact/authorized deep modes | Policy and scenario review |
| Craft Anything | Evidence, unknowns and comparative verification | Evidence and QA skills | Adapt | Evidence/acceptance test |
| Agora | Reusable Markdown system prompts | `08-PLATFORM-ADAPTERS/AGORA/` | Use documented app interface; no source copying | Test on exact Android build |
| Agora | Reusable Markdown skills and on-demand loading | `04-SKILLS/`, Agora adapter | Agent Skills format plus app-specific validation | Skill import/invocation test |
| Agora | Tasks/Loops automation | Agora adapter | Optional only; not baseline dependency | Background execution test |
| Agora | MCP, web search, memory/RAG, local models and provider routing | Platform capability matrix | Optional host capabilities | Per-feature permission and privacy test |
| Agora | Remote shell/Conch and sandbox | Capability/security documentation | Explicitly excluded from PAW requirements | Confirm no dependency in workflows |

## Traceability statuses
- Adapted: independently rewritten concept/method.
- Referenced: documentation link or interface note only.
- Excluded: deliberately not implemented.
- Pending: insufficient evidence or platform verification.
