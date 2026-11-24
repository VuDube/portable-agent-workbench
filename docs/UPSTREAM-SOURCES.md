# Upstream sources

This record captures a source-level review performed on 2026-11-24. Recommendations are independently authored for PAW. PAW does not bundle upstream source code, prompt files, logos, or assets.

## Agency Agents

- URL: https://github.com/msitarzewski/agency-agents
- Inspected revision: `8ae6164602c95ca78828b148b9052460ee426885` on `main`; no tagged release was verified.
- Licence: MIT.
- Inspected: `README.md`, `divisions.json`, `CONTRIBUTING.md`, `LICENSE`, `scripts/check-divisions.sh`, a representative engineering agent, and repository metadata.
- Verified finding: `divisions.json` is the division source of truth. The inspection counted 18 divisions. `integrations/`, `examples/`, `scripts/`, and `strategy/` are supporting namespaces, not official divisions.
- PAW use: maintain a first-class registry, distinguish catalog metadata from operational text, require distinct agent scope, and pin any imported material by SHA.

## REA — Reverse Engineer Anything

- URL: https://github.com/morluto/rea
- Inspected revision: `e896f60540f03e2c1fe0f916412bddd656c1f296`; package version `6.10.1`.
- Licence: MIT for REA-authored code; external analysis tools retain their own terms.
- Inspected: README, licence, package metadata, MCP contracts, prompts, supported targets, limits, tool-design guidance, evidence server and evidence ledger implementation.
- Verified finding: REA separates evidence identity, coverage, limitations, residual unknowns, and provider/session context. It documents six guided workflows: investigate feature, compare application versions, verify reconstruction, trace crash, audit residual unknowns, and prepare bounded process capture.
- PAW use: reproduce the methodology as instruction-based workflows, never claim REA’s MCP or native engines are included, and make runtime effects and limits explicit.

## Craft Anything

- URL: https://github.com/storytold/craft-anything
- Inspected revision: `b8dd88cf7181c020f114aaf23d5bb44808eb5b96`; no release/version was independently verified.
- Licence: MIT OR Apache-2.0 for repository work; bundled assets and brand materials retain separate terms.
- Inspected: README, tool catalogue, Claude integration, status, MIT/Apache licences, NOTICE, and ATTRIBUTION.
- Verified finding: the UI presents Study → Build → Check → Ready, with refinement described as an iterative action. Clean Room limits what the application/agent may inspect but is explicitly not an OS sandbox.
- PAW use: model Refine as a first-class state transition, separate policy from containment, and maintain file-level attribution inventories.

## Agora

- URL: https://github.com/newo-ether/Agora
- Inspected revision: `6f22c79304c9367e0fae271d0e4408a834da13c0` on `master`; v2.2.0 tag peeled to `801e844042af47f38b76c9f075cb1d66c419d755`.
- Licence: current repository GPL-3.0; the project documents v2.1.0 and earlier as MIT.
- Inspected: README, ARCHITECTURE, PRIVACY, current and historical licences, and official manual pages for prompts, skills, tools, automation, MCP, context, memory, providers, import/export, and privacy.
- Verified finding: Agora is an Android BYOK client with local storage, provider adapters, skills, MCP, tasks/loops, memory, context compaction, and versioned archive import/export. Current exports may contain unencrypted secrets if the user opts in.
- PAW use: preserve provider-neutral schemas, capability firewalls, bounded loops, measured context, explicit routing/privacy, and version-specific licence boundaries.

## Agent Skills specification

- URL: https://agentskills.io/specification
- Inspected repository revision: `83021e2be457a9b6679148719c1f6074f0ad975e`; reference package `skills-ref` version `0.1.0`.
- Licence: repository code Apache-2.0; repository README states documentation is CC-BY-4.0.
- Verified finding: a skill is a directory containing `SKILL.md` with YAML frontmatter requiring `name` and `description`; the name must match its parent directory and progressive disclosure is the intended loading model.
- PAW use: validate naming and frontmatter, keep discovery metadata small, load bodies and resources on activation, and treat optional fields as capability-sensitive.

## Research boundary

This is not a complete legal audit, live compatibility test, or end-to-end execution test of any upstream project. It records the inspected files and exact revisions so future work can repeat or update the review.
