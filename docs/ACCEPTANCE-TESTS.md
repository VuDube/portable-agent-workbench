# Acceptance tests

Status values: PASS / FAIL / BLOCKED / NOT TESTED.

## Core requirements
| ID | Test | Acceptance condition | Initial status |
|---|---|---|---|
| AT-001 | Plain prompt portability | Master instructions can be copied as text without requiring a proprietary runtime | Designed; not platform-tested |
| AT-002 | Capability honesty | Missing tools are disclosed and no action is fabricated | Designed; scenario test pending |
| AT-003 | No CLI dependency | All baseline use instructions avoid mandatory terminal commands | Pass by document inspection |
| AT-004 | No VPS/local host dependency | Core prompts and skills work as static files | Pass by architecture inspection |
| AT-005 | No mandatory API | No API key is needed to read/use the instruction library; cloud inference may still require provider access | Pass by architecture inspection |
| AT-006 | Agent Skills format | Each authored skill has valid frontmatter, matching directory name and required fields | Not schema-tested |
| AT-007 | Evidence integrity | Facts, inferences and unknowns are distinguished | Designed; scenario test pending |
| AT-008 | Platform adapter honesty | No platform is marked tested without test record | Pass by document inspection |
| AT-009 | Licensing provenance | No upstream source code/assets copied into initial package | Pass by package construction |
| AT-010 | Agora optionality | Core PAW works without Conch, MCP, Tasks/Loops or remote shell | Pass by architecture inspection |

## Required future platform test record
Record exact product, app version/build, account tier where relevant, device/OS, model/provider, date, test prompt, expected result, actual result, evidence and tester. Unknown build/version means the result cannot establish current platform compatibility.

## Release rule
A v1.0.0 release must pass all P0 tests. Any failed mandatory test blocks release. Not Tested is not Pass.
