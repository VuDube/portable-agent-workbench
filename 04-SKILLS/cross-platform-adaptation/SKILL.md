---
name: cross-platform-adaptation
description: Adapt a PAW prompt, agent or skill to an AI application while preserving intent and documenting feature and tool limitations.
license: MIT
metadata:
  version: "0.1.0"
  category: interoperability
  portability: universal
---

# Cross-platform Adaptation

1. Identify the exact app, client, version/build and account tier if known.
2. Consult its current official documentation.
3. Determine supported instruction fields, files, skills, tools, memory, automation and context limits.
4. Map the canonical PAW content to the host's supported format.
5. Preserve required instructions; do not silently truncate.
6. Move optional reference material to files if supported.
7. Remove unsupported tool calls and replace them with explicit user-mediated steps.
8. Identify privacy, data-routing and retention implications.
9. Test a representative task.
10. Record date, build, test case, result and known limitations.

Do not equate text prompt acceptance with tool or workflow compatibility.
