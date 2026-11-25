# PAW compatibility investigator — ChatGPT/OpenAI API target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Test the exact OpenAI API-compatible endpoint and model actually configured. Do not call the result a ChatGPT web-app result unless the consumer ChatGPT application itself is the target. Record base URL class, model identifier, API response metadata, tool/function support, structured-output support, and any proxy or sandbox boundary visible to you. Never expose the API key.

## API-specific probes

1. Send one minimal request with the PAW core contract as the system/developer instruction and a deterministic test request. Record whether the endpoint accepts that instruction channel.
2. Repeat with a PAW skill excerpt and a specialist-agent specification. Distinguish “the model followed text in a prompt” from “the platform activated a native skill/agent.”
3. Request the PAW project-state fixture using the endpoint’s documented structured-output mechanism, then validate the returned JSON locally against `10-SCHEMAS/project-state.schema.json`.
4. If tool calling is exposed, use only a harmless fixture tool that returns a fixed value. If it is not exposed, run and record the manual fallback instead; do not emulate a tool call.
5. Test a multi-turn handoff with a project-state object and check whether continuity exists only in the request payload or is retained by the host.
6. Record truncation, refusal, rate-limit, timeout, retry, token-limit, and malformed-JSON behaviour if any occurs naturally. Do not create load or abuse traffic.

## Required conclusion

Report separately: API prompt compatibility; API file/fixture compatibility; structured-output reliability; tool-call compatibility; native ChatGPT web compatibility; and native agent/skill/workflow compatibility. Mark web/native items `NOT RUN` unless the web application was actually tested.