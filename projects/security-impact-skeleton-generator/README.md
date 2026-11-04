# Security Impact Skeleton Generator | Python Development Tool

**Project:** Hardhat Enterprises, Policy Deployment Engine  
**Verified contribution:** [PR #878: Add security impact skeleton generator](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878), authored by `devv000-git`, merged 18 October 2026  
**Technology:** Python, JSON, Terraform templates, Rego policy skeletons, pytest  
**Source:** [main.py](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/main.py) and [test_main.py](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/_tests/test_main.py)

## Situation

PDE contributors needed repetitive file structures before writing individual cloud security policies. Manual scaffolding increased setup work and risked inconsistent policy directory and package names.

## Task

Build a developer tool to prepare missing policy and Terraform test fixture skeletons based on resource documentation, without overwriting existing contributors' files or making security decisions automatically.

## Action

The merged Python implementation:

1. Accepts a resource reference in `cloud/service/resource` format.
2. Loads the resource JSON and identifies arguments explicitly marked `security_impact: true`.
3. Checks the required policy folder, Terraform fixture files and shared `config.tf`.
4. Generates missing `policy.rego`, `compliant.tf`, `nonCompliant.tf` and resource `_vars.rego` from templates.
5. Supports nested argument identifiers such as `oidc.web_sso_config.response_type`, converting them to valid package names while preserving the source argument paths.
6. Skips files that already exist, protecting contributors' work.
7. Leaves remediation logic, security-impact decisions and compliant/non-compliant settings for a human author.

### Documented usage

```bash
python3 scripts/security_impact_skeleton_generator/main.py \
  "gcp/Cloud IAM/google_iam_workforce_pool_provider"

python3 scripts/security_impact_skeleton_generator/main.py \
  "gcp/Cloud IAM/google_iam_workforce_pool_provider" --generate
```

The first command reports missing and existing files. The second creates **only missing** skeletons, provided shared project templates and config exist.

## Verification

The current public `dev` branch includes **nine `pytest` test functions**. They cover target parsing, security-impact filtering, service slug conversion, path construction, nested arguments, template substitution and no-overwrite handling.

- [Source README and usage](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/README.md)
- [Nine test functions](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/_tests/test_main.py)
- [Merged PR #878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878)

**Important:** Nine functions exist in the checked source. Their historical README records `9 passed`. We have not independently rerun the project's environment for this portfolio update and do not claim a fresh execution result.

## Result

**PR #878 was reviewed and merged** into the Hardhat Enterprises repository. It demonstrates Python automation, validation-aware design and collaborative GitHub development. It does **not** claim measured time saved or autonomous generation of secure policy logic.

## STAR summary

**Situation:** Contributors repeatedly created predictable Terraform and Rego policy structures.  
**Task:** Automate safe scaffolding while preserving contributor-controlled logic.  
**Action:** Wrote a Python generator using JSON metadata, templates, nested path support, no-overwrite checks and pytest coverage.  
**Result:** The tool was integrated into the project's shared `dev` branch through merged [PR #878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878).

## Repository provenance

The files belong to an organisational team repository. This case study links to the actual implementation and tests rather than reproducing or relicensing them as independently owned work.
