# Before-and-after examples

Extract of ICTE-1 section 8. These examples show writing transformations. They are not executable procedures.

Canonical text: [spec/ICTE-1.md](../spec/ICTE-1.md).

| Domain | Ambiguous wording | ICTE-1 wording |
|---|---|---|
| Infrastructure | Optimize the cluster before maintenance. | The operator verifies that the remaining hypervisor hosts meet the capacity criterion before maintenance. Capacity criterion: TBD. |
| Cloud | Secure connectivity is enabled. | The application connects through the private endpoint. The service requires authentication and encrypted transport. |
| AI | The agent intelligently resolves infrastructure issues. | The agent reads alerts and proposes changes. An operator must approve changes before execution. |
| GitOps | Push the deployment through GitOps. | An operator creates the commit that holds the desired state. The GitOps controller reconciles the managed resources. |
| DevSecOps | The pipeline ensures secure releases. | The pipeline blocks promotion when a required security check fails. Approved exceptions must identify an owner and expiry. |
| Platform engineering | The platform streamlines developer onboarding. | Developers request a project through the portal. The platform creates the resources defined in the approved project template. |
