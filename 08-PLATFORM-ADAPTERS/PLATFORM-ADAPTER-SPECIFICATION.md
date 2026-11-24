# Platform adapter specification

An adapter maps PAW’s universal core to a host’s actual affordances. It must state the host and version checked, available input/file/tool/runtime features, unsupported features, privacy and data-routing notes, setup steps, portability loss, evidence, and a manual fallback.

Status values are **designed**, **documented**, **partially-tested**, **tested**, or **blocked**. A README or vendor claim is not a compatibility test. The adapter must never claim that a model has tools, memory, scheduling, MCP, or file access unless the host actually exposes and the test records it.

For each capability, use `available`, `partial`, `unverified`, or `unavailable`. Keep system instructions, skills, workflows, schemas, and optional integrations separate.
