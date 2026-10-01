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
