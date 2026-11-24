---
name: repository-forensic-audit
description: Perform an evidence-led audit of a Git repository's identity, structure, modules, features, dependencies, workflows, tests, security, licensing and implementation status.
license: MIT
metadata:
  version: "0.1.0"
  category: software-research
  portability: universal
---

# Repository Forensic Audit

## Preconditions
Confirm the canonical repository and authorization. Record accessible branch/revision. State whether the audit is web-only, uploaded-archive-based, connector-based or locally executed.

## Procedure
1. Verify repository owner, name, URL, visibility and license.
2. Record branch, commit or release when visible.
3. Inventory files and directories.
4. Inspect README, architecture, docs, manifests, workflows, tests, security and license files.
5. Map features to implementation locations and tests.
6. Identify dependencies, runtime, compute, credentials, network and hosting requirements.
7. Classify each capability as implemented, partial, experimental, planned, deprecated, external or unknown.
8. Review data flow, permissions, secrets and trust boundaries.
9. Build source-to-feature traceability.
10. Identify missing evidence and audit coverage.
11. Produce prioritized recommendations.

## Required output
Repository identity; scope/coverage; structure; feature matrix; dependency/runtime matrix; security/licensing review; traceability; risks; limitations; acceptance tests.

## Prohibitions
Never claim exhaustive source inspection, test execution or runtime verification unless performed. Do not copy proprietary or third-party material without checking its license and notices.
