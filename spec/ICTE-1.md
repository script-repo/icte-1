# ICTE-1: Infrastructure and Cloud Technical English

Version: 0.1  
Status: Proposed independent specification  
Date: 2026-10-10  
Scope: IT infrastructure, cloud, AI, GitOps, DevSecOps, and platform engineering

## 1. Overview and relationship to ASD-STE100

ICTE-1 is a proposed writing specification that combines controlled terminology, clear writing rules, and operational documentation requirements. It is an independent, STE-inspired draft. It is not an official version of ASD-STE100 and does not establish ASD-STE100 compliance.

ASD-STE100 Simplified Technical English (STE) is a controlled form of English designed to make technical documentation clear, consistent, and less ambiguous. It regulates vocabulary, approved meanings, and sentence construction. Its central principle is to simplify language without removing technical meaning.

STE originated in aircraft maintenance. The first AECMA Simplified English Guide appeared in 1986. The current issue discussed here is Issue 9, published on January 15, 2025. Issue 9 has 53 writing rules and 875 approved words in its core dictionary, commonly rounded to approximately 900. The dictionary is not a hard limit on all usable terminology: the standard permits technical nouns and technical verbs under defined rules.

STE is different from an ontology. A controlled vocabulary governs terminology. A controlled language governs terminology and sentence construction. An ontology defines concepts, properties, relationships, and constraints. ICTE-1 provides a language and terminology layer that can be extended with an ontology, but its word list alone is not an ontology.

STE also differs from plain English, which is a broader approach to clear communication, and from S1000D, which addresses the structure and management of technical content rather than primarily its language.

A prompt that requests STE-style output does not prove formal compliance. Compliance requires checking the complete rules, dictionary, word meanings, grammatical roles, technical terminology, and technical accuracy.

The ICTE-1 rules and vocabulary below are proposed conventions, not quotations from ASD-STE100. Sentence-length targets and requirement-word definitions are local conventions for this draft.

## 2. Purpose and scope

### 2.1 Purpose

Make technical content precise enough that a reader can identify:

1. Which component performs an action.
2. Which resource the action affects.
3. Where the action occurs.
4. Which conditions must be true.
5. What result to expect.
6. How to detect failure.
7. How to recover.

Preserve technical detail. Simplify the language, not the architecture.

### 2.2 Scope

Apply ICTE-1 to:

- Architecture descriptions and design decisions.
- Deployment guides and operational runbooks.
- Infrastructure-as-code documentation.
- GitOps workflows and repository documentation.
- Security controls and exception records.
- AI model serving and agent workflows.
- Platform service definitions and developer guides.
- Technical proposals and customer-facing explanations.

Do not apply prose restrictions to commands, source code, API identifiers, configuration keys, logs, or quoted source material.

## 3. Core writing rules

### 3.1 Language and structure

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

Sentence-length targets are review checks, not permission to remove technical meaning. Record exceptions for long product names, conditions, and identifiers.

### 3.2 Requirement language

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Avoid shall. Avoid using will to imply a guarantee unless the behavior is established and its conditions are stated.

### 3.3 Claims and evidence

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

## 4. Controlled terminology

This is a starter vocabulary, not an exhaustive dictionary. Definitions establish how terms should be used within ICTE-1.

### 4.1 IT infrastructure

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| physical server | A physical compute system. Use when distinguishing physical and virtual resources. |
| hypervisor host | A system that runs a hypervisor and hosts virtual machines. |
| virtual machine | A virtual compute instance with its own guest operating system. |
| cluster | A named group of cooperating systems. State the cluster type. |
| node | A member of a named cluster. Qualify it when multiple cluster types appear. |
| workload | An application or processing task and its associated execution requirements. |
| resource | An identifiable compute, storage, network, or software object. Specify the type when relevant. |
| capacity | The amount of a resource available or supported. State the resource and unit. |
| utilization | The measured proportion of a resource in use. State the measurement interval. |
| snapshot | A point-in-time representation of state. Do not use as an automatic synonym for backup. |
| backup | A retained recovery copy. State retention, location, and recovery assumptions. |
| failover | Transfer of service operation to an alternate resource after a failure or specified trigger. |
| recovery | Restoration of a specified service or data state. State the recovery criterion. |

### 4.2 Cloud

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| cloud environment | A specified environment that provides cloud services. Name its provider or operator. |
| cloud account | A provider-specific administrative and billing boundary. Preserve the provider's exact resource name. |
| region | A provider-defined geographic deployment area. |
| availability zone | A provider-defined deployment boundary. Do not imply identical guarantees across providers. |
| tenant | An explicitly defined consumer or isolation boundary. |
| managed service | A service with stated provider and customer responsibilities. |
| control plane | Components that manage configuration, scheduling, or lifecycle operations. |
| data plane | Components that process application traffic or data. |
| private endpoint | An endpoint reached through a specified private network path. |
| hybrid cloud | A design that integrates private and public cloud environments. State the actual integration. |
| multicloud | Use of services from more than one cloud provider. State which providers and services. |

Do not use private, isolated, disconnected, and air-gapped interchangeably. Describe network reachability, administration, and data movement separately.

### 4.3 AI and agent systems

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| model | A machine-learning model. Qualify its function and version when relevant. |
| model artifact | Stored model files and associated metadata. |
| model version | An identifiable revision of a model. |
| inference | Execution of a model to produce an output from an input. |
| inference server | Software that loads models and processes inference requests. |
| inference endpoint | The address and interface used to request inference. |
| token | A unit produced by a specified tokenizer. Do not treat tokens as words. |
| context window | The supported token capacity for a specified model and execution configuration. |
| embedding | A numeric representation produced by a specified embedding model. |
| retrieval | Selection of stored information for a request. |
| retrieval-augmented generation | Generation that uses retrieved information as additional context. |
| agent | A software system that selects or sequences actions toward a goal. State its authority and limits. |
| tool | A callable capability available to software or an agent. |
| tool call | An invocation of a tool with specified arguments. |
| memory | Retained information available across interactions. State storage, scope, and retention. |
| evaluation | Measurement against specified tasks, datasets, and acceptance criteria. |

Prohibit misleading equivalences:

- Model output is not verified fact.
- Retrieval is not model training.
- Tool availability is not permission to execute.
- Agent autonomy is not unrestricted authority.
- Open-weight is not automatically open-source.
- Private deployment is not automatically compliant deployment.

### 4.4 GitOps and delivery

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| desired state | The declared configuration that a managed system is intended to reach. |
| observed state | The state reported by the managed system at a specified time. |
| reconciliation | Comparison of desired and observed state, followed by permitted corrective actions. |
| configuration drift | A specified difference between desired and observed configuration. |
| GitOps controller | Software that obtains declared state and reconciles managed resources. |
| source repository | A version-controlled store for source material. |
| artifact repository | A store for built or packaged artifacts. |
| manifest | A declarative resource description. |
| commit | A version-control record of changes. |
| promotion | Selection or approval of an artifact or configuration for another environment. |
| deployment | Introduction or update of software or configuration in an environment. |
| rollout | The process of introducing a deployment across its intended targets. |
| rollback | An attempt to return to a specified previous state. State what it does and does not restore. |

For this draft, reserve GitOps for workflows with declared state and automated reconciliation. Merely storing scripts in Git does not satisfy that convention.

### 4.5 DevSecOps

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| identity | A represented user, workload, or system principal. |
| authentication | Verification of an asserted identity. |
| authorization | Determination of permitted actions. |
| credential | Information used to establish identity or access. |
| secret | Sensitive information that requires controlled access and handling. |
| policy | A stated rule or set of rules. |
| policy enforcement | Application of a policy at a named enforcement point. |
| vulnerability | A weakness that can contribute to a security compromise. |
| finding | A reported observation from a scan, test, or review. |
| security exception | An approved departure from a requirement, with scope and expiry. |
| provenance | Information about an artifact's origin and production history. |
| attestation | A statement about an artifact or process, associated with an identified issuer. |

Do not use a successful scan as proof that a system is secure. State the checks performed, their coverage, and their limitations.

### 4.6 Platform engineering

| Preferred term | Controlled meaning or usage restriction |
|---|---|
| platform | A defined set of services and interfaces provided to specified consumers. |
| platform service | A named capability with an owner, interface, and operating conditions. |
| internal developer platform | An internal platform that supports software delivery and operation. |
| developer portal | An interface for discovering or requesting capabilities. Do not equate it with the entire platform. |
| service catalog | A maintained inventory of services and their metadata. |
| golden path | A supported workflow for a defined use case. State whether its use is optional or mandatory. |
| self-service | Consumer execution of a defined action without a separate operator performing that action. |
| guardrail | A named preventive or detective control. State its enforcement behavior. |
| service owner | The accountable owner of a specified service. |
| service-level objective | A stated target for a defined service-level indicator over a specified period. |

## 5. Approved action verbs

| Verb | Intended action |
|---|---|
| create | Make a new resource. |
| provision | Allocate and configure resources for use. |
| configure | Set resource properties. |
| build | Produce an artifact from source inputs. |
| deploy | Introduce an artifact or configuration into an environment. |
| reconcile | Bring managed state toward declared state within specified authority. |
| validate | Test an item against specified rules or criteria. |
| verify | Establish that a stated condition is true using evidence. |
| authorize | Permit a named action for a named identity. |
| revoke | Remove specified permission or credential validity. |
| rotate | Replace a credential or key through a defined transition. |
| scale | Change resource allocation or instance count. State which. |
| migrate | Move a workload or data between specified locations. |
| restore | Recover from a specified recovery source. |
| delete | Remove a specified resource. State permanence and dependent effects. |

Avoid vague operational verbs such as handle, fix, optimize, secure, and enable unless the sentence explains the specific action.

## 6. Domain-specific precision rules

### 6.1 Infrastructure and cloud

Every design or procedure must state relevant:

- Resource types and boundaries.
- Failure domains.
- Capacity assumptions.
- Network paths and dependencies.
- Provider and customer responsibilities.
- Recovery objectives and verification criteria.

Replace highly available with a description of the failures the design addresses.

Replace unlimited scale with stated scaling limits or an explicit note that limits are unknown.

### 6.2 AI

Every model-serving description must identify relevant:

- Model and model version.
- Serving software and version.
- Hardware and resource allocation.
- Precision or quantization.
- Input and output limits.
- Concurrency and batching conditions.
- Data handling and retention.
- Evaluation criteria.

Every agent procedure must identify:

- Available tools.
- Permitted targets.
- Read and write permissions.
- Approval requirements.
- Execution limits.
- Audit records.
- Failure and escalation behavior.

### 6.3 GitOps

Every GitOps procedure must name:

- The desired-state source.
- The managed resources.
- The reconciliation controller.
- The controller's authority.
- Drift handling.
- Promotion gates.
- Emergency-change handling.
- Recovery limitations.

Do not imply that reverting a commit necessarily restores application data or reverses external side effects.

### 6.4 DevSecOps

Every control description must name:

- The protected resource.
- The threat or prohibited condition.
- The control mechanism.
- The enforcement point.
- The evidence of operation.
- The exception owner and expiry, when applicable.

### 6.5 Platform engineering

Every platform service must state:

- Intended consumers.
- Service owner.
- Supported interface.
- Required inputs.
- Provisioned outputs.
- Quotas and restrictions.
- Support boundaries.
- Lifecycle and retirement behavior.

## 7. Required document patterns

### 7.1 Operational runbook

```text
Title:
Purpose:
Owner:
Applicable products and versions:
Target environment:
Required permissions:
Prerequisites:
Impact and warnings:

Procedure:
1. Condition, if applicable.
   Action.
   Expected result.
   Failure response.

Verification:
Stop conditions:
Recovery or rollback:
Known limitations:
Evidence to retain:
```

### 7.2 Architecture description

```text
Objective:
Scope:
Consumers and owners:
Components:
Interfaces:
Data flows:
Identity and authorization:
Trust boundaries:
Failure domains:
Capacity assumptions:
Observability:
Recovery:
Constraints:
Alternatives:
Decision and rationale:
Unverified assumptions:
```

### 7.3 AI tool description

```text
Tool name:
Purpose:
Allowed callers:
Allowed targets:
Input schema:
Output schema:
Read or write behavior:
External side effects:
Required approval:
Timeout:
Retry behavior:
Idempotency conditions:
Failure response:
Audit requirements:
```

A language rule never overrides an organization's approval, security, or change-management requirements.

## 8. Before-and-after examples

The examples illustrate writing transformations. They are not executable procedures.

| Domain | Ambiguous wording | ICTE-1 wording |
|---|---|---|
| Infrastructure | Optimize the cluster before maintenance. | Verify that the remaining hosts meet the workload capacity requirements before maintenance. |
| Cloud | Secure connectivity is enabled. | The application connects through the private endpoint. The service requires authentication and encrypted transport. |
| AI | The agent intelligently resolves infrastructure issues. | The agent reads alerts and proposes changes. An operator must approve changes before execution. |
| GitOps | Push the deployment through GitOps. | Commit the desired configuration. The GitOps controller retrieves the configuration and reconciles the managed resources. |
| DevSecOps | The pipeline ensures secure releases. | The pipeline blocks promotion when a required security check fails. Approved exceptions must identify an owner and expiry. |
| Platform engineering | The platform streamlines developer onboarding. | Developers request a project through the portal. The platform creates the resources defined in the approved project template. |

### 8.1 Infrastructure procedure example

Original:

> Prior to initiating the upgrade process, it should be verified that all workloads have been successfully migrated from the target host and that sufficient capacity exists across the remaining cluster nodes.

Clearer procedural version:

1. Before you start the upgrade, check the available capacity on the other cluster nodes.
2. Move all workloads from the target host.
3. Check that no workloads remain on the target host.
4. Start the upgrade.

This example illustrates actor, sequence, and verification clarity. It is not a complete maintenance runbook or a formally checked STE compliance example. A real procedure requires product-specific prerequisites, impact assessment, capacity criteria, stop conditions, and recovery instructions.

## 9. Machine-readable vocabulary format

Store each term as a record rather than a simple word list.

```yaml
specification: ICTE-1
version: 0.1
status: draft

terms:
  - id: gitops.reconciliation
    preferred_term: reconciliation
    part_of_speech: noun
    domain: gitops
    definition: >
      Comparison of desired and observed state, followed
      by permitted corrective actions.
    allowed_aliases: []
    avoid_as_synonyms:
      - deployment
      - synchronization
    related_terms:
      - desired state
      - observed state
      - configuration drift
    usage_rule: >
      Identify the controller, managed resources,
      and corrective-action authority.
    example: >
      The controller reconciles the managed resources
      against the declared configuration.
    owner: platform-engineering
```

### 9.1 Extension toward an ontology

The record structure supports a terminology registry. To extend it into an ontology, add typed concepts and explicit relations such as:

```text
GitOpsController reconciles ManagedResource
InferenceServer serves ModelVersion
Agent invokes Tool
Policy constrains Action
PlatformService hasOwner Team
```

These relations are proposed modeling statements. They require defined entity types and constraints before they constitute a formal ontology.

## 10. Copy-ready AI instruction

```text
Write using ICTE-1, an independent technical writing profile
for infrastructure, cloud, AI, GitOps, DevSecOps, and platform
engineering.

Use clear technical English and consistent terminology.
Name the actor, action, target, scope, and conditions.
Give one action per procedural step.
Target 20 words per procedural sentence and 25 words per
descriptive sentence. Preserve meaning when an exception
is necessary.

Use must for requirements, should for recommendations,
may for permission, and can for capability.

Preserve product names, code, commands, API identifiers,
configuration keys, and quoted logs exactly.

Separate facts, observations, assumptions, recommendations,
and design intentions.

Do not invent prerequisites, values, expected results,
product behavior, or performance evidence.
Mark missing information as unspecified or TBD.

For state-changing procedures, state permissions, impact,
verification, stop conditions, and recovery limitations.

For AI agents, state tool authority, permitted targets,
approval requirements, and execution limits.

For GitOps, distinguish desired state, observed state,
reconciliation, deployment, and promotion.

Do not claim that private means compliant, that a scan
proves security, or that model output is verified fact.

Do not claim formal ASD-STE100 compliance.
```

### 10.1 General STE-inspired instruction

For situations that do not require the full ICTE-1 profile:

```text
Write in clear technical English using ASD-STE100 principles.
Use short sentences, active voice, and consistent terminology.
Give one instruction per procedural sentence.
Preserve product names, commands, configuration keys, and
necessary technical terms.
Do not remove conditions, caveats, or technical detail to
shorten the text.
Do not claim formal STE compliance.
```

## 11. Acceptance and governance

A document passes this draft profile when:

- Terms match the approved domain meanings.
- Actions identify their targets and relevant actors.
- Preconditions and success criteria are explicit.
- Destructive effects and recovery limits are stated.
- Product-specific claims identify applicable versions.
- Performance claims include measurement conditions.
- Unknown information remains visibly unknown.
- A technical owner has reviewed correctness.
- Exceptions to the writing rules are recorded.

For an initial implementation, maintain three version-controlled assets:

1. The writing rules.
2. The terminology registry.
3. Example documents.

These assets can remain sections of this single document initially. Separate them only when independent maintenance becomes useful.

Treat automated linting as a language check, not proof of technical correctness.

The next improvement should be to test this draft against one architecture document, one operational runbook, and one AI tool specification. Use the review results to refine the vocabulary before expanding it into a larger dictionary.

## 12. Limitations

- ICTE-1 is a proposed writing profile, not a published industry standard.
- The vocabulary is a starter set, not a complete replacement for the ASD-STE100 dictionary.
- The domain definitions are local usage conventions, not universal definitions across every vendor or standard.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- Examples are illustrative and require technical validation before operational use.
- A prompt alone cannot establish compliance with either ICTE-1 or ASD-STE100.

## 13. Source notes

Background about ASD-STE100 and GitOps was drawn from the sources reviewed in the preceding discussion. The ICTE-1 rules, vocabulary, templates, and examples are original proposed conventions.

- ASD-STE100 home page: https://www.asd-ste100.org/
- About ASD-STE100: https://www.asd-ste100.org/about.html
- ASD-STE100 FAQ: https://www.asd-ste100.org/STE_faq.html
- ASD-STE100 Issue 9 specification: https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf
- Simplified Technical English and S1000D context: https://www.techwriter.ai/s1000d/writing-for-s1000d/simplified-technical-english
- Controlled natural language and formal representation: https://www.tkuhn.org/talk/larc2013cnl.pdf
- ASD-STE100 technical writing overview: https://www.techscribe.co.uk/techw/asd-simplified-technical-english.htm
- GitOps overview: https://www.infralovers.com/glossary/gitops/
