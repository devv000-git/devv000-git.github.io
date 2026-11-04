# Policy Deployment Engine | GCP IAM Security Controls

**Industry capstone:** Hardhat Enterprises, Policy Deployment Engine (PDE)  
**Role documented on LinkedIn:** Policy Author (March–September 2026)  
**Verified contribution:** [Merged pull request #636](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636), authored by `devv000-git`, merged on 1 September 2026  
**Technology:** Google Cloud IAM, Terraform, Open Policy Agent (OPA), Rego, security-impact documentation

## Situation

A collaborative cloud security policy engine needed consistent, reviewed controls for settings in Terraform resource definitions. The goal was to help identify configurations that warranted security review and demonstrate their evaluation using policy-as-code.

## Task

Contribute to the resource `google_iam_workforce_pool_provider`. The merged PR contains documentation changes, Rego policy files and compliant/non-compliant Terraform examples for five security-relevant arguments:

- `attribute_condition`
- `deletion_policy`
- `detailed_audit_logging`
- `location`
- `oidc.web_sso_config.response_type`

## Action

1. Reviewed the GCP resource's arguments and recorded security-impact assessments and rationales in the resource JSON documentation.
2. Wrote OPA/Rego policy checks against input Terraform configuration.
3. Created compliant and non-compliant Terraform fixtures for each of the five argument controls.
4. Submitted the contribution through a GitHub pull request for the team's review and integration.

### A concrete example: location guardrail

The current PDE `dev` branch contains a `location` control for `google_iam_workforce_pool_provider` that checks the approved value `global`. Its paired fixtures illustrate permitted and non-permitted configuration values.

- [Current Rego policy](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/policy.rego)
- [Compliant Terraform fixture](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/compliant.tf)
- [Non-compliant Terraform fixture](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/nonCompliant.tf)
- [Security assessment documentation](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/docs/gcp/Cloud%20IAM/google_iam_workforce_pool_provider.json)

The present repository layout differs from the layout in PR #636 because the team subsequently refactored the file structure. The merged PR is the historical attribution record.

## Result

**PR #636 was merged** into the Hardhat Enterprises repository. Its change set includes **37 files**, including five Rego policy files and paired Terraform fixtures in the historical structure. The code and examples are publicly inspectable.

This establishes a reviewed, accepted contribution. It does **not** establish that the policies were deployed to a real cloud tenant, or a measured reduction in attacks or compliance incidents.

## STAR summary

**Situation:** Security-critical Terraform settings required consistent evaluation.  
**Task:** Cover the security-relevant arguments of a GCP IAM workforce identity provider resource.  
**Action:** Reviewed resource documentation, authored Rego checks and prepared positive and negative Terraform fixtures.  
**Result:** Changes were reviewed and merged into the organisation's PDE repository ([PR #636](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636)).

## Scope, provenance and reuse

This is a **team capstone repository**, not a sole-authored application. The PR attribution confirms the user's contribution. Source code is linked to its original public repository, not copied wholesale into this personal portfolio. Permission to view public code does not imply permission to relicense or redistribute team work.

Other PRs authored by the same user were closed without merging. They should not be represented as merged contributions.
