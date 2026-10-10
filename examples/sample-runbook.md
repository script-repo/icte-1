# Sample: operational runbook

Illustration of section 7.1. This is not an executable procedure. Unknown facts are `TBD`. The precondition order matches section 8.1.

Rules on the steps are annotations for the reviewer. They are not part of the procedure a technician reads aloud.

**Title:** Upgrade one hypervisor host

**Purpose:** Upgrade the named hypervisor host after the two preconditions pass.

**Owner:** TBD

**Applicable products and versions:** TBD

**Target environment:** TBD

Reviewer note: this field names the runtime target, not the cloud environment. Cloud environment: TBD.

**Required permissions:** TBD

**Prerequisites:** The operator has the cluster name and the target host name. Cluster type: TBD.

**Capacity criterion:** TBD

**Impact and warnings:** Impact: TBD. Repeat the impact in the warning on the upgrade step.

## Procedure

1. **Condition, if applicable:** The change window is open. Window: TBD.

   **Warning, immediately before a destructive action:** not applicable. This step does not change the host.

   **Action:** The operator verifies that every workload has migrated off the target host.

   **Expected result:** No workload remains on the target host.

   **Failure response:** Stop. Do not upgrade the host.

   Rules: L02, L03, L05, L06, L12. Verb: verify.

2. **Condition, if applicable:** Step 1 passed.

   **Warning, immediately before a destructive action:** not applicable. This step does not change the host.

   **Action:** The operator verifies that the remaining nodes meet the capacity criterion.

   **Expected result:** The remaining capacity meets the capacity criterion. Criterion: TBD.

   **Failure response:** Stop. Do not upgrade the host.

   Rules: L01, L02, L03, L12. Verb: verify. State the cluster type. Cluster type: TBD.

3. **Condition, if applicable:** Steps 1 and 2 passed.

   **Warning, immediately before a destructive action:** The upgrade takes the target host out of normal service. Impact: TBD. Recovery: TBD.

   **Action:** The operator upgrades the target host. Upgrade command: TBD.

   **Expected result:** TBD

   **Failure response:** Stop. Follow Recovery or rollback. Do not invent a recovery step.

   Rules: L05, L12, L13.

   Exception: upgrade is not an approved verb. The approved list has no verb for a vendor upgrade command.

## Verification

The operator verifies that the target host reports the product version. Product version: TBD. Command: TBD.

Rules: E04, verb verify.

## Stop conditions

Stop when step 1 or step 2 fails. Stop when the impact is still TBD and the change window does not allow an unknown impact.

## Recovery or rollback

TBD. State what recovery restores and what it does not restore. A rollback of configuration does not by itself restore data on the host.

## Known limitations

The capacity criterion, the product, the command, and the recovery method are unknown. This sample does not make them known.

## Evidence to retain

TBD
