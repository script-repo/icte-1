# Infrastructure procedure example

Extract of ICTE-1 section 8.1. This example shows actor, sequence, and verification clarity. It is not a complete maintenance runbook, and it is not a formally checked STE compliance example.

A real procedure requires product-specific prerequisites, an impact assessment, capacity criteria, stop conditions, and recovery instructions.

## Original

> Prior to initiating the upgrade process, it should be verified that all workloads have been successfully migrated from the target host and that sufficient capacity exists across the remaining cluster nodes.

## Clearer procedural version

1. Before you start the upgrade, check the available capacity on the other cluster nodes.
2. Move all workloads from the target host.
3. Check that no workloads remain on the target host.
4. Start the upgrade.

## What this example does not state

The source text does not state the capacity criterion, the product, the permissions, the impact, the stop conditions, or the recovery method. Do not invent those values. Mark them `TBD` until an owner supplies them.

Use [templates/runbook.md](../templates/runbook.md) when the procedure must be operational.
