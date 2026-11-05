# Azure Placement Dashboard | Architecture and Engineering Review

**Context:** CloudVantage IT Support & Cloud Analyst placement, September 2026  
**Application type:** Cloud-hosted placement activity dashboard  
**Technologies:** React, Vite, Python, Azure Functions, Azure Table Storage, Terraform and Azure Static Web Apps

## Architecture

The project uses a React frontend to manage placement tasks and a Python Azure Functions API for task operations. Azure Table Storage provides persistence. Terraform defines the related hosting and storage infrastructure.

```text
Browser / React (Azure Static Web Apps)
          |
          | Task requests (HTTP)
          v
Python API (Azure Functions)
          |
          | Read / write task entities
          v
Azure Table Storage

Terraform defines hosting and storage resources.
```

### Frontend

The React interface includes task title, date, recorded hours, category, status, three reflection fields (WHAT, SO WHAT, NOW WHAT) and professional skill mapping. It calculates totals and task progress and supports editing and deletion.

The client adapter implements GET and POST requests to `/tasks` and PUT and DELETE requests to `/tasks/{id}`. The endpoint base URL is a deployment setting rather than a hard-coded public service address.

### Backend

The Python Azure Functions implementation maps request data to Azure Table Storage records. Its operations cover listing, creating, updating and deleting tasks. It uses entity identifiers and a partition/row-key structure.

### Infrastructure

The Terraform configuration describes Azure hosting and persistence resources, including a resource group, storage account, task table, private Blob container, hosting plan, Linux Function App and Static Web App. The historical deployment used Azure infrastructure for the frontend and API.

### Supporting automation

A Python import workflow was used to prepare placement activity records and check for duplicates. No genuine placement records are distributed as part of this case study.

## Documented outcome

The placement activity record documents a deployed minimum viable product tested through creation, viewing, updating and deleting task entries. The application was demonstrated to the placement supervisor. These are functional checks, not results from an independent production security or performance assessment.

## Security considerations

The historical application was built as a **placement MVP**. It did not complete end-user identity integration and should not be treated as a production-ready, multi-user service.

A production deployment would need:

1. End-user authentication and per-user authorisation.
2. Server-side input validation and consistent error handling.
3. Secure configuration and credential management.
4. Audit logging, monitoring and deployment review.

The [public Python API reference](../projects/azure-placement-dashboard/code-examples/backend/function_app_reference.py) is a **sanitised, security-adjusted illustration**, not a claim that the historical system was hardened. Function-level access settings alone are not sufficient for a browser-facing multi-user service.

## Explore the implementation

- [React component excerpt](../projects/azure-placement-dashboard/code-examples/frontend/TaskDashboardExcerpt.jsx), adapted from the original application.
- [Frontend API adapter](../projects/azure-placement-dashboard/code-examples/frontend/api.js).
- [Python Azure Functions reference](../projects/azure-placement-dashboard/code-examples/backend/function_app_reference.py).
- [Terraform resource map](../projects/azure-placement-dashboard/code-examples/terraform/azure-resources.tf).
- [Browser-only demonstration](https://devv000-git.github.io/demos/placement-dashboard/).

**About the demo:** The public demo is a standalone browser-based recreation using fictional tasks and local browser storage. It does not call the original cloud API or contain actual placement records. The original deployed frontend used React and a cloud backend.

The shared code extracts and demo are examples for reviewing technical approach. They are not a packaged or supported production deployment.
