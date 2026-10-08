import pathlib

UPDATED = "October 8, 2026"
P, PT, E, N = "Practised", "Partly practised", "Explained", "Not started"

DOMAINS = [
    ("Manage Azure identities and governance", "20 to 25%", [
        ("Users and groups", [
            ("Create users and groups", P, "Day 2, portal and CLI"),
            ("Manage user and group properties", N, ""),
            ("Manage licenses in Microsoft Entra ID", E, "Day 2, license tiers"),
            ("Manage external users", N, ""),
            ("Configure self-service password reset", N, ""),
        ]),
        ("Access to Azure resources", [
            ("Use built-in Azure roles", P, "Day 2"),
            ("Assign roles at different scopes", P, "Day 2"),
            ("Interpret access assignments", P, "Day 2, direct and inherited"),
        ]),
        ("Subscriptions and governance", [
            ("Implement and manage Azure Policy", P, "Day 3, Modify and Deny"),
            ("Configure resource locks", P, "Day 3"),
            ("Apply and manage tags", P, "Day 3"),
            ("Manage resource groups", P, "Days 1 and 3"),
            ("Manage subscriptions", E, "Day 1"),
            ("Manage costs with alerts, budgets and Azure Advisor", P, "Budget alert and Advisor"),
            ("Configure management groups", P, "Day 3"),
        ]),
    ]),
    ("Implement and manage storage", "15 to 20%", [
        ("Access to storage", [
            ("Configure storage firewalls and virtual networks", N, ""),
            ("Create and use shared access signature tokens", N, ""),
            ("Configure stored access policies", N, ""),
            ("Manage access keys", N, ""),
            ("Configure identity-based access for Azure Files", N, ""),
        ]),
        ("Storage accounts", [
            ("Create and configure storage accounts", N, ""),
            ("Configure storage redundancy", N, ""),
            ("Configure object replication", N, ""),
            ("Configure storage account encryption", N, ""),
            ("Manage data with Storage Explorer and AzCopy", N, ""),
        ]),
        ("Azure Files and Blob Storage", [
            ("Create and configure a file share", N, ""),
            ("Create and configure a blob container", N, ""),
            ("Configure storage tiers", N, ""),
            ("Configure soft delete for blobs and containers", N, ""),
            ("Configure snapshots and soft delete for Azure Files", N, ""),
            ("Configure blob lifecycle management", N, ""),
            ("Configure blob versioning", N, ""),
        ]),
    ]),
    ("Deploy and manage Azure compute resources", "20 to 25%", [
        ("ARM templates and Bicep", [
            ("Interpret an ARM template or a Bicep file", N, ""),
            ("Modify an existing ARM template", N, ""),
            ("Modify an existing Bicep file", N, ""),
            ("Deploy resources from a template or Bicep file", N, ""),
            ("Export a deployment as a template, or convert a template to Bicep", N, ""),
        ]),
        ("Virtual machines", [
            ("Create a virtual machine", N, ""),
            ("Configure encryption at host", N, ""),
            ("Move a VM to another resource group, subscription or region", N, ""),
            ("Manage VM sizes", N, ""),
            ("Manage VM disks", N, ""),
            ("Deploy VMs to availability zones and availability sets", E, "Day 1"),
            ("Deploy and configure virtual machine scale sets", N, ""),
        ]),
        ("Containers", [
            ("Create and manage an Azure Container Registry", N, ""),
            ("Provision a container with Azure Container Instances", N, ""),
            ("Provision a container with Azure Container Apps", N, ""),
            ("Manage sizing and scaling for containers", N, ""),
        ]),
        ("Azure App Service", [
            ("Provision an App Service plan", N, ""),
            ("Configure scaling for an App Service plan", N, ""),
            ("Create an App Service", N, ""),
            ("Configure certificates and TLS", N, ""),
            ("Map an existing custom DNS name", N, ""),
            ("Configure backup for an App Service", N, ""),
            ("Configure networking settings", N, ""),
            ("Configure deployment slots", N, ""),
        ]),
    ]),
    ("Implement and manage virtual networking", "15 to 20%", [
        ("Virtual networks", [
            ("Create and configure virtual networks and subnets", N, ""),
            ("Create and configure virtual network peering", N, ""),
            ("Configure public IP addresses", N, ""),
            ("Configure user-defined routes", N, ""),
            ("Troubleshoot network connectivity", N, ""),
        ]),
        ("Secure access to virtual networks", [
            ("Create and configure NSGs and application security groups", N, ""),
            ("Evaluate effective security rules in NSGs", N, ""),
            ("Implement Azure Bastion", N, ""),
            ("Configure service endpoints for PaaS", N, ""),
            ("Configure private endpoints for PaaS", N, ""),
        ]),
        ("Name resolution and load balancing", [
            ("Configure Azure DNS", N, ""),
            ("Configure an internal or public load balancer", N, ""),
            ("Troubleshoot load balancing", N, ""),
        ]),
    ]),
    ("Monitor and maintain Azure resources", "10 to 15%", [
        ("Monitoring", [
            ("Interpret metrics in Azure Monitor", N, ""),
            ("Configure log settings in Azure Monitor", N, ""),
            ("Query and analyze logs in Azure Monitor", N, ""),
            ("Set up alert rules, action groups and alert processing rules", N, ""),
            ("Configure and interpret Azure Monitor Insights for VMs, storage and networks", N, ""),
            ("Use Network Watcher and Connection monitor", N, ""),
        ]),
        ("Backup and recovery", [
            ("Create a Recovery Services vault", N, ""),
            ("Create an Azure Backup vault", N, ""),
            ("Create and configure a backup policy", N, ""),
            ("Perform backup and restore operations", N, ""),
            ("Configure Azure Site Recovery for Azure resources", N, ""),
            ("Perform a failover to a secondary region with Site Recovery", N, ""),
            ("Configure and interpret backup reports and alerts", N, ""),
        ]),
    ]),
]

def table(rows):
    out = ["| Objective | Status | Notes |", "|---|---|---|"]
    out += [f"| {o} | {s} | {n} |" for o, s, n in rows]
    return "\n".join(out)

counts = {P: 0, PT: 0, E: 0, N: 0}
total = 0
body = []
for dom, weight, groups in DOMAINS:
    body.append(f"## {dom} ({weight} of the exam)\n")
    for g, rows in groups:
        body.append(f"### {g}\n")
        body.append(table(rows) + "\n")
        for _, s, _ in rows:
            counts[s] += 1
            total += 1

head = f"""# AZ-104 Objective Tracker

An honest map of where I stand against the official exam objectives for Azure Administrator.

**Source:** the [Microsoft Learn study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-104), skills measured as of April 17, 2026. The objectives below are paraphrased, and Microsoft's page is the authority.

**Progress on {UPDATED}:** {counts[P]} practised, {counts[PT]} partly practised, {counts[E]} explained only, {counts[N]} not started, out of {total} objectives.

- **Practised:** built or run in my own lab
- **Partly practised:** some of it built
- **Explained:** studied and discussed, not yet built
- **Not started:** not covered yet

"""
out = pathlib.Path("docs/exam-tracker/az-104.md")
out.write_text(head + "\n".join(body))
print("written:", dict(counts), "total", total)
