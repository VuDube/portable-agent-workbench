# Release readiness

**Status:** IN PROGRESS; v1.0.0 blocked.

## Passed or evidenced

- Correct public repository owner, name, URL, and default branch.
- Archive readable, SHA-256 recorded, safe extraction completed, and 45-file remote baseline reconciled.
- Universal core, six investigation workflows, schemas, governance, agent and skill catalogues, workflow procedures, adapter documentation, and evaluation records exist.
- Local structural validation passes at commit `290b0723a61eaef379e9425251525836932fbcf8`.
- The dependency-free comprehensive validation runner records 17 PASS, 0 FAIL, 0 BLOCKED, and 0 NOT RUN for its executable local scope.
- GitHub Actions run `45498587981` passed for commit `b579c2c0fb2fdac6020e713f96f8c54d89e55cc8`.
- GitHub secret scanning and secret-scanning push protection are enabled; vulnerability alerts were enabled. Dependabot security-fix activation was unavailable through the current repository API response, while the committed Dependabot configuration remains present.
- Manus partial compatibility evidence was executed on 2026-11-25: 10 repository-backed and host-integration checks passed, with machine-readable and Markdown logs under `11-EVALUATION/REPORTS/`. Native PAW instruction injection, specialist-agent invocation, PAW-native workflow execution, and complete MCP/account coverage remain untested.

## Blocking or pending

- Complete live testing for all eight platform adapters; Manus has only partial coverage and remains blocking.
- Complete manual usability, adversarial, link, schema-instance, and regression test execution.
- Final file-level licence and attribution review after scope freeze.
- Release manifest, version freeze, v1.0.0 tag, GitHub release, and independent final verification.

A v1.0.0 tag must not be created until every critical gate has a recorded result. BLOCKED and NOT RUN are not PASS.
