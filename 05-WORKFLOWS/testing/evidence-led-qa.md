# Evidence-led QA

**Capability tier:** T1/T2

## Inputs
candidate artefact, requirements, test cases.

## Steps
select tests → execute available checks → record evidence → classify failures/blockers → retest. At each step, record the actual capability used, evidence IDs, and any blocked work.

## Outputs
test report, defects, residual risk.

## Approval gates
Require explicit approval for destructive actions, external publication, credential use, sensitive export, financial/legal submissions, or runtime side effects.

## Exit criteria
The output is traceable, limitations are disclosed, failed and blocked checks are not marked passed, and another host can resume from the recorded state.
