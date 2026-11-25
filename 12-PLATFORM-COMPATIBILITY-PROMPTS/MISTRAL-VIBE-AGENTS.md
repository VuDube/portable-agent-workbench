# PAW compatibility investigator — Mistral Vibe target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Identify the exact Mistral Vibe product/build and whether it is a CLI, desktop runtime, hosted coding agent, or wrapper. Record executable version, model/provider configuration, working directory, operating system, sandbox permissions, and authentication state without exposing credentials.

## Vibe-specific probes

1. Verify whether `AGENTS.md`, Markdown instructions, repository rules, or equivalent files are actually discovered by the runtime. Record the path and observed loading evidence.
2. Test read-only repository inspection first. Test file creation only inside a temporary fixture directory and clean it up afterward.
3. Run one bounded, non-destructive command only if shell execution is visibly enabled. Capture exit code and stdout/stderr; never infer execution from a proposed command.
4. Test PAW skill, agent, and workflow files as repository instructions and distinguish file discovery from native role/workflow execution.
5. Validate a structured JSON output externally. Record whether the CLI has native schema enforcement or whether validation was performed by a separate script.
6. If no Vibe executable, runtime, or permission is available, mark runtime tests `BLOCKED` rather than substituting a generic Mistral API or another coding agent.

## Required conclusion

Do not generalize from Mistral API behaviour to Vibe. Report filesystem, shell, repository, instruction-discovery, and native orchestration evidence separately.