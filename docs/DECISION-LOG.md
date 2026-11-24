# Architecture decision log

## ADR-001 — Static, instruction-first distribution
**Decision:** distribute Markdown/YAML/JSON as the baseline.
**Reason:** compatible with ordinary AI chat apps and does not require a runtime.
**Trade-off:** no native autonomous execution is created by the files themselves.

## ADR-002 — Agent Skills as canonical skill package
**Decision:** use `SKILL.md` folders with the official Agent Skills frontmatter requirements.
**Reason:** portable skill convention and progressive disclosure.
**Trade-off:** each host may implement only part of the format.

## ADR-003 — No mandatory CLI, VPS or local host
**Decision:** exclude runtime engines from the baseline.
**Reason:** user hard constraint.
**Trade-off:** native binary analysis, local instrumentation, MCP server hosting and persistent background jobs are optional integrations, not universal features.

## ADR-004 — No upstream source-code copying in initial release
**Decision:** independently author PAW materials and cite upstream projects.
**Reason:** avoids mixing upstream licenses and proprietary/trademarked assets.
**Trade-off:** PAW reproduces methodologies, not upstream engines.

## ADR-005 — Platform adapters are evidence-rated
**Decision:** distinguish designed, documented, tested and unavailable.
**Reason:** prompt acceptance is not proof of tool compatibility.
