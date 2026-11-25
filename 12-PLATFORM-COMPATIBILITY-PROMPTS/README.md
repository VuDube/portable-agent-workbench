# PAW platform compatibility forensic prompt set

This directory contains one common evidence protocol and one platform-specific investigator prompt for each named PAW platform. These are designed to be pasted into the target host, saved as `AGENTS.md` where that host actually supports repository instruction files, or supplied as a controlled task prompt where it does not.

## Files

- `00-COMMON-FORENSIC-PROTOCOL.md` — mandatory evidence, safety, status, and reporting contract.
- `CHATGPT-OPENAI-API-AGENTS.md` — OpenAI API target; do not generalize to consumer ChatGPT web.
- `GEMINI-AGENTS.md` — exact Gemini web/API target; do not merge with Google AI Studio.
- `GOOGLE-AI-STUDIO-AGENTS.md` — Google AI Studio target; do not generalize to exported Gemini API behaviour.
- `MISTRAL-VIBE-AGENTS.md` — Mistral Vibe CLI/desktop/runtime target.
- `QWEN-AGENTS.md` — exact Qwen web/API/Code target.
- `DEEPSEEK-AGENTS.md` — exact DeepSeek web/API target.
- `MANUS-AGENTS.md` — Manus host and task-runtime target.
- `AGORA-AGENTS.md` — exact Agora Android application target.

## Immediate execution procedure

1. Select exactly one platform file and copy it together with the common protocol and the PAW repository or required PAW fixtures into the target platform.
2. Identify the exact product and execution mode before testing. Do not combine web, API, CLI, mobile, and studio results.
3. Ask the target to execute the protocol, not merely summarize the adapter documentation.
4. Require both the Markdown forensic report and the machine-readable JSON report. If the host cannot create files, require fenced blocks with exact filenames.
5. Require raw or redacted evidence locators for every `PASS` and `FAIL`. A conclusion without evidence is not a compatibility record.
6. Return the complete report set to the PAW maintainer without editing the PAW compatibility matrix automatically.

## Evaluation rule

A platform-generated forensic report is **necessary evidence but not self-authenticating proof**. The PAW maintainer must independently inspect the underlying transcript, screenshots, tool results, API metadata, command output, or device records. The report may update PAW only when:

- the exact target identity is clear;
- the host actually executed the declared test;
- the evidence supports the claimed capability;
- missing, blocked, and not-run checks are explicit;
- the result is reproducible or the non-repeatability is disclosed;
- secrets and personal data are removed; and
- the capability status is updated narrowly rather than globally.

The prompts intentionally prohibit guarantees. They can improve evidence quality and reduce hallucinated compatibility claims, but no prompt can guarantee that another model will execute honestly, that a platform exposes a capability, or that a generated report is true without review of its evidence.

## Suggested returned filenames

- `<platform>-paw-forensic-report.md`
- `<platform>-paw-forensic-report.json`
- `<platform>-paw-evidence/` for screenshots, redacted transcripts, API metadata, command logs, or device records
