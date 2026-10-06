# Day 2: Identity and Access

**Date:** October 6, 2026

**Status:** Phase 1, Week 1

## Outcome

Built and tested read-only access for an auditor on `rg-vestlux-lab`, first in the portal and then with the Azure CLI, and verified the result with both the CLI and PowerShell.

## Microsoft Entra ID

Entra ID is the cloud directory that answers who you are. It holds users, groups and application identities. Authentication proves identity (password, MFA). Authorization decides what that identity may do.

The tenant runs the Free license, which covers users, groups, Azure RBAC and single sign-on. Conditional Access, dynamic groups and Privileged Identity Management need P1 or P2 licenses.

Entra ID is a different product from on-premises Active Directory. It uses OAuth, SAML and OpenID Connect over HTTPS, has a flat structure without OUs or GPOs, and is connected to AD DS later with Entra Connect.

## Azure RBAC

A role assignment has three parts: who (a user or group), what (a role) and where (a scope).

- **Owner:** everything, including granting access to others
- **Contributor:** everything except granting access
- **Reader:** view only
- **User Access Administrator:** manages access only

Scope inherits downward, permissions add up, and there is no simple deny. Roles are assigned to groups, so a joiner or leaver is handled by group membership alone.

Entra roles control the directory (users, groups, licenses). Azure roles control resources (VMs, storage, resource groups). Being Global Administrator gives no rights over Azure resources by default.

## What I built

1. Created the security group `grp-auditors` and a test user, and added the user to the group.
2. Assigned Reader on `rg-vestlux-lab` to the group, not to the user.
3. Signed in as the test user in a private window and tried to add a tag. The portal showed the form, and Apply failed with `AuthorizationFailed`. Check access showed one Reader assignment, inherited through the group, and no deny assignments.
4. Repeated the build with the CLI: created a second group, assigned Reader with `az role assignment create`, and verified with `az role assignment list` and `Get-AzRoleAssignment`.
5. Cleaned up the CLI test group, removing its role assignment first and then the group, so no orphaned assignment is left behind.

## Issues met and how I fixed them

1. **The CLI rejected my role assignment command.** I had used `--resource-group`, but `az role assignment create` requires `--scope`, the full resource ID. I read the ID with `az group show` into a variable and passed that instead.
2. **The CLI list did not show my Owner role, but PowerShell did.** Owner is assigned at the subscription. `az role assignment list` shows only assignments at the exact scope unless `--include-inherited` is added, while `Get-AzRoleAssignment` includes inherited ones by default.

## Findings

- The portal shows forms to users who cannot save them. The check happens in ARM when the request arrives, which returns `AuthorizationFailed`.
- A Reader cannot register resource providers, so creating a VM was blocked before any permission check on the VM itself.
- The refused tag write did not appear in the Activity log of the resource group in this test. The role assignment did, with my account as the initiator.

## Summary

- Entra ID holds identities. Authentication proves who you are, authorization decides what you may do.
- A role assignment is who, what and where. Assign roles to groups.
- Owner can grant access, Contributor cannot, Reader can only view.
- Scope inherits downward, so always check both direct and inherited assignments.
- Entra roles manage the directory, Azure roles manage resources.
- The portal, the CLI and PowerShell all build the same assignment, because ARM is the single front door.

## Revision questions

??? question "What is the difference between authentication and authorization?"
    Authentication proves who you are, for example with a password and MFA. Authorization decides what you are allowed to do, which in Azure is handled by RBAC.

??? question "What are the three parts of a role assignment?"
    Who gets access (a user or group), what they may do (the role) and where it applies (the scope).

??? question "What can Contributor do that Reader cannot, and what can Owner do that Contributor cannot?"
    Contributor can create, change and delete resources. Owner can also grant access to others by assigning roles.

??? question "A user is Reader on the subscription and Contributor on one resource group. What can they do inside that group?"
    Manage every resource in it, because permissions add up, but not assign roles. Outside the group they can only read.

??? question "Why assign roles to groups and not to individual users?"
    One change to group membership updates access everywhere, access stays consistent, and an audit has one place to look.

??? question "What is the difference between an Entra role and an Azure role?"
    Entra roles control the directory (users, groups, apps, licenses). Azure roles control access to resources. A Global Administrator has no rights over Azure resources by default.

??? question "Why did PowerShell list an assignment that the CLI list did not?"
    That assignment was inherited from the subscription. `Get-AzRoleAssignment` shows inherited assignments by default, while `az role assignment list` needs `--include-inherited`.

??? question "Why can a user open a form in the portal and still be refused when saving?"
    The portal only shows the interface. Authorization is enforced by ARM when the request is sent, and a Reader's write is refused with `AuthorizationFailed`.

??? question "Why delete the role assignment before deleting the group?"
    If the group is deleted first, the assignment stays behind as an orphan pointing to an identity that no longer exists.
