# ICTE-1: Infrastructure and Cloud Technical English

Version: 0.2  
Status: Proposed independent specification  
Date: 2026-10-10  
Scope: IT infrastructure, cloud, AI, GitOps, DevSecOps, and platform engineering

Version 0.2 revises the 0.1 draft. It does not change the purpose. It splits conformance, names the reader, corrects the registry schema, and replaces the procedure example that changed the original sequence.

## 1. Overview and relationship to ASD-STE100

ICTE-1 is a proposed writing specification that combines controlled terminology, clear writing rules, and operational documentation requirements. It is an independent, STE-inspired draft. It is not an official version of ASD-STE100 and does not establish ASD-STE100 compliance.

ASD-STE100 Simplified Technical English (STE) is a controlled form of English designed to make technical documentation clear, consistent, and less ambiguous. It regulates vocabulary, approved meanings, and sentence construction. Its central principle is to simplify language without removing technical meaning.

STE originated in aircraft maintenance. The first AECMA Simplified English Guide appeared in 1986. The current issue discussed here is Issue 9, published on January 15, 2025. Issue 9 has 53 writing rules and 875 approved words in its core dictionary, commonly rounded to approximately 900. The dictionary is not a hard limit on all usable terminology: the standard permits technical nouns and technical verbs under defined rules.

STE is different from an ontology. A controlled vocabulary governs terminology. A controlled language governs terminology and sentence construction. An ontology defines concepts, properties, relationships, and constraints. ICTE-1 provides a language and terminology layer that can be extended with an ontology, but its word list alone is not an ontology.

STE also differs from plain English, which is a broader approach to clear communication, and from S1000D, which addresses the structure and management of technical content rather than primarily its language.

A prompt that requests STE-style output does not prove formal compliance. Compliance requires checking the complete rules, dictionary, word meanings, grammatical roles, technical terminology, and technical accuracy.

The ICTE-1 rules and vocabulary below are proposed conventions, not quotations from ASD-STE100. Sentence-length targets and requirement-word definitions are local conventions for this draft. The requirement words are not RFC 2119. In particular, this profile defines *can*, and it does not use *shall*.

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

### 2.3 Reader

Write for a technical reader who can execute the procedure or review it. Include a reader who does not already know this product, and a reader who is not a native speaker of English.

Name the product when the behavior depends on it. Do not rely on unstated local knowledge. Sentence-length targets in rule L04 exist for this reader. They are not permission to delete a condition.

## 3. Core writing rules

The prose in this section is normative. [rules/writing-rules.md](../rules/writing-rules.md) must match it. `tools/check_alignment.py` checks that match.

### 3.1 Language and structure

A required rule fails the language result when the document breaks it and records no exception. An advisory rule is reported. An advisory miss does not fail the language result. Record the miss when the writer keeps the longer sentence in order to preserve meaning.

L04 applies to procedural and descriptive sentences in the document under review. It does not apply to tables, identifiers, or quoted source material in this specification.

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

### 3.2 Requirement language

| Word | Meaning in ICTE-1 |
|---|---|
| must | A required condition or action. |
| must not | A prohibited condition or action. |
| should | A recommendation. An exception requires a stated reason. |
| may | Permission. |
| can | Capability or possibility, not permission. |

Do not use shall. Do not use will to imply a guarantee unless the behavior is established and its conditions are stated.

### 3.3 Claims and evidence

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

## 4. Controlled terminology

[vocabulary/registry.yaml](../vocabulary/registry.yaml) is normative for term records. The tables in this section and in section 5 must match that file. Change both in the same commit. `tools/check_alignment.py` fails if they differ.

This is a starter vocabulary, not an exhaustive dictionary. Definitions establish how terms are used within ICTE-1.

### 4.1 IT infrastructure

| Preferred term | Definition | Usage rule |
|---|---|---|
| physical server | A physical compute system. | Use when distinguishing physical and virtual resources. |
| hypervisor host | A system that runs a hypervisor and hosts virtual machines. | Do not use hypervisor host as a synonym for node unless that host is a member of the named cluster. |
| virtual machine | A virtual compute instance with its own guest operating system. | — |
| cluster | A named group of cooperating systems. | State the cluster type. Do not leave cluster unqualified when the document names more than one cluster type. |
| node | A member of a named cluster. | State the cluster type. Do not use node as a synonym for hypervisor host. |
| workload | An application or processing task and its associated execution requirements. | — |
| resource | An identifiable compute, storage, network, or software object. | Specify the type when relevant. |
| capacity | The amount of a resource available or supported. | State the resource and unit. |
| utilization | The measured proportion of a resource in use. | State the measurement interval. |
| snapshot | A point-in-time representation of state. | Do not use as an automatic synonym for backup. |
| backup | A retained recovery copy. | State retention, location, and recovery assumptions. |
| failover | Transfer of service operation to an alternate resource after a failure or specified trigger. | — |
| recovery | Restoration of a specified service or data state. | State the recovery criterion. |
| namespace | A named isolation scope inside a specified platform or cluster. | State the system that defines the namespace. Do not use namespace as a synonym for tenant or cloud account. |
| volume | A storage unit presented to a workload. | State the storage system, and state whether the volume is ephemeral or persistent. |
| recovery point objective | The maximum age of data that recovery is intended to restore. | State the service and the interval. Do not use recovery point objective as a synonym for recovery time objective. |
| recovery time objective | The maximum time allowed to restore a stated service after a stated failure. | State the service and the failure. Do not use recovery time objective as a synonym for recovery point objective. |
| maintenance | A planned change that takes a named resource out of normal service. | State the window, the impact, and the recovery method. Do not use maintenance as a synonym for failover or recovery. |

### 4.2 Cloud

| Preferred term | Definition | Usage rule |
|---|---|---|
| cloud environment | A specified environment that provides cloud services. | Name its provider or operator. Do not use cloud environment as a synonym for environment. |
| environment | A named runtime target for a workload or a deployment. | Do not use environment as a synonym for cloud environment. Name the target, such as development, test, or production. |
| cloud account | A provider-specific administrative and billing boundary. | Preserve the provider's exact resource name. |
| region | A provider-defined geographic deployment area. | — |
| availability zone | A provider-defined deployment boundary. | Do not imply identical guarantees across providers. |
| tenant | An explicitly defined consumer or isolation boundary. | — |
| managed service | A service with stated provider and customer responsibilities. | — |
| control plane | Components that manage configuration, scheduling, or lifecycle operations. | — |
| data plane | Components that process application traffic or data. | — |
| private endpoint | An endpoint reached through a specified private network path. | — |
| hybrid cloud | A design that integrates private and public cloud environments. | State the actual integration. |
| multicloud | Use of services from more than one cloud provider. | State which providers and services. |

Do not use private, isolated, disconnected, and air-gapped interchangeably. Describe network reachability, administration, and data movement separately.

### 4.3 AI and agent systems

| Preferred term | Definition | Usage rule |
|---|---|---|
| model | A machine-learning model. | Qualify its function and version when relevant. |
| model artifact | Stored model files and associated metadata. | Do not use model artifact as a synonym for image. |
| model version | An identifiable revision of a model. | — |
| quantization | The numeric representation used to store or run a model. | State the representation, and state whether it applies to weights, activations, or the KV cache. Do not write precision alone when the text means quantization. |
| inference | Execution of a model to produce an output from an input. | — |
| inference server | Software that loads models and processes inference requests. | — |
| inference endpoint | The address and interface used to request inference. | — |
| token | A unit produced by a specified tokenizer. | Do not treat a token as a word. Do not use token for an authentication credential. Use credential for that sense. |
| context window | The supported token capacity for a specified model and execution configuration. | — |
| embedding | A numeric representation produced by a specified embedding model. | — |
| retrieval | Selection of stored information for a request. | Retrieval is not model training. |
| retrieval-augmented generation | Generation that uses retrieved information as additional context. | — |
| agent | A software system that selects or sequences actions toward a goal. | State its authority and limits. Agent autonomy is not unrestricted authority. |
| tool | A callable capability available to software or an agent. | Tool availability is not permission to execute. |
| tool call | An invocation of a tool with specified arguments. | — |
| memory | Retained information available across interactions. | State the storage, the scope, and the retention. Do not use memory for RAM, GPU memory, or other hardware capacity. State hardware capacity with the resource and the unit. |
| evaluation | Measurement against specified tasks, datasets, and acceptance criteria. | — |

The following equivalences are prohibited. Each one has severity required.

- Model output is not verified fact.
- Retrieval is not model training.
- Tool availability is not permission to execute.
- Agent autonomy is not unrestricted authority.
- Open-weight is not automatically open-source.
- Private deployment is not automatically compliant deployment.

### 4.4 GitOps and delivery

| Preferred term | Definition | Usage rule |
|---|---|---|
| desired state | The declared configuration that a managed system is intended to reach. | — |
| observed state | The state reported by the managed system at a specified time. | — |
| reconciliation | Comparison of desired and observed state, followed by permitted corrective actions. | Identify the controller, managed resources, and corrective-action authority. |
| configuration drift | A specified difference between desired and observed configuration. | — |
| GitOps controller | Software that obtains declared state and reconciles managed resources. | — |
| managed resource | A resource that a named GitOps controller is authorized to reconcile. | Name the controller and the authority of that controller. |
| source repository | A version-controlled store for source material. | — |
| artifact repository | A store for built or packaged artifacts. | — |
| image | A packaged software artifact identified by a digest or an immutable tag. | Do not use image as a synonym for model artifact. |
| manifest | A declarative resource description. | — |
| commit | A version-control record of changes. | Do not imply that reverting a commit restores application data or reverses external side effects. |
| promotion | Selection or approval of an artifact or configuration for another environment. | — |
| deployment | Introduction or update of software or configuration in an environment. | Do not use deployment as a synonym for reconciliation or promotion. When the text names a product object, preserve the product identifier and state that the name is the product object. |
| rollout | The process of introducing a deployment across its intended targets. | — |
| rollback | An attempt to return to a specified previous state. | State what it does and does not restore. |

For this profile, reserve *GitOps* for a workflow that declares the desired state and reconciles that state continuously. That use follows the OpenGitOps principles of declarative desired state and continuous reconciliation. Storing scripts in Git does not satisfy the convention. See https://opengitops.dev/.

### 4.5 DevSecOps

| Preferred term | Definition | Usage rule |
|---|---|---|
| identity | A represented user, workload, or system principal. | — |
| authentication | Verification of an asserted identity. | Do not use authentication as a synonym for authorization. |
| authorization | Determination of permitted actions. | Do not use authorization as a synonym for authentication. |
| credential | Information used to establish identity or access. | Do not use credential as a synonym for token. In this profile, token means a tokenizer unit. |
| secret | Sensitive information that requires controlled access and handling. | — |
| policy | A stated rule or set of rules. | Name the policy type. Do not use policy alone for a network policy, an identity policy, or an admission policy. |
| policy enforcement | Application of a policy at a named enforcement point. | — |
| vulnerability | A weakness that can contribute to a security compromise. | — |
| finding | A reported observation from a scan, test, or review. | A finding is not by itself proof that a system is secure or insecure. State the check and its coverage. |
| security exception | An approved departure from a requirement, with scope and expiry. | — |
| provenance | Information about an artifact's origin and production history. | — |
| attestation | A statement about an artifact or process, associated with an identified issuer. | — |

Do not use a successful scan as proof that a system is secure. State the checks performed, their coverage, and their limitations.

### 4.6 Platform engineering

| Preferred term | Definition | Usage rule |
|---|---|---|
| platform | A defined set of services and interfaces provided to specified consumers. | — |
| platform service | A named capability with an owner, interface, and operating conditions. | — |
| internal developer platform | An internal platform that supports software delivery and operation. | — |
| developer portal | An interface for discovering or requesting capabilities. | Do not equate it with the entire platform. |
| service catalog | A maintained inventory of services and their metadata. | — |
| golden path | A supported workflow for a defined use case. | State whether its use is optional or mandatory. |
| self-service | Consumer execution of a defined action without a separate operator performing that action. | — |
| guardrail | A named preventive or detective control. | State its enforcement behavior. |
| service owner | The accountable owner of a specified service. | — |
| service-level objective | A stated target for a defined service-level indicator over a specified period. | — |

### 4.7 Senses that must not be merged

The usage rule on each term is normative. These pairs are the collisions the starter vocabulary already blocks:

- *token* is a tokenizer unit. It is not a credential.
- *memory* is retained agent state. It is not RAM, GPU memory, or other hardware capacity.
- *policy* needs a type. It is not, by itself, a network policy, an identity policy, or an admission policy.
- *node* is a member of a named cluster. It is not a hypervisor host.
- *deployment* is not reconciliation, and it is not promotion. Preserve a product identifier when the product object uses the same word.
- *environment* is a named runtime target. It is not a cloud environment.
- *image* is a packaged software artifact. It is not a model artifact.

## 5. Approved action verbs

Approved verbs are records in `terms`. Set `part_of_speech` to `verb` and `domain` to `action`. The registry has no separate `verbs` key.

The noun *action* names the class. Use an approved verb for a particular operation.

### 5.1 The noun *action*

| Preferred term | Definition | Usage rule |
|---|---|---|
| action | A named operation that an actor performs on a target. | Name the operation with an approved verb. State the actor and the target. |

### 5.2 Verbs

| Verb | Definition | Usage rule |
|---|---|---|
| create | Make a new resource. | — |
| provision | Allocate and configure resources for use. | — |
| configure | Set resource properties. | — |
| build | Produce an artifact from source inputs. | — |
| deploy | Introduce an artifact or configuration into an environment. | Do not use deploy as a synonym for reconcile. |
| reconcile | Bring managed state toward declared state within specified authority. | Do not use reconcile as a synonym for deploy. |
| validate | Test an item against specified rules or criteria. | Do not use validate as a synonym for verify. Validate tests an item against stated rules. |
| verify | Establish that a stated condition is true using evidence. | Do not use verify as a synonym for validate. Verify uses evidence to establish that a condition is true. |
| authorize | Permit a named action for a named identity. | — |
| revoke | Remove specified permission or credential validity. | — |
| rotate | Replace a credential or key through a defined transition. | — |
| scale | Change resource allocation or instance count. | State which change the verb names. |
| migrate | Move a workload or data between specified locations. | — |
| restore | Recover from a specified recovery source. | — |
| delete | Remove a specified resource. | State permanence and dependent effects. |

Do not use vague operational verbs such as handle, fix, optimize, secure, and enable unless the sentence states the specific action.

## 6. Domain-specific precision rules

The prose in this section is normative. [rules/domain-precision.md](../rules/domain-precision.md) must match it.

For every checklist in this section, state each item, or mark the item not applicable. Do not omit an item because it might be irrelevant. "Relevant" is not a pass condition.

### 6.1 Infrastructure and cloud

Every design or procedure must state each item below, or mark the item not applicable.

- Resource types and boundaries.
- Failure domains.
- Capacity assumptions.
- Network paths and dependencies.
- Provider and customer responsibilities.
- Recovery objectives and verification criteria.

Replace highly available with a description of the failures the design addresses.

Replace unlimited scale with stated scaling limits, or state that the limits are unknown.

Do not use private, isolated, disconnected, and air-gapped interchangeably. Describe network reachability, administration, and data movement separately.

Put the warning immediately before a destructive action. Rule L13 applies.

### 6.2 AI

Every model-serving description must state each item below, or mark the item not applicable.

- Model and model version.
- Serving software and version.
- Hardware and resource allocation.
- Quantization, and whether it applies to weights, activations, or the KV cache.
- Input and output limits.
- Concurrency and batching conditions.
- Data handling and retention.
- Evaluation criteria.

Every agent procedure must state each item below, or mark the item not applicable.

- Available tools.
- Permitted targets.
- Read and write permissions.
- Approval requirements.
- Execution limits.
- Audit records.
- Failure and escalation behavior.

### 6.3 GitOps

Every GitOps procedure must state each item below, or mark the item not applicable.

- The desired-state source.
- The managed resources.
- The reconciliation controller.
- The controller's authority.
- Drift handling.
- Promotion gates.
- Emergency-change handling.
- Recovery limitations.

Do not imply that reverting a commit restores application data or reverses external side effects.

### 6.4 DevSecOps

Every control description must state each item below, or mark the item not applicable.

- The protected resource.
- The threat or prohibited condition.
- The control mechanism.
- The enforcement point.
- The evidence of operation.
- The exception owner and expiry, when an exception exists. Mark this item not applicable when no exception exists.

### 6.5 Platform engineering

Every platform service must state each item below, or mark the item not applicable.

- Intended consumers.
- Service owner.
- Supported interface.
- Required inputs.
- Provisioned outputs.
- Quotas and restrictions.
- Support boundaries.
- Lifecycle and retirement behavior.

## 7. Required document patterns

A language rule never overrides an organization's approval, security, or change-management requirements.

The field list in each pattern is normative for that document type. The template must contain each field name.

### 7.1 Operational runbook

```text
Title:
Purpose:
Owner:
Applicable products and versions:
Target environment:
Required permissions:
Prerequisites:
Capacity criterion:
Impact and warnings:

Procedure:
1. Condition, if applicable.
   Warning, immediately before a destructive action.
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
Network paths:
Provider and customer responsibilities:
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

### 7.4 Model-serving description

Use this pattern for a served model. Do not use the tool pattern in section 7.3 as a substitute.

```text
Title:
Model:
Model version:
Serving software and version:
Hardware and resource allocation:
Quantization:
Input and output limits:
Concurrency and batching:
Data handling and retention:
Evaluation criteria:
Failure behavior:
Unverified items:
```

## 8. Before-and-after examples

The examples illustrate writing transformations. They are not executable procedures.

| Domain | Ambiguous wording | ICTE-1 wording |
|---|---|---|
| Infrastructure | Optimize the cluster before maintenance. | The operator verifies that the remaining hypervisor hosts meet the capacity criterion before maintenance. Capacity criterion: TBD. |
| Cloud | Secure connectivity is enabled. | The application connects through the private endpoint. The service requires authentication and encrypted transport. |
| AI | The agent intelligently resolves infrastructure issues. | The agent reads alerts and proposes changes. An operator must approve changes before execution. |
| GitOps | Push the deployment through GitOps. | An operator creates the commit that holds the desired state. The GitOps controller reconciles the managed resources. |
| DevSecOps | The pipeline ensures secure releases. | The pipeline blocks promotion when a required security check fails. Approved exceptions must identify an owner and expiry. |
| Platform engineering | The platform streamlines developer onboarding. | Developers request a project through the portal. The platform creates the resources defined in the approved project template. |

### 8.1 Infrastructure procedure example

The source text states two preconditions, in this order. The workloads are already off the target host. The remaining nodes have sufficient capacity. The upgrade has not started. The source does not name the actor, the capacity criterion, the product, or the recovery method.

Original:

> Prior to initiating the upgrade process, it should be verified that all workloads have been successfully migrated from the target host and that sufficient capacity exists across the remaining cluster nodes.

The original fails these checks:

| Text | Failure |
|---|---|
| The sentence is passive and names no actor. | L02, L06 |
| The sentence joins two checks. | L03 |
| Sufficient capacity has no criterion. | L12 |
| Should makes a precondition sound optional. | Section 3.2 |

ICTE-1 wording. The precondition order is unchanged. The upgrade is not a new migration. Missing facts stay missing.

1. The operator verifies that every workload has migrated off the target host.
   Expected result: no workload remains on the target host.
   Rules: L02, L03, L06. Verb: verify.
2. The operator verifies that the remaining nodes in the named cluster meet the capacity criterion.
   Cluster name: TBD. Cluster type: TBD. Capacity criterion: TBD.
   Rules: L01, L02, L12. Verb: verify.
3. Warning: state the impact of the upgrade before this action. Impact: TBD.
   After steps 1 and 2 pass, the operator upgrades the target host.
   Product and version: TBD. Upgrade command: TBD.
   Recovery: TBD. State what recovery restores and what it does not restore.
   Rules: L05, L12, L13.
   Exception: upgrade is not an approved verb. The approved list has no verb for a vendor upgrade command. Record this exception until the command is known.

This example is not a complete runbook, and it is not an ASD-STE100 compliance claim. A real procedure also needs the permissions, the stop conditions, and the evidence to retain. Use section 7.1. Do not invent those values.

## 9. Machine-readable vocabulary format

Store each term as one record in `terms`. Do not use a separate `verbs` list.

```yaml
specification: ICTE-1
version: "0.2"
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
```

Omit `owner` until a maintainer accepts accountability for that term. Do not copy the illustration `owner: platform-engineering` into the registry.

A verb uses the same fields:

```yaml
  - id: action.verify
    preferred_term: verify
    part_of_speech: verb
    domain: action
    definition: >
      Establish that a stated condition is true using evidence.
    allowed_aliases: []
    avoid_as_synonyms:
      - validate
    usage_rule: >
      Do not use verify as a synonym for validate.
      Verify uses evidence to establish that a condition is true.
```

`non_equivalences` and `proposed_relations` are records, not bare sentences. Section 9.1 states the relation shape. Each `left` and each `right` on a proposed relation is a term id.

### 9.1 Extension toward an ontology

These statements are proposed modeling relations. They are not a formal ontology until the entity types have constraints. The ids point at terms in the registry:

| id | left | relation | right |
|---|---|---|---|
| rel.gitops.reconciles | gitops.controller | reconciles | gitops.managed_resource |
| rel.ai.serves | ai.inference_server | serves | ai.model_version |
| rel.ai.invokes | ai.agent | invokes | ai.tool |
| rel.devsecops.constrains | devsecops.policy | constrains | action.named_action |
| rel.platform.has_owner | platform.platform_service | has_owner | platform.service_owner |

## 10. Copy-ready AI instruction

The text of this instruction is normative. [prompts/icte-1.txt](../prompts/icte-1.txt) must match the fenced block, without the fence.

<!-- prompt:icte-1 -->
```text
Write using ICTE-1, an independent technical writing profile
for infrastructure, cloud, AI, GitOps, DevSecOps, and platform
engineering.

Write for a technical reader who can execute or review the
procedure. Include a reader who does not already know this
product.

Use one approved term for each concept.
A token is a tokenizer unit, not a credential.
Memory is retained agent state, not hardware capacity.
A node is a member of a named cluster, not a hypervisor host.
An environment is a named runtime target, not a cloud environment.

Name the actor, the action, the target, the scope, and the
conditions.
Give one action per procedural step.
Put a condition before the action.
Put a warning immediately before a destructive action.
Target 20 words for a procedural sentence and 25 words for a
descriptive sentence. This target is advisory. Do not remove
technical meaning to meet it.

Use must for a requirement and must not for a prohibition.
Use should for a recommendation.
Use may for permission.
Use can for capability.
Do not use shall.
Do not use will to imply a guarantee unless the behavior is
established and its conditions are stated.

Preserve product names, code, commands, API identifiers,
configuration keys, and quoted logs exactly.

Separate observed results, design intentions, assumptions, and
recommendations.

Do not invent prerequisites, values, expected results, product
behavior, or performance evidence.
Mark missing information as unspecified or TBD.
For a checklist item that does not apply, write not applicable.

For a state-changing procedure, state the permissions, the
impact, the verification, the stop conditions, and the recovery
limits.

For an AI agent, state the tool authority, the permitted
targets, the approval requirements, and the execution limits.

For GitOps, distinguish desired state, observed state,
reconciliation, deployment, and promotion.

Do not claim that model output is verified fact, that retrieval
is training, that tool availability is permission to execute,
that a scan proves security, or that a private deployment is a
compliant deployment.

Do not claim formal ASD-STE100 compliance.
```
<!-- /prompt:icte-1 -->

### 10.1 General STE-inspired instruction

Use this block only when the document does not need the full ICTE-1 profile. [prompts/ste-inspired.txt](../prompts/ste-inspired.txt) must match it. This block is not ICTE-1.

<!-- prompt:ste-inspired -->
```text
Write in clear technical English using ASD-STE100 principles.
Use short sentences, active voice, and consistent terminology.
Give one instruction per procedural sentence.
Preserve product names, commands, configuration keys, and
necessary technical terms.
Do not remove conditions, caveats, or technical detail to
shorten the text.
Do not use shall.
Do not claim formal STE compliance.
This instruction is not the ICTE-1 profile.
```
<!-- /prompt:ste-inspired -->

## 11. Acceptance and governance

A review records three results. One result does not imply another.

### 11.1 Language result

The language result passes when all of the following are true:

- Terms match the approved meanings in the registry.
- Actions identify their targets and the actors that matter.
- Requirement words match section 3.2.
- Every required rule that the document breaks has a recorded exception.
- Unknown information remains visibly unknown.
- The document does not assert a prohibited equivalence from section 4.3.

Advisory rules, including L04, are reported. An advisory miss does not fail the language result. Record it when the writer kept the longer sentence in order to keep the meaning.

### 11.2 Operational completeness

Operational completeness passes when both of the following are true:

- Each item in the section 6 checklist for that document type is stated, or marked not applicable.
- Each field in the matching section 7 pattern is filled, or marked not applicable.

### 11.3 Technical review

Technical review passes only when a named owner of the technical content has reviewed correctness. This profile cannot record that result by itself. A language result is not a technical review. Operational completeness is not a technical review.

### 11.4 Normative sources

| Subject | Normative source | Copy that must match |
|---|---|---|
| Writing rules, requirement words, and claim rules | This document, section 3 | [rules/writing-rules.md](../rules/writing-rules.md) |
| Domain checklists | This document, section 6 | [rules/domain-precision.md](../rules/domain-precision.md) |
| The three results and the limitations | This document, sections 11 and 12 | [rules/acceptance.md](../rules/acceptance.md) |
| Term records | [vocabulary/registry.yaml](../vocabulary/registry.yaml) | Sections 4 and 5 of this document |
| Assistant instructions | Section 10 of this document | [prompts/](../prompts/) |
| Document patterns | Section 7 of this document | [templates/](../templates/) |

If a prose copy disagrees with this document, this document wins. Then change the copy in the same commit. If a term table disagrees with the registry, the registry wins for that record. Then change the table in the same commit. Do not delete technical meaning to silence the checker.

`tools/check_alignment.py` must pass before a change is complete. The checker is a language-alignment check. It is not proof of technical correctness, and it is not a language result for an arbitrary document.

Keep these assets under version control: the writing rules, the terminology registry, and the example documents. Also version the templates, the prompts, and the checker, because those copies drift when they are unversioned.

The next improvement is to apply section 11 to one real architecture document, one real runbook, and one real AI tool specification. Use the mismatches to refine the vocabulary. Do not expand the dictionary first.

## 12. Limitations

- ICTE-1 is a proposed writing profile, not a published industry standard.
- The vocabulary is a starter set, not a complete replacement for the ASD-STE100 dictionary.
- The domain definitions are local usage conventions, not universal definitions across every vendor or standard.
- The profile does not certify technical correctness, safety, security, compliance, or operational readiness.
- A language result does not establish operational completeness or technical review.
- Examples are illustrative and require technical validation before operational use.
- A prompt alone cannot establish compliance with either ICTE-1 or ASD-STE100.
- Automated alignment checks are not proof that a document is correct.

## 13. Source notes

Background about ASD-STE100 was drawn from the ASD-STE100 pages below. The GitOps reservation in section 4.4 follows the OpenGitOps principles. The ICTE-1 rules, vocabulary, templates, and examples are original proposed conventions.

- ASD-STE100 home page: https://www.asd-ste100.org/
- About ASD-STE100: https://www.asd-ste100.org/about.html
- ASD-STE100 FAQ: https://www.asd-ste100.org/STE_faq.html
- ASD-STE100 Issue 9 specification: https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf
- Simplified Technical English and S1000D context: https://www.techwriter.ai/s1000d/writing-for-s1000d/simplified-technical-english
- Controlled natural language and formal representation: https://www.tkuhn.org/talk/larc2013cnl.pdf
- ASD-STE100 technical writing overview: https://www.techscribe.co.uk/techw/asd-simplified-technical-english.htm
- OpenGitOps principles: https://opengitops.dev/
