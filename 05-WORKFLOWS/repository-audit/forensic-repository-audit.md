# Forensic repository audit

**Capability tier:** T1/T2

## Inputs
repository or archive, authority, scope.

## Steps
preserve source → inventory → inspect metadata → validate structure → reconcile → report. At each step, record the actual capability used, evidence IDs, and any blocked work.

## Outputs
manifest, integrity report, risk register.

## Approval gates
Require explicit approval for destructive actions, external publication, credential use, sensitive export, financial/legal submissions, or runtime side effects.

## Exit criteria
The output is traceable, limitations are disclosed, failed and blocked checks are not marked passed, and another host can resume from the recorded state.
