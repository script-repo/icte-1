# Writing rules

Extract of ICTE-1 section 3. These are proposed conventions, not quotations from ASD-STE100.

Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md). If this file disagrees with the specification, the specification wins.

A required rule fails the language result when the document breaks it and records no exception. An advisory rule is reported. An advisory miss does not fail the language result.

L04 applies to procedural and descriptive sentences in the document under review. It does not apply to tables, identifiers, or quoted source material in the specification.

## Language and structure

| ID | Severity | Proposed rule | Example |
|---|---|---|---|
| L01 | required | Use one preferred term for each concept within a document. | Do not use node as a synonym for hypervisor host. State the cluster type when you use node. |
| L02 | required | Name the actor when responsibility matters. | The GitOps controller applies the configuration. |
| L03 | required | Give one action per procedural step. | Create the namespace. Then apply the policy in a separate step. |
| L04 | advisory | Target 20 words per procedural sentence and 25 words per descriptive sentence. | Split a long sentence. Do not remove a condition to meet the target. |
| L05 | required | Put the condition before the action. | If the health check fails, stop the rollout. |
| L06 | required | Use active voice for instructions. | The operator runs the validation job. |
| L07 | required | Replace an ambiguous pronoun with the component name. | The gateway forwards the request to the inference server. |
| L08 | required | Use a numbered list for a sequence and bullets for an unordered set. | Separate deployment steps from prerequisites. |
| L09 | required | Expand an acronym at its first use, unless the document defines an assumed vocabulary. | Recovery point objective (RPO). |
| L10 | required | Preserve a literal identifier exactly. | Write `spec.replicas`, not a paraphrased configuration key. |
| L11 | required | Do not use a synonym only to avoid repetition. | Repeat deployment when that is the intended action. |
| L12 | required | Do not invent a missing value, prerequisite, or expected result. | Mark an unspecified timeout as `TBD`. |
| L13 | required | Put the warning immediately before a destructive action. | State the impact. Then upgrade the host. |

## Requirement language

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Do not use shall. Do not use will to imply a guarantee unless the behavior is established and its conditions are stated.

## Claims and evidence

| ID | Severity | Proposed rule |
|---|---|---|
| E01 | required | Separate observed results, design intentions, assumptions, and recommendations. |
| E02 | required | Attach measurable conditions to performance and capacity claims. |
| E03 | required | State the scope of security, availability, and compatibility claims. |
| E04 | required | Identify the product version and configuration when behavior depends on them. |
| E05 | required | State uncertainty directly. |
| E06 | required | Distinguish a successful API response from successful completion of the requested operation. |

Preferred claim patterns:

- Observed: The test achieved `[throughput]` under `[test conditions]`.
- Intended: The design targets `[availability objective]`.
- Assumed: This estimate assumes `[workload and failure conditions]`.
- Conditional: The service meets `[criterion]` when `[conditions]` hold.
- Unknown: Compatibility with `[version]` has not been verified.

## Where prose rules stop

Do not apply these prose restrictions to commands, source code, API identifiers, configuration keys, logs, or quoted source material. Preserve those literals exactly.
