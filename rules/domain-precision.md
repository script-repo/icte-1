# Domain precision rules

Extract of ICTE-1 section 6. Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md). If this file disagrees with the specification, the specification wins.

For every checklist in this section, state each item, or mark the item not applicable. Do not omit an item because it might be irrelevant.

## Infrastructure and cloud

Every design or procedure must state each item below, or mark the item not applicable.

- Resource types and boundaries.
- Failure domains.
- Capacity assumptions.
- Network paths and dependencies.
- Provider and customer responsibilities.
- Recovery objectives and verification criteria.

Replace highly available with a description of the failures the design addresses.

Replace unlimited scale with stated scaling limits, or state that the limits are unknown.

Put the warning immediately before a destructive action. Rule L13 applies.

Do not use private, isolated, disconnected, and air-gapped interchangeably. Describe network reachability, administration, and data movement separately.

## AI

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

The following equivalences are prohibited. Each one has severity required.

- Model output is not verified fact.
- Retrieval is not model training.
- Tool availability is not permission to execute.
- Agent autonomy is not unrestricted authority.
- Open-weight is not automatically open-source.
- Private deployment is not automatically compliant deployment.

## GitOps

For this profile, reserve GitOps for a workflow that declares the desired state and reconciles that state continuously. Storing scripts in Git does not satisfy the convention.

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

## DevSecOps

Every control description must state each item below, or mark the item not applicable.

- The protected resource.
- The threat or prohibited condition.
- The control mechanism.
- The enforcement point.
- The evidence of operation.
- The exception owner and expiry, when an exception exists. Mark this item not applicable when no exception exists.

Do not use a successful scan as proof that a system is secure. State the checks performed, their coverage, and their limitations.

## Platform engineering

Every platform service must state each item below, or mark the item not applicable.

- Intended consumers.
- Service owner.
- Supported interface.
- Required inputs.
- Provisioned outputs.
- Quotas and restrictions.
- Support boundaries.
- Lifecycle and retirement behavior.

A language rule never overrides an organization's approval, security, or change-management requirements.
