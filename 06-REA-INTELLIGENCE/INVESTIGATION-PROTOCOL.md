# REA-inspired portable investigation protocol

This is a methodology adaptation, not a replacement for REA's MCP server or native analysis engines.

## Investigation modes
- Observation mode: public/user-visible behavior and supplied screenshots or descriptions.
- Artifact mode: user-supplied files, source, logs, manifests, exports or analysis reports.
- Authorized deep mode: internal analysis only where authorization and actual tools exist.

## Investigation sequence
1. Define target and feature.
2. Define permitted evidence and boundaries.
3. Profile target type and accessible artifacts.
4. Identify relevant components and dependencies.
5. Trace behavior using available evidence.
6. Record evidence and unknowns.
7. Build a behavior/architecture hypothesis.
8. Design tests that could falsify the hypothesis.
9. Validate against observed results.
10. Produce a reconstruction specification.

## Non-portable capabilities
Native decompilation, disassembly, process tracing, packet capture, fuzzing, instrumentation, Ghidra/IDA/Hopper/Kuna automation and deep binary inspection require specialized runtime tools. PAW does not claim these are available through prompts alone.

## Inspired investigation templates
- Feature investigation
- Version comparison
- Reconstruction verification
- Crash investigation
- Residual unknowns audit
- Bounded process experiment design

These correspond conceptually to REA's documented guided workflow categories; PAW's text is independently authored.
