# Day 3: Governance

**Date:** October 8, 2026

**Status:** Phase 1, Week 1

## Outcome

Enforced company rules in Azure: tags and Azure Policy for what is allowed to exist, resource locks for what cannot be deleted, and a management group above the subscription. Each rule was tested until Azure refused or fixed something.

## RBAC, Policy and locks

RBAC decides who may act. Azure Policy decides what is allowed to exist at all, even for an Owner. A lock blocks deleting or changing a scope, whoever you are. A request passes all three checks: identity, permission, then rules.

## Tags

Tags are name and value labels used for cost reports, ownership and automation. Tags are not inherited. The lab resource group carried three tags, and the Static Web App inside it carried none. In `az tag update`, the `Merge` operation adds tags and keeps the existing ones, while `Replace` removes them.

## Azure Policy

A definition is one rule, an initiative bundles several, and an assignment applies them to a scope. Two built-in policies were tested.

- **Modify** ("Inherit a tag from the resource group if missing") copies one named tag from the group to a resource that lacks it. It works through a managed identity that holds a role, and one assignment handles one tag name.
- **Deny** ("Require a tag on resource groups") blocks creating a resource group without the tag, even for the subscription Owner, with the error `RequestDisallowedByPolicy`.

New assignments take a few minutes to apply. For resources that already exist, a compliance scan marks them non-compliant, and a remediation task then fixes them.

## Resource locks

CanNotDelete blocks deletion. ReadOnly blocks changes as well. Locks override RBAC and inherit downward, and an Owner can remove a lock before deleting. Deleting a locked group failed with `ScopeLocked`. A permanent CanNotDelete lock now protects the resource group that hosts this documentation site.

## Management groups

A management group is a folder above subscriptions. Policy and role assignments made on it inherit downward to every subscription beneath it. A group called VestLux Lab was created under the Tenant Root Group, and the subscription was moved into it. The Owner role and the Deny policy, both assigned on the subscription itself, stayed in force.

## Costs and Azure Advisor

Cost analysis can group spending by tag, which is why tags matter for cost reports. A budget sends alerts and does not stop spending. Advisor gave one recommendation, in the Operational Excellence category: create an Azure Service Health alert.

## What I built

1. Added tags to the lab resource group with the CLI, and saw that the resource inside did not inherit them.
2. Assigned the Modify policy to the lab resource group, ran a compliance scan and a remediation task, and confirmed the Static Web App received the owner tag.
3. Assigned the Deny policy to the subscription and watched a resource group without the tag be refused.
4. Created a test group with a CanNotDelete lock and watched the delete fail with ScopeLocked, then placed a permanent lock on the lab group.
5. Created a management group, moved the subscription into it, and confirmed that the Owner role and the policy still applied.
6. Removed the test objects and both policy assignments, lifting the lock briefly and restoring it, then confirmed that groups can be created again without a tag.

## Issues met and how I fixed them

1. **Wrong policy scope.** The first assignment form had the subscription as the scope and the lab resource group in the exclusions box, so the resources it was meant to fix would have been skipped. I set the scope to the resource group and cleared the exclusions.
2. **Existing resource not fixed at first.** A new Modify assignment does not change resources that already exist. The compliance scan took several minutes, and my first remediation command failed because the CLI needs the assignment's resource name, not its display name. Once the scan marked the Static Web App as non-compliant, a remediation task added the tag.
3. **Cleanup blocked by the lock.** The CanNotDelete lock on the lab group also protected the role assignment and policy assignment stored inside it. I removed the lock, deleted both, and created the lock again.

## Findings

- A Deny policy applies to an Owner as well. RBAC can allow an action and Policy can still refuse it.
- One Modify assignment copies one tag. Inheriting three tags needs three assignments or an initiative.
- Assignments made on a subscription stay with it when the subscription moves to a management group.

## Exam objectives covered

Official AZ-104 objectives (study guide effective April 17, 2026), with an honest status.

- **Practised:** apply and manage tags
- **Practised:** implement and manage Azure Policy
- **Practised:** configure resource locks
- **Practised:** manage resource groups
- **Practised:** configure management groups
- **Practised:** manage costs with alerts, budgets and Azure Advisor

See the [AZ-104 objective tracker](../exam-tracker/az-104.md).

## Summary

- RBAC decides who may act, Policy decides what may exist, and locks protect what must not be removed.
- Tags are not inherited. The Modify effect can copy a tag down, one tag name per assignment.
- Deny blocks a request even for an Owner. Modify fixes it for you.
- Policy changes new and updated resources by itself. Existing resources need a compliance scan and a remediation task.
- Locks override RBAC and inherit downward, and they can block your own cleanup inside a locked group.
- Management groups let one assignment reach many subscriptions, and assignments on a subscription stay with it when it moves.

## Revision questions

??? question "What question does RBAC answer, and what question does Policy answer?"
    RBAC answers who may do something. Policy answers whether it is allowed to exist at all, even for someone who has permission.

??? question "Are tags inherited from a resource group by the resources inside it?"
    No. A Modify policy can copy a tag down, but one assignment handles one tag name.

??? question "What is the difference between the Deny and Modify effects?"
    Deny blocks the request. Modify changes the resource, for example by adding a tag, and needs a managed identity with a role to do it.

??? question "Why did an existing resource need extra steps after assigning a Modify policy?"
    Policy acts on new and updated resources by itself. For existing ones, a compliance scan must mark them non-compliant, and then a remediation task applies the change.

??? question "Can an Owner create a resource group that a Deny policy forbids?"
    No. Owner permission lets the request through RBAC, and the policy still refuses it with RequestDisallowedByPolicy.

??? question "Can an Owner delete a resource group that has a CanNotDelete lock?"
    Not directly. The delete fails with ScopeLocked. An Owner can remove the lock first and then delete, which adds a deliberate extra step.

??? question "How do CanNotDelete and ReadOnly locks differ?"
    CanNotDelete allows reading and changing but blocks deleting. ReadOnly blocks changing and deleting.

??? question "Does an Azure budget stop spending when the limit is reached?"
    No. A budget sends alerts. It does not stop spending.

??? question "If a policy is assigned on a management group, what does it reach?"
    Every subscription under that group, and everything inside those subscriptions, through inheritance.

??? question "Why did the cleanup fail while the lab group was locked?"
    A lock inherits downward, so it also protects the role assignment and policy assignment stored inside the group. The lock had to be lifted first and restored afterwards.
