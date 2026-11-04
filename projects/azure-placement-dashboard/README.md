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

A later entry describes the Python import script using API requests to migrate placement records to Azure Table Storage with duplicate checks. The logbook does not include its actual source code or measured migration result.

## Architecture reconstructed from the logbook

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

This is **a text architecture reconstruction from recorded implementation steps**. It should be replaced by an actual configuration diagram when the original code becomes available.

## Result

The logbook documents a **deployed and demonstrated MVP** whose task records were tested with create, read, update and delete operations. Unlike the Azure security monitoring lab, this work documents a successful **application-level functional test**. It does not establish load testing, production user adoption, access-control hardening, continuous availability or measured performance.

## STAR narrative

**Situation:** Placement work needed practical cloud-backed task tracking.  
**Task:** Deliver an application MVP integrating frontend, backend and persistence.  
**Action:** Provisioned Azure resources with Terraform, connected a React frontend to Python Functions and Table Storage, tested CRUD tasks and demonstrated the deployed application.  
**Result:** A functioning cloud-hosted MVP was recorded in the placement logbook and shown to the supervisor.

## Verified source files from the original VS Code project

I have now reviewed the full `internship-portfolio-portal.zip` supplied by the project owner. It contains the original React/Vite UI, the Python Azure Functions backend, Terraform infrastructure, import scripts and detailed documentation.

| Original source | What it demonstrates |
| --- | --- |
| `frontend/src/App.jsx` | React task state, dynamic form, skills selection, WHAT / SO WHAT / NOW WHAT reflection and CRUD controls |
| `frontend/src/api.js` | GET, POST, PUT and DELETE requests to the task API, configured through `VITE_API_BASE_URL` |
| `backend/azure-functions/function_app.py` | Python HTTP routes and Azure Table Storage entity operations |
| `terraform/main.tf` | Resource group, storage account/table, private Blob container, Linux Functions App, service plan and Azure Static Web App |
| `scripts/import_full_logbook.py` | Existing-task checks and logbook import logic, withheld because it includes original placement entries |

These are **source-verified technical features**, not just descriptions from a logbook.

## Interactive public demonstration

[**Try the privacy-safe task dashboard demo**](https://devv000-git.github.io/demos/placement-dashboard/)

The public demo uses fictional examples and browser-local storage. It does not connect to Azure, authenticate to the original backend, or publish actual placement records. It recreates the core interaction in standalone HTML/JavaScript. The **original application was written in React** and connected to Azure Functions and Table Storage.

The following sanitised code examples are published for recruiter review:

- [Adapted React dashboard component](code-examples/frontend/TaskDashboardExcerpt.jsx), covering state, hour totals, reflections and CRUD controls
- [Frontend API client](code-examples/frontend/api.js)
- [Python Azure Functions implementation reference](code-examples/backend/function_app_reference.py)
- [Anonymised Terraform Azure resource map](code-examples/terraform/azure-resources.tf)
- [Original ZIP source review and security notes](../../docs/placement-dashboard-source-review.md)

## Security review and limits

The uploaded project contained `.env`, Azure Functions `local.settings.json`, Terraform state and backup files, prior Git history and original placement entries. These **are excluded from public publication**.

The original Python Functions app used **anonymous HTTP authorization** for task CRUD. The documentation explains that Microsoft Entra integration was deferred because the tenant required administrator approval. CORS and HTTPS settings do not provide end-user authentication. The public demo intentionally does not call this API. The public Python reference is security-adjusted, not an unchanged copy of the original.

If the original Azure storage account is still active, its keys should be rotated because the private archive contains credential-bearing settings and Terraform state. Any new live backend requires proper identity, authorisation and access controls.

## Additional evidence that would strengthen the project

- Redacted screenshots of the originally deployed Azure application and infrastructure.
- Successful function and storage logging output from the original deployment.
- Confirmation of the source code's sharing permissions under the placement agreement.
- A redesigned, authenticated deployment if the application is to be used again with real records.

## Publication boundaries

The private placement logbook itself is **not** published. This public description excludes company records, customer information, subscription IDs, credentials and infrastructure secrets.

[Full placement case study](https://devv000-git.github.io/industry-projects.html#dashboard)
