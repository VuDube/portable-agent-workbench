# PAW compatibility investigator — Gemini target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Identify whether the target is Gemini consumer web, Gemini API, Google AI Studio, or another Google product. Do not merge results across them. Record model name/version, API or UI mode, account tier if exposed, file modality, tool/function mode, structured-output mode, and safety settings relevant to the test.

## Gemini-specific probes

1. Test the actual system-instruction or equivalent instruction channel. If the selected Gemini surface has no such channel, record the limitation and use the lowest safe fallback.
2. Test one PAW Markdown file and one JSON schema as supplied inputs. Record whether they are uploaded, indexed, parsed, or merely included in the prompt.
3. Request the project-state fixture in the exact structured-output mode exposed by the target; validate it against the PAW schema outside the model.
4. Test one harmless function/tool call only when the target visibly exposes it. Record the tool declaration, invocation, returned fixture, and whether execution occurred on-host or externally.
5. Test context continuity in a fresh conversation and in the same conversation separately. Do not infer persistent memory from ordinary context retention.
6. Record any file-size, context-window, safety-filter, rate, or model-availability limitation actually observed.

## Required conclusion

Separate Gemini web, Gemini API, and Google AI Studio claims. A successful prompt response is not evidence of native Agent Skills, specialist-agent execution, or PAW workflow execution.