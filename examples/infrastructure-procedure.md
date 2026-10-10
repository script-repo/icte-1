# Infrastructure procedure example

Extract of ICTE-1 section 8.1. This example keeps the original precondition order. It is not a complete maintenance runbook, and it is not a formally checked STE compliance example.

A real procedure also needs the permissions, the stop conditions, and the evidence to retain. Do not invent those values. Mark them `TBD`.

Use [templates/runbook.md](../templates/runbook.md) when the procedure must be operational. A filled illustration is in [sample-runbook.md](sample-runbook.md).

## Original

> Prior to initiating the upgrade process, it should be verified that all workloads have been successfully migrated from the target host and that sufficient capacity exists across the remaining cluster nodes.

The original fails these checks:

| Text | Failure |
|---|---|
| The sentence is passive and names no actor. | L02, L06 |
| The sentence joins two checks. | L03 |
| Sufficient capacity has no criterion. | L12 |
| Should makes a precondition sound optional. | Section 3.2 |

## ICTE-1 wording

The workloads are already off the target host. The remaining nodes have sufficient capacity. The upgrade has not started. Missing facts stay missing.

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
