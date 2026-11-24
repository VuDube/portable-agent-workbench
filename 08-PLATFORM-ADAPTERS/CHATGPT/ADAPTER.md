# ChatGPT adapter

**Status:** documented / unverified

This adapter is a provider-neutral mapping guide, not a claim of live compatibility testing. Follow the host’s current official documentation for setup and privacy.

## Core mapping

1. Load `01-CORE-SYSTEM/UNIVERSAL-OPERATING-CONTRACT.md` where the host accepts system instructions; otherwise paste it at the start of a conversation.
2. Use only the skills, files, tools, memory, and workflows the host visibly supports.
3. Record any capability loss and use the manual T0/T1 fallback.
4. Never place real secrets or sensitive exports into examples.

## Capability status

- Instruction input: unverified on this adapter revision.
- File or project import: unverified.
- Tool access: unverified and host-dependent.
- Agent Skills support: unverified; use the Markdown body manually if unsupported.
- Persistent automation or runtime integrations: optional and unverified.

## Test procedure

Record host name/version, test date, exact steps, observed output, evidence, privacy route, and blocked checks. Do not mark this adapter tested until that record exists.
