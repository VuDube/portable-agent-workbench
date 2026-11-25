# PAW platform compatibility matrix

This matrix reflects the current verification state as of 2026-11-25. All eight named adapters are documented. Manus now has a dated partial PAW compatibility record for repository-backed loading and host operations, but its complete native adapter scope remains untested.

| Platform | Adapter | Environment | Live PAW test | Readiness | v1.0.0 gate |
|---|---|---|---|---|---|
| ChatGPT | documented | not verified | not executed | R1 — documented | Blocking |
| Gemini | documented | not verified | not executed | R1 — documented | Blocking |
| Google AI Studio | documented | not verified | not executed | R1 — documented | Blocking |
| Manus | partially tested | current session available | partial: 10 executable checks passed | R3 — partially tested | Blocking |
| Mistral Vibe | documented | not verified | not executed | R1 — documented | Blocking |
| Qwen | documented | not verified | not executed | R1 — documented | Blocking |
| DeepSeek | documented | not verified | not executed | R1 — documented | Blocking |
| Agora | documented | Android runtime not verified | not executed | R1 — documented | Blocking |

**Summary:** 7 documented; 0 test-ready; 1 partially tested; 0 tested; 0 release-ready. The platform gate remains blocking for v1.0.0 because native PAW instruction injection, specialist-agent invocation, workflow execution, and broader MCP/account coverage remain unproven.

For the full evidence boundary, platform-specific findings, required test-record fields, and machine-readable data, see the [platform compatibility report](PLATFORM-COMPATIBILITY-REPORT.md) and [machine-readable readiness matrix](platform-compatibility-matrix.json).

“Documented” means an adapter file and portable fallback exist. “Test-ready” means the target environment is available but no PAW test has been executed. “Partially tested” means some declared capabilities have dated evidence but the adapter scope is incomplete. “Tested” requires an actual dated execution record with host/version, configuration, inputs, expected result, observed result, evidence, and limitations for the declared scope.
