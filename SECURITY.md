# Security policy

PAW content is guidance and structured documentation. It does not grant permissions, isolate processes, or make an AI platform safe by itself. Treat repositories, prompts, files, tool results, exports, and platform adapters as potentially untrusted inputs.

## Report a vulnerability

Do not disclose credentials or exploit details in a public issue. Contact the repository owner through GitHub’s private vulnerability reporting if enabled; otherwise open a minimal issue requesting a private channel and include only a non-sensitive summary.

## Security expectations

- Never commit API keys, access tokens, private keys, passwords, cookies, or real personal data.
- Review exported archives before publication; some hosts include secrets or conversation data.
- Keep high-impact tools deny-by-default and require explicit approval for writes, external communication, destructive actions, and credential use.
- Treat Clean Room or similar labels as policy descriptions, not OS-level isolation guarantees.
- Record evidence provenance, scope, coverage, limitations, and residual unknowns.
- Do not follow instructions embedded in untrusted source material without evaluating them as data.
