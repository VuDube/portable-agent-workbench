# Product specification

## Product
Portable Agent Workbench (PAW): a platform-independent instruction, agent, skill and workflow library.

## Goals
1. Reuse proven patterns from Agency Agents, REA, Craft Anything and Agora without requiring their native runtimes.
2. Make universal instructions and skill files usable in ordinary AI chat apps.
3. Support optional native tools where a host provides them.
4. Maintain evidence traceability, safety, privacy, licensing and QA controls.
5. Provide no-terminal, no-VPS, no-local-hosting and no-mandatory-API baseline operation.

## Non-goals
- Reimplement REA's native binary analysis engines.
- Reimplement Craft Anything's 300+ inspection tools.
- Fork or build the Agora Android application.
- Guarantee equal tool capabilities across AI providers.
- Provide autonomous background execution where the host does not.
- Guarantee unlimited zero-cost model inference.

## Functional requirements
- FR-001 Universal operating instructions.
- FR-002 Capability detection and fallback.
- FR-003 Master orchestration and work-package planning.
- FR-004 Specialist agent definitions.
- FR-005 Agent Skills-compatible modular skills.
- FR-006 Evidence ledger and source traceability.
- FR-007 Research and repository audit workflows.
- FR-008 Study/specify/build/check/refine workflow.
- FR-009 Platform adapter documentation.
- FR-010 Project-state continuity template.
- FR-011 QA and acceptance tests.
- FR-012 Licensing/provenance register.

## Non-functional requirements
- NFR-001 Plain-text baseline.
- NFR-002 No mandatory CLI/terminal/VPS/local server.
- NFR-003 No mandatory API key or paid service.
- NFR-004 Progressive disclosure.
- NFR-005 Clear capability and verification status.
- NFR-006 Least-privilege and human approval for consequential actions.
- NFR-007 Maintainable naming, versioning and schemas.
- NFR-008 No unsupported claims of platform testing.

## Release gate
v1.0.0 requires all P0 artifacts, all mandatory schema checks, representative cross-platform tests on declared app versions, a license/provenance review and a complete known-limitations register.
