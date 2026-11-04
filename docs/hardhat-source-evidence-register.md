# Hardhat Enterprises source-evidence register

Updated 4 November 2026. Verification was performed by reading the public `Hardhat-Enterprises/Policy-Deployment-Engine` repository and GitHub pull-request records.

## Authorship and merge status

The repository is an **organisational team capstone**. The following PRs show the portfolio owner's GitHub username `devv000-git` as author and an actual merge, rather than merely a submitted or closed PR.

| PR | Title | Author | Merge date (UTC) | Verification |
| --- | --- | --- | --- | --- |
| [#636](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636) | Service/gcp/cloud iam/google iam workforce pool provider | `devv000-git` | **1 September 2026** | `merged: true`, **37 changed files**, five Rego policies + compliant/non-compliant Terraform examples in the historical PR |
| [#878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878) | Add security impact skeleton generator | `devv000-git` | **18 October 2026** | `merged: true`, current [generator source](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/main.py) and [nine tests](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/_tests/test_main.py) |
| [#393](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393) | Add Cloud Quotas policies and documentation | `devv000-git` | **23 May 2026** | `merged: true`, **57 changed files** shown in the historical PR diff |

## Direct source evidence

### GCP IAM

- [Merged PR #636 file list](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636/files)
- [Current location policy](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/policy.rego)
- [Current compliant Terraform example](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/compliant.tf)
- [Current non-compliant Terraform example](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/policies/gcp/Cloud%20IAM/google_iam_workforce_pool_provider/location/nonCompliant.tf)
- [Current resource security-impact JSON](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/docs/gcp/Cloud%20IAM/google_iam_workforce_pool_provider.json)

The current location Rego code uses a whitelist of `global`. Its Terraform examples include `global` as compliant and `us-central1` as non-compliant. These are project policy examples, not a general statement that Google Cloud has only one technically supported location.

### Generator

- [Merged PR #878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878)
- [Python implementation](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/main.py)
- [Usage and design README](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/README.md)
- [pytest source](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/_tests/test_main.py)

Exactly **nine** `test_*` functions are visible in the current test module. The upstream README states `9 passed`. This portfolio did **not** run those tests independently.

### Cloud Quotas

- [Merged PR #393](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393)
- [Historical changes](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393/files)

**Critical:** The current `dev` branch did not contain the original Cloud Quotas policy paths from PR #393 when reviewed. The PR diff is used to prove the historical contribution. Do not present outdated paths as live.

## Caution about other PRs

Search also identified PRs #638, #637, #635, #534, #520, #450, #449, #448, #447 and #380 under the same author account. Their GitHub API response showed `merged: false`. These are **not** counted as merged contributions on the portfolio. The author may have prepared work in them, but the project integration status must remain distinct.

## Scope and intellectual property

- The upstream repository is owned by **Hardhat Enterprises**, not the portfolio owner.
- These cases describe **the owner's verified contributions to the team**, not sole ownership or exclusive development of the full PDE.
- The personal portfolio links to upstream source rather than copying substantial code or assigning it a different licence.
- No production deployment, compliance certification, attack prevention rate, or measured development-time saving is claimed.
- Historical project dates on LinkedIn and later merge dates are kept distinct.

## LinkedIn and portfolio sources

The supplied seven-page LinkedIn PDF documents the capstone role and project names. Its section on page 3 describes Terraform security-impact assessments, OPA/Rego, compliant/non-compliant configurations, Python automation and review workflow. Page 6 lists individual project titles and dates. The source PDF itself remains private and is not committed.
