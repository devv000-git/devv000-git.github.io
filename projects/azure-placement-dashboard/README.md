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

## Evidence and code to add

The source logbook says GitHub code was pushed, but the relevant repository **is not in the connected GitHub repository set**. The following files are not currently available to verify:

- Actual React component and routing source.
- Python Azure Functions, API definitions and validation logic.
- Terraform configuration and deployment manifest.
- Import script with duplicate-handling implementation.
- App screenshots and deployment/CRUD test outputs.
- Security controls, authentication or identity configuration.

Do not present this project as a production-secure application until those controls can be inspected.

## Publication boundaries

The private placement logbook itself is **not** published. This public description excludes company records, customer information, subscription IDs, credentials and infrastructure secrets.

[Full placement case study](https://devv000-git.github.io/industry-projects.html#dashboard)
