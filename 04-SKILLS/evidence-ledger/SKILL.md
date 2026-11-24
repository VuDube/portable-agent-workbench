---
name: evidence-ledger
description: Create and maintain traceable evidence records that distinguish observation, inference, assumption and unknowns.
license: MIT
metadata:
  version: "0.1.0"
  category: research-quality
  portability: universal
---

# Evidence Ledger

For each material claim create:
- `evidence_id`;
- claim;
- source name and URL/path;
- exact locator (heading, line, file, timestamp or screenshot);
- source date/revision;
- observation;
- interpretation;
- confidence;
- limitations;
- verification status.

Keep direct observations separate from conclusions. A source can support an observation without supporting a broader inference. Preserve contradictory evidence. Update or supersede records rather than silently deleting them.

Use statuses: `verified`, `partially_verified`, `unverified`, `contradicted`, `superseded`.
