# Domain precision rules

Extract of ICTE-1 section 6. Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md).

## Infrastructure and cloud

Every design or procedure must state the relevant items below.

- Resource types and boundaries.
- Failure domains.
- Capacity assumptions.
- Network paths and dependencies.
- Provider and customer responsibilities.
- Recovery objectives and verification criteria.

Replace *highly available* with a description of the failures the design addresses.

Replace *unlimited scale* with stated scaling limits, or state that the limits are unknown.

Do not use *private*, *isolated*, *disconnected*, and *air-gapped* interchangeably. Describe network reachability, administration, and data movement separately.

## AI

Every model-serving description must identify the relevant items below.

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

Prohibited equivalences:

- Model output is not verified fact.
- Retrieval is not model training.
- Tool availability is not permission to execute.
- Agent autonomy is not unrestricted authority.
- Open-weight is not automatically open-source.
- Private deployment is not automatically compliant deployment.

## GitOps

Reserve *GitOps* for workflows with declared state and automated reconciliation. Storing scripts in Git does not satisfy that convention.

Every GitOps procedure must name:

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

Every control description must name:

- The protected resource.
- The threat or prohibited condition.
- The control mechanism.
- The enforcement point.
- The evidence of operation.
- The exception owner and expiry, when applicable.

Do not use a successful scan as proof that a system is secure. State the checks performed, their coverage, and their limitations.

## Platform engineering

Every platform service must state:

- Intended consumers.
- Service owner.
- Supported interface.
- Required inputs.
- Provisioned outputs.
- Quotas and restrictions.
- Support boundaries.
- Lifecycle and retirement behavior.

A language rule never overrides an organization's approval, security, or change-management requirements.
