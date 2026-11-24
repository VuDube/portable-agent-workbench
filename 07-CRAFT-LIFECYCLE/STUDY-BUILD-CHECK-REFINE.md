# Craft-inspired lifecycle adaptation

The upstream Craft Anything project documents a Study → Build → Check → Ready flow, with Clean Room and Deep modes. PAW adapts the workflow while removing mandatory desktop, CLI, Rust, local runtime and coding-agent dependencies.

## Study
Use accessible evidence only. Establish target behavior, scope and constraints.

## Specify (PAW-added gate)
Translate evidence into a finite specification, requirements register and acceptance tests.

## Build
Use the AI host's available artifact or code-generation capabilities. If it cannot write files, provide complete code and precise user-mediated instructions.

## Check
Compare deliverables against acceptance criteria. Record test method and actual result.

## Refine
Fix prioritized defects and repeat checks.

## Ready
Release only when mandatory criteria pass or an explicitly approved exception is recorded.
