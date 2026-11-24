---
name: study-build-check-refine
description: Run an iterative product or software workflow that studies a reference, specifies requirements, builds an authorized implementation, checks it and refines defects.
license: MIT
metadata:
  version: "0.1.0"
  category: product-engineering
  portability: universal
---

# Study → Specify → Build → Check → Refine

## Study
Collect permitted evidence: user requirements, supplied assets, public behavior, documentation and accessible source. Distinguish clean-room observation from authorized artifact analysis.

## Specify
Create functional requirements, non-functional requirements, scope exclusions, design contract, acceptance tests and unresolved questions. Do not build before the specification gate passes.

## Build
Use the available host capabilities. Generate code or instructions only to the extent supported. Do not claim files were edited or applications deployed unless confirmed.

## Check
Compare implementation against each acceptance criterion. Use browser, code execution, screenshots, tests or manual review only when available. Label unexecuted checks.

## Refine
Prioritize defects by severity. Correct, retest and record residual issues. Stop when acceptance criteria pass or when a blocker is documented.

## Deliver
Provide artifacts, instructions, test evidence, limitations and handoff state.
