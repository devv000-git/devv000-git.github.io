# Original VS Code project source review

**Source:** `internship-portfolio-portal.zip`, privately uploaded in November 2026  
**Project:** CloudVantage placement task dashboard (SIT306)  
**Review scope:** React UI, client-side API adapter, Python Azure Functions, Terraform, import scripts, documentation and files that could contain secrets

## Actual source layout verified

| Source path in the private ZIP | Reviewed finding |
| --- | --- |
| `frontend/src/App.jsx` | React state hooks, form for activity title, date, hours, category, status, WHAT/SO WHAT/NOW WHAT, skills, editing and deleting tasks |
| `frontend/src/api.js` | Fetch-based client for GET/POST `/tasks` and PUT/DELETE `/tasks/{id}`, with base URL supplied by `VITE_API_BASE_URL` |
| `frontend/src/styles.css` | Responsive card layout and forms, including a narrower mobile layout |
| `backend/azure-functions/function_app.py` | Python HTTP-triggered Azure Functions using `TableServiceClient`, partition/row keys and CRUD operations against Azure Table Storage |
| `terraform/main.tf` | Azure resource group, storage account, table, private evidence container, service plan, Linux Functions App and Static Web App |
| `scripts/import_logbook.py` and `import_full_logbook.py` | Placement-data import scripts containing personal reflections and real task material. **Not republished** |
| `docs/project-documentation.md` | Source architecture, features, configuration and discussion of unresolved Entra authentication permission requirements |
| `backend/template.yaml` and `terraform/aws-backup/` | Earlier AWS SAM/DynamoDB/S3 starter files. **Not evidence that the final Azure app used AWS** |

The source's `README.md` still describes the earlier AWS starter. The more detailed documentation and the actual Azure implementation establish the final Azure architecture. This case study does not conflate these.

## Strong technical evidence

- **UI and workflow:** React state and memoisation track tasks, completion and total placement hours; the original form supports adding, editing and deleting entries.
- **API design:** The Python Functions app exposes REST-style task endpoints and translates records to/from an Azure Table Storage schema.
- **Cloud deployment model:** Terraform configures infrastructure, references a private Blob container, sets `https_only = true` and configures explicit frontend CORS origins.
- **Data import:** The source contains an import workflow using HTTP requests and existing-task checks, but private entry contents have been excluded.
- **Dated placement result:** The separate uploaded logbook records deployed testing of create, read, update and delete operations, plus a demonstration to the supervisor.

## Security observations

### High priority: authentication

The original backend configures `func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)`, exposing task operations without Function-level authentication or an enforceable user identity in the inspected code. Its source documentation explicitly states that attempted Microsoft Entra integration was removed after administrator approval was unavailable.

**Do not publish the actual live backend URL or invite recruiters to test it.** If the original Function App remains accessible, restrict it until organisation-approved identity and authorisation are in place. A CORS allowlist prevents some cross-origin browser requests but does **not** prevent direct unauthenticated requests.

The public [Python reference](../projects/azure-placement-dashboard/code-examples/backend/function_app_reference.py) is **security-adjusted for documentation** and uses `FUNCTION` rather than the original `ANONYMOUS`. Function keys themselves must never be put into frontend JavaScript and are not a replacement for proper end-user authentication.

### High priority: credentials in the private archive

The source ZIP contains an actual `frontend/.env`, `backend/azure-functions/local.settings.json`, `terraform/terraform.tfstate` and a Terraform state backup. The settings include storage connection strings and the state contains credential fields. **These files were not published.** The archive also includes its prior `.git` history and thousands of dependency artifacts.

If the underlying storage account is still active, rotate its keys. Check whether any secret-bearing copies were ever pushed to remote repositories or shared elsewhere. Do not assume `.gitignore` removes files already present in a Git history.

### Other limitations

- Limited input validation and broad exception catches appear in the original API code.
- The deployment was a placement MVP, not a formally security-tested production service.
- Cloud cost, auth, uptime and load test results were not verified in the source.
- The original import scripts contain individual placement entries and should not be published.
- Azure identifiers and service URLs have been withheld from public documentation.

## What's publicly available

- [Static browser-only demo](https://devv000-git.github.io/demos/placement-dashboard/) with fictional tasks, editing, deletion and browser-local data.
- [Original-structure front-end API reference](../projects/azure-placement-dashboard/code-examples/frontend/api.js), showing the historic Azure task routes but no endpoint.
- [Security-adjusted Python Functions reference](../projects/azure-placement-dashboard/code-examples/backend/function_app_reference.py).
- [Anonymised Terraform resource map](../projects/azure-placement-dashboard/code-examples/terraform/azure-resources.tf).

The public preview is a **new static HTML/JavaScript recreation**, not the original React bundle. The original React frontend is preserved in the sanitized source ZIP supplied privately in the conversation. No real data or Azure API connections are used in the public preview.

## Checks

The standalone local demo was exercised in a headless browser with fictional tasks for create, edit and delete, and a mobile width check. The separate GitHub preview uses the same privacy-safe approach but should not be represented as a production app or an audited security product.

## Copyright and publication

The project is described as a placement project. Before uploading full organisational code, deployments, customer materials or screenshots, confirm relevant internship and organisation sharing rules. The public source examples are trimmed and anonymised. This is not a claim of exclusive ownership of all third-party material.
