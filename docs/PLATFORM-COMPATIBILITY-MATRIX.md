# PAW platform compatibility matrix

This matrix reflects the current verification state as of 2026-11-25. All eight named adapters are documented. None has a formal live PAW compatibility test record. Manus is test-ready because the current execution environment is available, but its adapter has not yet been formally tested.

| Platform | Adapter | Environment | Live PAW test | Readiness | v1.0.0 gate |
|---|---|---|---|---|---|
| ChatGPT | documented | not verified | not executed | R1 — documented | Blocking |
| Gemini | documented | not verified | not executed | R1 — documented | Blocking |
| Google AI Studio | documented | not verified | not executed | R1 — documented | Blocking |
| Manus | documented | current session available | not executed | R2 — test-ready | Blocking |
| Mistral Vibe | documented | not verified | not executed | R1 — documented | Blocking |
| Qwen | documented | not verified | not executed | R1 — documented | Blocking |
| DeepSeek | documented | not verified | not executed | R1 — documented | Blocking |
| Agora | documented | Android runtime not verified | not executed | R1 — documented | Blocking |

**Summary:** 8 documented; 1 test-ready; 0 partially tested; 0 tested; 0 release-ready. The platform gate remains blocking for v1.0.0.

For the full evidence boundary, platform-specific findings, required test-record fields, and machine-readable data, see the [platform compatibility report](PLATFORM-COMPATIBILITY-REPORT.md) and [machine-readable readiness matrix](platform-compatibility-matrix.json).

“Documented” means an adapter file and portable fallback exist. “Test-ready” means the target environment is available but no PAW test has been executed. “Tested” requires an actual dated execution record with host/version, configuration, inputs, expected result, observed result, evidence, and limitations.
