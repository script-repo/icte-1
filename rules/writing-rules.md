# Writing rules

Extract of ICTE-1 section 3. These are proposed conventions, not quotations from ASD-STE100.

Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md). If this file disagrees with the specification, the specification wins.

Sentence-length targets are review checks, not permission to remove technical meaning. Record exceptions for long product names, conditions, and identifiers.

## Language and structure

| ID | Proposed rule | Example |
|---|---|---|
| L01 | Use one preferred term for each concept within a document. | Do not alternate between hypervisor host and worker node unless they identify different resources. |
| L02 | Name the actor when responsibility matters. | The GitOps controller applies the configuration. |
| L03 | Give one action per procedural step. | Create the namespace. Then apply the policy in a separate step. |
| L04 | Target 20 words per procedural sentence and 25 words per descriptive sentence. | Split long sentences without removing conditions. |
| L05 | Put the condition before the action. | If the health check fails, stop the rollout. |
| L06 | Use active voice for instructions. | Run the validation job. |
| L07 | Replace ambiguous pronouns with component names. | The gateway forwards the request to the inference server. |
| L08 | Use numbered lists for sequences and bullets for unordered information. | Separate deployment steps from prerequisites. |
| L09 | Expand an acronym at its first use, unless the document defines an assumed vocabulary. | Recovery point objective (RPO). |
| L10 | Preserve literal identifiers exactly. | Write `spec.replicas`, not a paraphrased configuration key. |
| L11 | Do not use synonyms solely to avoid repetition. | Repeat deployment when that is the intended action. |
| L12 | Do not invent missing values, prerequisites, or expected results. | Mark an unspecified timeout as `TBD`. |

## Requirement language

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Avoid *shall*. Avoid using *will* to imply a guarantee unless the behavior is established and its conditions are stated.

## Claims and evidence

| ID | Proposed rule |
|---|---|
| E01 | Separate observed results, design intentions, assumptions, and recommendations. |
| E02 | Attach measurable conditions to performance and capacity claims. |
| E03 | State the scope of security, availability, and compatibility claims. |
| E04 | Identify the product version and configuration when behavior depends on them. |
| E05 | State uncertainty directly. |
| E06 | Distinguish a successful API response from successful completion of the requested operation. |

Preferred claim patterns:

- Observed: The test achieved `[throughput]` under `[test conditions]`.
- Intended: The design targets `[availability objective]`.
- Assumed: This estimate assumes `[workload and failure conditions]`.
- Conditional: The service meets `[criterion]` when `[conditions]` hold.
- Unknown: Compatibility with `[version]` has not been verified.

## Where prose rules stop

Do not apply these prose restrictions to commands, source code, API identifiers, configuration keys, logs, or quoted source material. Preserve those literals exactly.
