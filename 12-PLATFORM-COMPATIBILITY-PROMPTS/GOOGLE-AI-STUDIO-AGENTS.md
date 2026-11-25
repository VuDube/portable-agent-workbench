# PAW compatibility investigator — Google AI Studio target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Test Google AI Studio itself, or explicitly identify the API/exported configuration if that is what is being tested. Record the Studio interface or API version, selected Gemini model, project/account context without secrets, generation settings, file handling, structured-output controls, and tool/function settings.

## Studio-specific probes

1. Verify whether PAW core instructions can be placed in the target’s system-instruction field or only in user content.
2. Upload or attach the PAW contract, one skill, one agent specification, one workflow, and one schema only if the interface exposes that operation. Record filenames, displayed parsing/indexing state, and actual accessibility.
3. Run a structured project-state request and validate the response independently. Record whether schema enforcement is native or post-validated.
4. If Studio exposes code execution, tools, grounding, or function calls, test only a fixed harmless fixture and identify whether it actually ran. Do not treat a generated code block as execution.
5. Check whether a new chat loses prior PAW context and whether saved prompts/projects are available in the tested account. Record visibility, not assumptions.
6. Record export/API parity limits: Studio behaviour must not be generalized to a separately exported API integration.

## Required conclusion

Report Studio UI evidence and Gemini API evidence in separate sections. Native skills, agents, workflows, MCP, and persistence are `unverified` unless directly demonstrated.