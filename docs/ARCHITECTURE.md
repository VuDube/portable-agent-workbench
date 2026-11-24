# PAW architecture

PAW follows this portability chain:

**Universal core → modular agents → reusable skills → workflows → schemas and templates → platform adapters → optional execution integrations.**

The universal core contains provider-neutral instructions, evidence rules, approval rules, and output contracts. Agents add distinct specialist perspectives. Skills package reusable instructions using the Agent Skills `SKILL.md` convention. Workflows compose agents and skills into ordered procedures. Schemas and templates make state and evidence portable. Adapters describe host-specific setup and capability loss without redefining the core.

## Capability tiers

- **T0 instruction-only:** text instructions, manual checklists, and structured output guidance.
- **T1 file-enabled:** reading and writing project files, schemas, reports, and templates.
- **T2 tool-enabled:** web, repository, application, or data tools that must actually be available and called.
- **T3 runtime-dependent:** MCP, persistent automation, local models, native analysis, or other external runtimes.

A document may describe a higher-tier option, but it must state the prerequisite and provide a lower-tier fallback where practical.

## Evidence model

PAW distinguishes observation, derived fact, inference, decision, and unknown. Every material conclusion should identify its source, scope, confidence, limitations, and unresolved questions. Absence of evidence is not evidence of absence when coverage is incomplete.

## Execution model

PAW documents procedures and contracts. A host model may perform role-based passes or may have true independent agents; documentation must state which occurred. Written workflows never imply that native reverse engineering, browsing, scheduling, or external side effects happened without a corresponding tool result.
