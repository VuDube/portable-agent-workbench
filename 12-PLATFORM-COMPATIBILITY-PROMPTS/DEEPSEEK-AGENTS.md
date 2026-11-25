# PAW compatibility investigator — DeepSeek target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Identify whether the target is DeepSeek web, DeepSeek API, an OpenAI-compatible endpoint, or a third-party integration. Record exact model, endpoint class, model revision if exposed, account mode, tool/function support, context handling, and any proxy boundary.

## DeepSeek-specific probes

1. Test system/developer instruction support and record whether the endpoint accepts it or only user messages.
2. Test PAW contract, skill, agent, workflow, and schema fixtures as plain text or files according to the actual target affordance.
3. Request the PAW project-state object and independently validate required fields, status enum, and types.
4. If function/tool calling exists, use a fixed harmless fixture and record actual invocation versus generated JSON or code.
5. Test one fresh-session boundary and one same-session continuation to distinguish context from persistence.
6. Record any JSON instability, refusal, truncation, context, rate, or endpoint compatibility issue observed; do not claim a failure without the raw redacted response.

## Required conclusion

An OpenAI-compatible API shape does not prove ChatGPT compatibility or DeepSeek web compatibility. Keep provider, endpoint, and product conclusions separate.