# Quick start

## Universal use

1. Open the AI application you intend to use.
2. If it offers a system-instructions field, paste `01-CORE-SYSTEM/MASTER-SYSTEM-INSTRUCTIONS.md` there. Otherwise paste it as the first message in a new conversation.
3. Paste or invoke `02-MASTER-ORCHESTRATION/MASTER-ORCHESTRATOR.md` for complex tasks.
4. Provide the task, objective, constraints, available inputs and desired deliverables.
5. The AI must first state which capabilities it actually has in this session.
6. Activate only the skills relevant to the task.
7. Keep a project-state note when the work spans multiple conversations.

## No-terminal rule

Do not follow upstream installation commands such as `npx`, `npm`, shell scripts, Rust builds, Android Studio builds, or local MCP server setup as a required PAW installation step. Such integrations may be described as optional upstream capabilities, but PAW's baseline operation must not depend on them.

## What the host must provide

- Web research requires a browser/search capability or user-supplied sources.
- File inspection requires file upload or connected file access.
- Code execution requires an available execution environment.
- Persistent automation requires native automation support.
- MCP requires a host that supports MCP and user-authorized server configuration.

If unavailable, provide an instruction-only or supplied-artifact alternative and mark what remains unverified.
