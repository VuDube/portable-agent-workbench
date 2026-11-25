# PAW platform compatibility report

**Report date:** 2026-11-25  
**Repository:** [VuDube/portable-agent-workbench](https://github.com/VuDube/portable-agent-workbench)  
**Assessed repository commit:** `40c27d189dc7117336bb3ed40f321c5e62045405`  
**Overall status:** All eight adapters are documented; Manus has partial dated compatibility evidence, while complete live compatibility remains unverified for all eight named platforms.  
**v1.0.0 impact:** The platform-compatibility release gate remains open and blocks a production v1.0.0 label.

## Interpretation of statuses

This report uses the PAW adapter status model rather than treating documentation as test evidence.

- **Documented:** an adapter file and a portable fallback exist in the repository.
- **Test-ready:** the target execution environment is available or can be reached, but the PAW test has not yet been executed and recorded.
- **Partially tested:** some named capabilities have actual dated execution evidence, but the complete adapter scope has not been tested.
- **Tested:** the declared adapter scope has an actual dated test record with host/version, configuration, inputs, expected results, observed results, evidence, and limitations.
- **Release-ready:** tested coverage is complete for the declared scope, no critical compatibility defect remains, and the result is included in release evidence.
- **Blocked:** the test cannot currently be executed because a required environment, permission, credential, application, or other dependency is unavailable.

A platform may be documented and test-ready at the same time. Neither status is equivalent to tested compatibility.

## Readiness matrix

| Platform | Adapter documentation | Execution environment currently available | PAW live test executed | Current adapter status | Readiness level | v1.0.0 gate | Evidence |
|---|---|---:|---:|---|---|---|---|
| ChatGPT | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/CHATGPT/ADAPTER.md`; no live test record |
| Gemini | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/GEMINI/ADAPTER.md`; no live test record |
| Google AI Studio | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/GOOGLE-AI-STUDIO/ADAPTER.md`; no live test record |
| Manus | Yes | Yes, current Manus execution environment | Partial | partially tested | R3 — partially tested | Blocking | `11-EVALUATION/REPORTS/manus-compatibility-test-log.md`; 10 executable checks passed; native PAW behaviours remain untested |
| Mistral Vibe | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/MISTRAL-VIBE/ADAPTER.md`; no live test record |
| Qwen | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/QWEN/ADAPTER.md`; no live test record |
| DeepSeek | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/DEEPSEEK/ADAPTER.md`; no live test record |
| Agora | Yes | Not verified | No | documented | R1 — documented | Blocking | `08-PLATFORM-ADAPTERS/AGORA/ADAPTER.md`; no live test record |

## Platform findings

### ChatGPT

The PAW adapter documentation exists. No authenticated ChatGPT browser session, API execution, desktop runtime, or dated PAW compatibility test was verified in the current evidence set. The platform therefore remains documented only. The required fallback is manual loading of PAW Markdown instructions and manual use of the schemas and workflows.

Required next evidence is a test record covering core-instruction loading, skill activation or manual skill use, structured JSON output, missing-tool fallback, untrusted-input handling, and project-state handoff in the exact ChatGPT configuration being assessed.

### Gemini

The PAW adapter documentation exists. No authenticated Gemini execution session or dated PAW compatibility test was verified in the current evidence set. The platform remains documented only. The required fallback is manual copy-and-paste use of the PAW core, skills, schemas, and workflows.

The test must identify the exact Gemini product, model, account capability, date, file or prompt method, observed structured-output behaviour, and any capability loss.

### Google AI Studio

The PAW adapter documentation exists. No authenticated Google AI Studio session, API call, or dated PAW compatibility test was verified in the current evidence set. The platform remains documented only. Manual Markdown and JSON use remains the fallback.

A valid test must distinguish Google AI Studio web behaviour from Gemini API behaviour. A test of one does not automatically establish compatibility with the other.

### Manus

The Manus adapter documentation exists, and the current environment exposes Manus browser tools and Manus execution capabilities. A dated compatibility run on 2026-11-25 passed 10 executable checks: PAW core/skill/agent/workflow specification loading, project-state required-field validation, local file round-trip, Git remote access, live browser access to the public repository, fallback-contract inspection, and non-execution handling of an untrusted-input fixture. The machine-readable report is `11-EVALUATION/REPORTS/manus-compatibility-test-report.json`; the detailed log is `11-EVALUATION/REPORTS/manus-compatibility-test-log.md`; live browser observations are `11-EVALUATION/REPORTS/manus-observations.json`.

The Manus adapter is therefore **partially tested**, not fully tested. The run did not establish native injection of the PAW core as system/developer instructions, native skill activation, independent specialist-agent invocation, PAW-native workflow execution, native host-enforced structured output, or complete account/MCP permission coverage. Those limitations are explicit in the test report, so the adapter remains blocking for release.

### Mistral Vibe

The PAW adapter documentation exists. No Mistral Vibe application, CLI, API, or authenticated execution environment was verified in the current evidence set. The adapter remains documented only, with copy-and-paste Markdown as the fallback.

Native Vibe compatibility cannot be inferred from generic Markdown compatibility or from another Mistral product.

### Qwen

The PAW adapter documentation exists. No Qwen application, model endpoint, API, or authenticated execution environment was verified in the current evidence set. The adapter remains documented only, with manual PAW instruction and schema use as the fallback.

A future test must identify whether the target is Qwen web, Qwen API, Qwen Code, or another Qwen product because those are not interchangeable compatibility targets.

### DeepSeek

The PAW adapter documentation exists. No authenticated DeepSeek session, API execution, or native runtime was verified in the current evidence set. The adapter remains documented only, with manual Markdown and JSON use as the fallback.

The test must identify the exact DeepSeek product and whether tool calling, file input, structured output, and conversation continuity are available in that configuration.

### Agora

The PAW adapter documentation exists. No Android device, emulator, installed Agora build, authenticated provider configuration, or live PAW import/use test was verified in the current evidence set. The adapter remains documented only.

Agora must be tested as an Android application and not treated as equivalent to a generic Markdown host. A valid test must identify the app version, Android version, import method, skill/prompt handling, archive behaviour, provider configuration, privacy route, and any limitations. No Android-native Agora compatibility claim is currently supported.

## Current gate conclusion

The current matrix supports the following factual conclusion:

**8/8 adapters are documented; 1/8 is partially tested; 0/8 are fully tested; 0/8 are release-ready; 7/8 have no verified execution environment in the current evidence set.** Manus evidence improves the factual status but does not close the platform gate because the declared Manus adapter scope is incomplete and the other seven platforms remain untested.

The local PAW repository and CI validation gates pass within their declared scope. They do not replace platform execution evidence. The platform gate must remain open until the test records described above are executed and reviewed.

## Required test-record fields

Each future platform record must include the platform and exact product name, application or API version, model/provider, account tier where relevant, device and operating system, date and time, PAW commit, adapter revision, test inputs, expected outputs, actual outputs, evidence paths or URLs, privacy/data-routing observations, failed or blocked checks, and reviewer conclusion.

## References

- [PAW platform adapter specification](../08-PLATFORM-ADAPTERS/PLATFORM-ADAPTER-SPECIFICATION.md)
- [PAW platform compatibility matrix](PLATFORM-COMPATIBILITY-MATRIX.md)
- [PAW release readiness](RELEASE-READINESS.md)
- [PAW acceptance results](../11-EVALUATION/ACCEPTANCE-RESULTS.md)
- [PAW known limitations](KNOWN-LIMITATIONS.md)
