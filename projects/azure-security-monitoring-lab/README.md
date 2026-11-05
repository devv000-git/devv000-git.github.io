# Azure Security Monitoring Lab | CloudVantage Placement

**Context:** Personal learning lab developed during an IT Support & Cloud Analyst placement  
**Primary evidence:** Placement logbook, dated 7–11 September 2026  
**Location:** Australia East Azure region  
**Technologies:** Azure Virtual Machines, VNets, Network Security Groups, Azure Monitor, Data Collection Rules, Log Analytics, Microsoft Sentinel, Microsoft Entra ID, Azure Budget

## Situation

During an industry placement, I wanted a practical lab to understand how endpoint, network and identity telemetry fits into Azure's security monitoring tools. The environment was built as a learning exercise in an Azure for Students tenant, not a production company SOC.

## Task

Create a minimally exposed Windows Server lab, connect it to a central Log Analytics workspace, explore Microsoft Sentinel and identity diagnostics, and account for the cost of cloud resources.

## Action and dated evidence

| Date | Logbook evidence | Interpretation |
| --- | --- | --- |
| **7 Sep 2026** | Created a dedicated resource group in Australia East, created a Log Analytics workspace, and enabled Sentinel on the workspace. | Initial monitoring environment established |
| **8 Sep 2026** | Deployed a Windows Server VM with VNet, subnet, public IP, NIC and NSG. Restricted inbound RDP to an explicitly permitted source IP. | A least-exposure network control was configured |
| **9 Sep 2026** | Created a Data Collection Rule for Windows Event Logs, linked the rule to the VM, and configured delivery to Log Analytics. | A log collection path was configured. Successful sustained ingestion or alert firing is not established solely by the logbook |
| **10 Sep 2026** | Created an Azure cost budget and **began implementing** a custom Azure Policy intended to enforce VM auto-shutdown. | Budget established. The policy's completion and enforcement are **not** proved |
| **11 Sep 2026** | Configured Microsoft Entra diagnostic settings intended to forward identity audit logs to Log Analytics. The source explicitly records a licensing limitation in the Azure for Students tenant. | Configuration attempt documented. **Full Entra log ingestion was not available** |

The logbook also records a supervisor reviewing the lab work and recommending cloud-service comparisons and cost awareness. That feedback is reflective, not an independent technical acceptance test.

## Recorded architecture

```text
Azure subscription (student lab)
└── Resource group (Australia East)
    ├── Windows Server virtual machine
    │   └── VNet / Subnet / NIC / NSG
    │       └── RDP inbound restricted to an individual source IP
    ├── Azure Monitor Data Collection Rule
    │   └── Configured Windows Event Logs from the VM
    ├── Log Analytics workspace
    │   ├── Destination for the Windows event data collection rule
    │   └── Microsoft Sentinel enabled on the workspace
    ├── Budget
    └── Custom VM auto-shutdown Azure Policy (work in progress)

Microsoft Entra diagnostic settings
└── Intended audit-log forwarding to Log Analytics
    └── Full ingestion limited by licensing
```

This diagram is **reconstructed from logbook text**, not exported from the Azure portal.

## Defensive interpretation

The strongest documented security decision is the restricted RDP access. The VM's RDP rule was limited to a permitted source IP rather than unrestricted internet access. The collection rule establishes how Windows Event Logs were intended to reach Azure Monitor and Log Analytics.

**Do not overstate:** The logbook does not contain an alert investigation, detection results, specific KQL queries, event counts, incident-response outcomes, or proof that the auto-shutdown policy was effective. Those claims require additional original evidence.

## STAR narrative

**Situation:** Needed hands-on experience with Azure security monitoring during an IT Support & Cloud Analyst placement.  
**Task:** Create an Azure lab with controlled VM access and a central Windows event-log collection path.  
**Action:** Provisioned a VM, network and NSG restrictions, configured a Log Analytics workspace and Data Collection Rule, enabled Sentinel and explored Entra logging and cloud budgeting.  
**Result:** Documented a configured lab environment and monitoring architecture, with limited Entra log ingestion and unfinished auto-shutdown policy enforcement clearly identified.

## Evidence not yet published

- Original Azure Portal resource list and network rule screenshot.
- Data Collection Rule settings and query outputs confirming data ingestion.
- Microsoft Sentinel configuration screenshots and investigation results, if any.
- Budget and Azure Policy screenshots confirming actual enforcement.
- Azure Entra diagnostic configuration and details of licensing restrictions.

This public case study excludes internal resource identifiers and network addresses. It is based on documented configuration steps and does not include a running cloud environment.

## Related evidence

[Full placement case study](https://devv000-git.github.io/industry-projects.html#cloudvantage)
