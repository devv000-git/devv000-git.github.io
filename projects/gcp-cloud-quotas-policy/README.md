# GCP Cloud Quotas | Terraform Policy-as-Code

**Project:** Hardhat Enterprises, Policy Deployment Engine  
**Verified contribution:** [PR #393: Add Cloud Quotas policies and documentation](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393), authored by `devv000-git`, merged on **23 May 2026**  
**Technology:** Google Cloud Quotas, Terraform, OPA/Rego, security documentation and test fixtures

## Situation

Quota configuration can affect cloud availability, operational limits and guardrails. PDE needed documented security decisions and reusable policy checks for Google Cloud Quotas Terraform resources.

## Task

Contribute policies and examples for:

- `google_cloud_quotas_quota_adjuster_settings`
- `google_cloud_quotas_quota_preference`

## Action

Merged PR #393 contains **57 changed files**. The historical change set includes:

- Security documentation for Cloud Quotas resources.
- OPA/Rego policy checks for settings including `enablement`, `ignore_safety_checks`, `justification`, `quota_config.preferred_value` and `contact_email`.
- Positive and negative Terraform fixture examples used to illustrate policy expectations.
- Configuration files and resource metadata used by the team workflow.

The project distinguishes potentially unsafe settings, such as bypassing safety checks, from ordinary quota parameter inputs.

## Result

**PR #393 was merged** into the project's `dev` branch on 23 May 2026.

This verifies that the contribution was accepted in the team codebase. It does **not** prove those policies were installed in a production Google Cloud environment, nor does it establish a measured reduction in cloud incidents.

### Important source-history detail

The current `dev` repository tree no longer contains the original Cloud Quotas policy paths introduced by PR #393. The best permanent evidence is the **merged PR diff and its file list**, rather than guessing that historical files still exist at current branch paths.

- [Merged PR #393 with original file changes](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393/files)
- [PR discussion and integration record](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393)

## STAR summary

**Situation:** Cloud quota-related infrastructure settings needed reusable governance controls.  
**Task:** Document security impact and implement example policy checks for Quotas resources.  
**Action:** Prepared Rego rules and compliant/non-compliant Terraform fixtures, backed by resource security documentation.  
**Result:** The contribution was merged through [PR #393](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393).

## Attribution and limitations

This is a contribution within an organisational capstone team. The author of PR #393 is the portfolio owner. The code is not copied into the personal portfolio because the upstream project may have its own reuse requirements. Current production deployment, current file layout and test status are not asserted.
