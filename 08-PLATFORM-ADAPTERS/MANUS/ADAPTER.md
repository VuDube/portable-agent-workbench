# Manus adapter

**Status:** partially tested

This adapter remains provider-neutral. The current Manus Sandbox has now been tested for repository-backed PAW loading, local file round-trip, Git remote access, live browser access, fallback documentation, and non-execution handling of an untrusted-input fixture. This is partial evidence, not a claim of complete native PAW compatibility.

## Core mapping

1. Load `01-CORE-SYSTEM/UNIVERSAL-OPERATING-CONTRACT.md` where the host accepts system instructions; otherwise paste it at the start of a conversation.
2. Use only the skills, files, tools, memory, and workflows the host visibly supports.
3. Record any capability loss and use the manual T0/T1 fallback.
4. Never place real secrets or sensitive exports into examples.

## Capability status

- Instruction input: not tested as native system/developer injection; core contract file loading passed.
- File or project import: local file round-trip and repository access passed; native project import not tested.
- Tool access: browser navigation/view and Git remote access passed; broader tool permissions remain host-dependent.
- Agent Skills support: PAW skill discovery/loading passed; native automatic skill activation not tested; use the Markdown body manually if unsupported.
- Specialist-agent invocation: not tested; agent specification loading passed.
- Workflow execution: not tested by a PAW-native runner; workflow procedure loading passed.
- Structured output: local instance was checked against the PAW project-state required fields; native host enforcement was not tested.
- Persistent automation or runtime integrations: optional and unverified.

## Test procedure

The dated record for this partial result is `11-EVALUATION/REPORTS/manus-compatibility-test-log.md` with machine-readable detail in `11-EVALUATION/REPORTS/manus-compatibility-test-report.json` and live browser observations in `11-EVALUATION/REPORTS/manus-observations.json`. The record identifies the host as Manus Sandbox, records the PAW baseline commit, inputs, expected and actual results, evidence paths, limitations, and untested native behaviours. Do not promote this adapter to tested or release-ready until the remaining native instruction, specialist-agent, workflow, and broader MCP/account checks have actual evidence.
