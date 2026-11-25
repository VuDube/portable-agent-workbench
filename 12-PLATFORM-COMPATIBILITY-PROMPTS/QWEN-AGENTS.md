# PAW compatibility investigator — Qwen target

Use `00-COMMON-FORENSIC-PROTOCOL.md` as the controlling protocol, then execute this platform-specific extension.

## Target boundary

Resolve the exact target: Qwen consumer web, Qwen API, Qwen Code/CLI, Alibaba Cloud model service, or another wrapper. Record model/version, endpoint or app build, account tier, region if exposed, file/tool/function support, and context settings.

## Qwen-specific probes

1. Test the actual instruction mechanism and determine whether it is persistent system configuration, a conversation message, a project rule, or unavailable.
2. Test one PAW Markdown fixture and one schema fixture using the target’s real file/import path. Record whether files are parsed, indexed, or only quoted.
3. Request and independently validate PAW project-state JSON. If JSON mode or schema mode is unavailable, record that and use post-validation only.
4. Test one harmless tool/function operation only if the target exposes execution. Distinguish generated commands from commands that actually ran.
5. Test context continuity and any claimed project/memory feature in a fresh session boundary.
6. If the available target is not the declared Qwen product, stop and relabel the test rather than combining product results.

## Required conclusion

Separate Qwen web, Qwen API, Qwen Code, and third-party wrapper evidence. Do not infer PAW compatibility across those products.