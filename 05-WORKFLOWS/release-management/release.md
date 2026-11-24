# Release management

**Capability tier:** T1/T2

## Inputs
release candidate, manifest, gates.

## Steps
freeze scope → validate version/licence/security/docs → generate manifest → approval → tag/release → verify. At each step, record the actual capability used, evidence IDs, and any blocked work.

## Outputs
release report and reproducible manifest.

## Approval gates
Require explicit approval for destructive actions, external publication, credential use, sensitive export, financial/legal submissions, or runtime side effects.

## Exit criteria
The output is traceable, limitations are disclosed, failed and blocked checks are not marked passed, and another host can resume from the recorded state.
