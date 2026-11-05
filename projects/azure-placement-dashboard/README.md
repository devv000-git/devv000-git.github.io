# Azure Placement Task Dashboard | React, Python and Terraform

**Context:** CloudVantage IT Support & Cloud Analyst industry placement  
**Evidence:** Placement logbook entries dated **3 and 4 September 2026**, with supporting Python reflection on 22 September  
**Stack recorded:** React, Azure Static Web Apps, Python Azure Functions, Azure Table Storage, Azure Storage, Terraform, GitHub

## Situation

Placement activities and their evidence needed a consistent place to be recorded and managed. The placement included building and demonstrating a cloud-hosted dashboard application.

## Task

Build and deploy a minimum viable task-management dashboard with a hosted frontend, backend API and persistent Azure data storage.

## Action

### 3 September 2026: infrastructure provisioning

The placement logbook states that Terraform was used to define and configure the project's resource group, storage account, Azure Table Storage, Blob Storage container, App Service Plan, Azure Function App and Azure Static Web App configuration. Azure resource configuration was reviewed after deployment.

### 4 September 2026: deployed application test

The logbook states that:

- The **React frontend** was hosted with Azure Static Web Apps.
- A **Python Azure Functions backend** was connected to the frontend.
- **Azure Table Storage** was used to store placement task records.
- The live deployment was tested by **creating, viewing, editing and deleting** records.
- Code, Terraform configuration and an import script were pushed to GitHub.
- The MVP was demonstrated to the placement supervisor, who discussed the stack and architecture.

### 22 September 2026: supporting automation

A later entry describes importing placement records through API requests with duplicate checks. The implementation includes import logic, although no verified migration totals or timings are reported.

## Application architecture

```text
Browser
  ↓
React frontend (Azure Static Web Apps)
  ↓ API calls
Python Azure Functions backend
  ↓ record operations
Azure Table Storage
  ↑
Python import script (API requests with duplicate checks)

Terraform → Resource group, storage account / Blob container,
            Azure Functions / hosting resources, Static Web App
```

This simplified architecture is consistent with the React, Python and Terraform implementation and the documented deployment.

## Result

The logbook documents a **deployed and demonstrated MVP** whose task records were tested with create, read, update and delete operations. Unlike the Azure security monitoring lab, this work documents a successful **application-level functional test**. It does not establish load testing, production user adoption, access-control hardening, continuous availability or measured performance.

## STAR narrative

**Situation:** Placement work needed practical cloud-backed task tracking.  
**Task:** Deliver an application MVP integrating frontend, backend and persistence.  
**Action:** Provisioned Azure resources with Terraform, connected a React frontend to Python Functions and Table Storage, tested CRUD tasks and demonstrated the deployed application.  
**Result:** A functioning cloud-hosted MVP was recorded in the placement logbook and shown to the supervisor.

## Implementation and source evidence

The project includes a React/Vite user interface, a Python Azure Functions backend, Terraform infrastructure definitions and supporting import logic. These components support the following functional capabilities:

| Original source | What it demonstrates |
| --- | --- |
| `frontend/src/App.jsx` | React task state, dynamic form, skills selection, WHAT / SO WHAT / NOW WHAT reflection and CRUD controls |
| `frontend/src/api.js` | GET, POST, PUT and DELETE requests to the task API, configured through `VITE_API_BASE_URL` |
| `backend/azure-functions/function_app.py` | Python HTTP routes and Azure Table Storage entity operations |
| `terraform/main.tf` | Resource group, storage account/table, private Blob container, Linux Functions App, service plan and Azure Static Web App |
| `scripts/import_full_logbook.py` | Existing-task checks and logbook import logic, withheld because it includes original placement entries |

These implementation details complement the functional testing recorded during the placement.

## Interactive public demonstration

[**Try the privacy-safe task dashboard demo**](https://devv000-git.github.io/demos/placement-dashboard/)

The public demo uses fictional examples and browser-local storage. It does not connect to Azure, authenticate to the original backend, or publish actual placement records. It recreates the core interaction in standalone HTML/JavaScript. The **original application was written in React** and connected to Azure Functions and Table Storage.

The following sanitised code examples are published for recruiter review:

- [Adapted React dashboard component](code-examples/frontend/TaskDashboardExcerpt.jsx), covering state, hour totals, reflections and CRUD controls
- [Frontend API client](code-examples/frontend/api.js)
- [Python Azure Functions implementation reference](code-examples/backend/function_app_reference.py)
- [Anonymised Terraform Azure resource map](code-examples/terraform/azure-resources.tf)
- [Architecture and engineering review](../../docs/placement-dashboard-source-review.md)

## Security and release scope

The original dashboard was a supervised placement MVP. User authentication was not completed, and the implementation is **not presented as a secure production deployment**. A future cloud release would require identity controls, authorisation, stricter input validation and secure configuration management.

The public demonstration uses fictional data stored in the browser, with no calls to the historical Azure application or access to real placement information. The published Python and Terraform samples are anonymised or adapted for explanation and do not form a ready-to-deploy system.

## Additional evidence that would strengthen the project

- Redacted screenshots of the originally deployed Azure application and infrastructure.
- Successful function and storage logging output from the original deployment.
- Confirmation of the source code's sharing permissions under the placement agreement.
- A redesigned, authenticated deployment if the application is to be used again with real records.

## Publication boundaries

Only technical descriptions, selected code examples and fictional demonstration data are shared publicly. Company records, real task entries and environment-specific settings are excluded.

[Full placement case study](https://devv000-git.github.io/industry-projects.html#dashboard)
