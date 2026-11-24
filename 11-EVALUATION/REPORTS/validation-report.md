# Automated validation report

- Tested commit: `b579c2c0fb2fdac6020e713f96f8c54d89e55cc8`
- Passed: 17
- Failed: 0
- Blocked: 0
- Not run: 0

## STRUCT-agent.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/agent.schema.json`.

## STRUCT-evidence.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/evidence.schema.json`.

## STRUCT-platform-adapter.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/platform-adapter.schema.json`.

## STRUCT-project-state.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/project-state.schema.json`.

## STRUCT-release-manifest.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/release-manifest.schema.json`.

## STRUCT-skill.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/skill.schema.json`.

## STRUCT-test-result.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/test-result.schema.json`.

## STRUCT-workflow.schema — PASS

Parse and inspect JSON Schema Actual: JSON parsed; object schema and required properties present Evidence: `10-SCHEMAS/workflow.schema.json`.

## SKILL-001 — PASS

Validate every skill frontmatter and name Actual: 54 skills checked; failures=0 Evidence: `tools/validators/validate.py`.

## AGENT-001 — PASS

Validate agent identifiers and directories Actual: 48 files; unique_ids=48; failures=0 Evidence: `tools/validators/validate.py`.

## DOC-001 — PASS

Validate internal Markdown links Actual: broken_links=0 Evidence: `tools/validators/run_all.py`.

## DOC-002 — PASS

Detect empty repository files Actual: empty_files=0 Evidence: `tools/validators/run_all.py`.

## SEC-001 — PASS

Scan tracked text for common credential patterns Actual: potential_hits=0 Evidence: `tools/validators/run_all.py`.

## STRUCT-REQUIRED — PASS

Check mandatory repository records exist Actual: missing=[] Evidence: `tools/validators/validate.py`.

## CAT-001 — PASS

Check mandatory agent and skill coverage Actual: agents=48 skills=54 Evidence: `docs/AGENT-CATALOG.md; docs/SKILL-CATALOG.md`.

## REG-001 — PASS

Run repository structural validator Actual: VALIDATION PASSED Evidence: `tools/validators/validate.py`.

## BASE-001 — PASS

Confirm every original baseline file remains present Actual: baseline_present=45/45 Evidence: `archive SHA-256 recorded in docs/BASELINE-AUDIT.md`.

