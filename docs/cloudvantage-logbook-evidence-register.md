# CloudVantage placement logbook: evidence register

## Evidence basis

- Dated CloudVantage placement activity entries, 3 August–24 September 2026.
- Activities record time spent, work completed, technical learning and next steps.
- The documented time total is not presented as total employment hours.
- The project cases below describe technical outcomes supported by these entries.

## Source row mapping

| Workbook row | Date | Project evidence | Qualification |
| --- | --- | --- | --- |
| 17 | 24 Aug | Initial VM deployed in Azure Portal | Initial practice VM, separate from later security lab |
| 18 | 25 Aug | VNet, subnet, NSG, NIC and RDP connectivity reviewed | No network diagram attached |
| 21 | 31 Aug | Started Microsoft Defender recommendation analysis | Research / review, not remediation |
| 22 | 1 Sep | Defender best practices and table, supervisor discussed limited permissions | Access allowed for certain controls, but no implementation result is evidenced |
| 23 | 3 Sep | Terraform resources for placement dashboard | Provisioning described in logbook |
| 24 | 4 Sep | React + Azure Static Web Apps, Python Functions, Table Storage, CRUD test and MVP demo | Functional demonstration explicitly recorded |
| 25 | 7 Sep | Resource group, Log Analytics workspace, Sentinel enabled | Does not prove SOC alert detection |
| 26 | 8 Sep | Windows Server VM and RDP NSG restricted to current public IP | No exact public IP republished |
| 27 | 9 Sep | Windows Event Log Data Collection Rule configured | No actual event counts or KQL output in workbook |
| 28 | 10 Sep | Azure budget created, custom auto-shutdown policy **began** | Does not prove enforcement |
| 29 | 11 Sep | Entra diagnostics configured, licensing restriction | Full Entra ingestion was limited |
| 36 | 22 Sep | Python/API import and duplicate checking described | Import implementation reviewed; migration totals not verified |

## Evidence levels

- **Logbook-supported execution:** Infrastructure creation, dashboard deployment, CRUD testing, VM/network configuration, DCR setup, budget creation and Entra diagnostic configuration.
- **Source-reported supervisor feedback:** Review of dashboard MVP, discussion of Defender recommendations and encouragement of lab development.
- **Configured but not independently proven:** Sustained event ingestion, production-ready Sentinel use and actual Azure Policy enforcement.
- **Explicit limitation:** Licensing prevented full Entra log ingestion.
- **Source reviewed:** React frontend, Python Azure Functions, Terraform infrastructure and importer for the placement dashboard.
- **Further evidence needed:** Portal screenshots, KQL query outputs, monitoring and cost-policy results, and independent deployment metrics.

## Scope and interpretation

The Azure monitoring findings are based on recorded placement activities. The dashboard has additional corroborating implementation files and recorded functional checks. Architecture illustrations are simplified descriptions rather than exports from a running cloud tenancy.

The technical activity records cover August and September 2026, while the broader placement period is listed as July–November 2026. These dates describe different scopes and should not be confused.
