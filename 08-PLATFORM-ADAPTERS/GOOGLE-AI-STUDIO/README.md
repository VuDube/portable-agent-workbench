# Google AI Studio adapter

Use PAW's universal instructions as the system instruction in a configured prompt/session when that interface supports it. Keep the canonical agent and skill documents in Markdown; include only relevant context in a session. If using function calling or API-backed tools, define and test the tool schema separately—prompt text does not create a callable function. API-backed workflows may require a Google AI API key and may incur usage costs; therefore they are optional and not part of PAW's zero-cost baseline.

Verify current AI Studio UI, model/tool support, quotas, privacy and regional availability before providing step-by-step setup guidance.

Official documentation: https://ai.google.dev/gemini-api/docs
Status: designed; not PAW-tested.
