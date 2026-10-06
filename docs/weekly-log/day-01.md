# Polaris Day 1: Azure fundamentals

## Structure of an Azure environment

Identity is held in the Entra tenant. Below it sit management groups (optional), subscriptions (the billing and limits boundary), resource groups (containers for things deployed and deleted together) and resources. Access and policy are inherited downwards.

My lab has one subscription directly under the tenant, with one resource group, `rg-vestlux-lab`.

## Resilience model

Availability zones protect against the loss of one datacenter, but only when at least two VMs are spread across different zones. Region pairs protect against the loss of a whole region.

Not every region has zones. I confirmed with `az account list-locations` that West Europe has three zones and UK West has none.

For a bank with EU data rules, the design is two VMs in two zones in West Europe, with North Europe as the paired recovery region.

## Azure Resource Manager

The portal, CLI and PowerShell all send requests to ARM, which checks who you are, what you may do and which company rules apply, then passes the request to the right service.

Every change is recorded in the Activity log with the account that made it. I tested this by adding a tag to `rg-vestlux-lab` with the CLI, then finding the entry in the portal. Reading information is not logged, only changes.

## Issues met and how I fixed them

1. **Cloud Shell showed a warning about registration.** Azure services must be switched on for a subscription before they can be used, and Cloud Shell was not switched on yet. I enabled it with `az provider register --namespace Microsoft.CloudShell`. The warning stopped appearing.

2. **The zone information was missing from my command output.** The table view hides detailed data. I ran the same command with JSON output and could then see the zones for West Europe.

3. **The Activity log showed nothing at first.** The log only records changes, and I had only been reading. After I added a tag to the resource group, the change appeared with my account name.


## Summary

- The Azure hierarchy runs tenant, management groups, subscription, resource group, resource. Access and policy inherit downward.
- A subscription is the billing and limits boundary. A resource group holds resources that share a lifecycle.
- Availability zones protect against losing one datacenter, but only with two or more VMs in different zones. A region pair protects against losing a whole region.
- Not every region has zones. `az account list-locations` shows the zone mappings for the regions that do.
- ARM is the single front door for the portal, the CLI and PowerShell, so all three give the same result. It checks identity, permissions and policy, then passes the request to a resource provider.
- The Activity log records changes, not reads.

## Revision questions

??? question "What is the difference between a subscription and a resource group?"
    A subscription is the boundary for billing, access and limits. A resource group is a container inside it for resources that are deployed, managed and deleted together.

??? question "Why is one VM in one availability zone not protected?"
    If that zone fails, the VM fails with it. Protection needs two or more VMs in different zones, with a load balancer sending traffic only to the healthy ones.

??? question "What does a region pair protect against, and which pair suits an EU-bound workload?"
    It protects against the loss of a whole region and is the basis for a disaster recovery design. West Europe (Netherlands) paired with North Europe (Ireland) keeps both sites in the EU.

??? question "Does every Azure region have availability zones?"
    No. West Europe has three, UK West has none. The command `az account list-locations` returns zone mappings only for regions that have them.

??? question "Why do the portal, the CLI and PowerShell all give the same result?"
    They all send their requests to Azure Resource Manager, the single front door.

??? question "What does ARM do with each request?"
    It checks who you are, what you are allowed to do and which policies apply, then passes the request to the right resource provider and records changes in the Activity log.

??? question "What is a resource provider, and what happens if it is not registered?"
    A resource provider is the service that delivers one kind of resource, for example Microsoft.Compute for VMs. A subscription must register it before creating that resource type, otherwise the deployment fails with a registration error.

??? question "Does the Activity log record reads?"
    No. Only changes such as create, update and delete are recorded, each with the account that made them.
