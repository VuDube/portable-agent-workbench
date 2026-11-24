# Contributing to PAW

PAW is an instruction-first, provider-neutral workbench. Contributions should improve portability, evidence quality, safety, usability, or maintainability without making a proprietary runtime mandatory.

## Before opening a change

Read the [product specification](docs/PRODUCT-SPECIFICATION.md), [architecture](docs/ARCHITECTURE.md), [security policy](SECURITY.md), and [licence review](docs/LICENCE-AND-ATTRIBUTION-REVIEW.md). For new agents, skills, workflows, or adapters, record the intended capability tier and validation status.

## Contribution rules

- Do not commit secrets, personal data, provider keys, private exports, or unreviewed third-party material.
- Keep universal instructions separate from platform-specific adapters.
- Do not claim that a tool, platform, agent, or workflow was tested unless the test was actually run and recorded.
- Prefer original methodology over copied upstream prompt or source files.
- Add or update an acceptance test for material behaviour.
- Keep identifiers stable and document breaking schema changes.

## Pull requests

Describe the requirement addressed, files changed, evidence collected, tests run, limitations, and any licensing or security implications. A maintainer may request a provenance note or a manual portability review.

## Adding content

New skills must use a directory whose name matches the `name` in `SKILL.md`. New agents and workflows must declare inputs, outputs, limitations, capability tier, approval points, and at least one evaluation case.
