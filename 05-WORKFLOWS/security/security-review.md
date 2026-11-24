# Security review

**Capability tier:** T0/T1/T2

## Inputs
architecture, data flows, threat context.

## Steps
identify assets → map boundaries → model abuse → assess controls → prioritise treatment → retest. At each step, record the actual capability used, evidence IDs, and any blocked work.

## Outputs
threat model and security findings.

## Approval gates
Require explicit approval for destructive actions, external publication, credential use, sensitive export, financial/legal submissions, or runtime side effects.

## Exit criteria
The output is traceable, limitations are disclosed, failed and blocked checks are not marked passed, and another host can resume from the recorded state.
