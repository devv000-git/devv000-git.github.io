# Devin Kalansuriya | Cybersecurity Portfolio

**Live website:** https://devv000-git.github.io/

A public portfolio combining university cybersecurity investigations with a CloudVantage IT Support & Cloud Analyst industry placement and a Hardhat Enterprises cloud security policy-as-code capstone.

The portfolio supports graduate and junior roles in security operations, cybersecurity analysis, digital forensics and security engineering.

## Experience and cloud security

- **CloudVantage Australia:** IT Support & Cloud Analyst, industry placement, July–November 2026. Azure infrastructure, identity, Microsoft Sentinel, Azure Monitor, Log Analytics/KQL and security recommendations.
- **Hardhat Enterprises:** Policy Author in the industry capstone Policy Deployment Engine, March–September 2026. Terraform and GCP IAM resource review, OPA/Rego controls, test configurations and Python automation.
- **Hardhat Enterprises:** Leadership Team Member, June–September 2026. Capstone contributor coordination and technical guidance.
- **Verified Hardhat GitHub contributions:** Policy Deployment Engine GCP IAM security policies ([merged PR #636](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636)), Security Impact Skeleton Generator ([merged PR #878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878)), and Cloud Quotas policy automation ([merged PR #393](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393)). Original upstream code and review records are linked.
- **Professional qualifications:** Microsoft Certified: Azure Fundamentals (AZ-900), Google Cybersecurity Professional Certificate V2 and Google AI Professional Certificate. Other courses and programmes are listed in the live website.

The portfolio describes industry placement and capstone work, with technical evidence linked in the individual project case studies.

## Verified industry case studies

The [industry project page](industry-projects.html) presents three verified Hardhat contributions, an Azure monitoring lab and a placement dashboard.

| Case study | Evidence |
| --- | --- |
| [GCP IAM security policies](industry-projects.html#iam) | [Merged PR #636](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/636) and [technical write-up](projects/cloud-policy-deployment/README.md) |
| [Python Security Impact Skeleton Generator](industry-projects.html#generator) | [Merged PR #878](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/878), [Python source](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/main.py), [pytest source](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/blob/dev/scripts/security_impact_skeleton_generator/_tests/test_main.py), [case study](projects/security-impact-skeleton-generator/README.md) |
| [GCP Cloud Quotas policies](industry-projects.html#quotas) | [Merged PR #393](https://github.com/Hardhat-Enterprises/Policy-Deployment-Engine/pull/393/files) and [technical write-up](projects/gcp-cloud-quotas-policy/README.md) |
| [Azure security monitoring lab](industry-projects.html#cloudvantage) | [Dated lab configuration and limitations](projects/azure-security-monitoring-lab/README.md) from 7–11 September 2026 |
| [Azure placement task dashboard](industry-projects.html#dashboard) | [Live privacy-safe demo](demos/placement-dashboard/), [reviewed React/Python/Terraform implementation evidence](projects/azure-placement-dashboard/README.md), and [security source review](docs/placement-dashboard-source-review.md) |

GitHub [evidence register](docs/hardhat-source-evidence-register.md) distinguishes merged work from unmerged PRs, historical code paths and unverified production claims.

The [CloudVantage logbook evidence register](docs/cloudvantage-logbook-evidence-register.md) maps individual dated entries to the Azure monitoring lab and deployed React/Python task dashboard. The dashboard architecture has also been reviewed against its React, Python and Terraform implementation. It distinguishes configured features, successful CRUD testing and unverified monitoring outcomes. The upstream code remains in the Hardhat Enterprises team repository.

## Featured work

| Case study | Primary technologies | Evidence |
| --- | --- | --- |
| [Python ARP spoofing detector](https://devv000-git.github.io/#project/arp-detector) | Python, Scapy, Linux | Original monitoring and alert screenshots, reconstructed code and unit tests |
| [Malware network traffic investigation](https://devv000-git.github.io/#project/malware-pcap) | Wireshark, PCAP, HTTP | Original endpoint, HTTP request and executable-header screenshot crops |
| [Malware behaviour and ATT&CK mapping](https://devv000-git.github.io/#project/malware-analysis) | Ghidra, VirusTotal, MITRE ATT&CK | Original Ghidra and VirusTotal screenshot crops, documented ATT&CK mapping and confidence limits |
| [Windows memory forensics](https://devv000-git.github.io/#project/memory-forensics) | Volatility, FTK Imager | Two original Volatility screenshot crops, separate investigation timelines and evidence register |
| [Web application security assessment](https://devv000-git.github.io/#project/web-security) | Burp Suite, BodgeIt Store, DVWA | Four original screenshot crops, nine documented vulnerabilities and behaviours, remediation recommendations |
| [Cybersecurity data analytics](https://devv000-git.github.io/#project/security-analytics) | Python, pandas, matplotlib | Three transparently recreated figures, source-derived tables, reproducible Python code and seven unit tests |

Seven additional supporting investigations are accessible through the [projects catalogue](https://devv000-git.github.io/#projects).

## Evidence standards

- Each case study identifies its originating university unit and the relevant PDF page references.
- Public images are selected excerpts, not complete assessment submissions.
- Evidence galleries are available for [SIT379 ARP detector screenshots](docs/arp-evidence-register.md), [SIT327 packet-capture analysis](docs/network-forensics-evidence-register.md), and [SIT324 malware analysis](docs/malware-analysis-evidence-register.md).
- The [SIT324 Windows memory forensics project](docs/memory-forensics-evidence-register.md) now has a detailed, page-referenced evidence register and two clearly separated investigations. Two original Volatility output crops are now published and carefully attributed to separate captures.
- The [SIT379 web application security project](docs/web-security-evidence-register.md) includes original XSS, negative-basket and file-upload evidence, with private request credentials excluded.
- The [SIT384 analytics case study](docs/sit384-analytics-evidence-register.md) provides three **figure reconstructions**, not original screenshots. Its original dataset files are unavailable, and the publicly tested code is labelled as reconstructed.
- Where code has been reconstructed from a report screenshot, it is labelled as reconstructed. It must not be mistaken for the exact original submitted source.
- Observed alerts are not automatically proof of compromise. Case studies document limits and alternative explanations.
- Original university reports, malicious samples, credentials and private data are not distributed here.

## Website

The current website is a responsive, self-contained static HTML/CSS/JavaScript application hosted on GitHub Pages. No backend services, account registration or database are required.

To run a local copy:

```bash
git clone https://github.com/devv000-git/devv000-git.github.io.git
cd devv000-git.github.io
python3 -m http.server 8000
```

Open `http://localhost:8000`. Changes to the `main` branch trigger GitHub Pages deployment.

## Reconstructed security analytics

The [SIT384 analytics folder](projects/cybersecurity-data-analytics/) contains a portable Python plotting implementation, an example transcribed from an original figure, synthetic test fixtures, and [automated tests](.github/workflows/analytics-tests.yml). It is not a real-time SOC dashboard or a replacement for the unavailable source datasets.

## Reconstructed ARP monitor

The [ARP detector folder](projects/arp-detector/) contains a documented Python/Scapy implementation and deterministic unit tests. The [GitHub Actions workflow](.github/workflows/arp-tests.yml) runs its tests automatically for code changes.

## Credentials

- Bachelor of Cybersecurity, Deakin University · **Distinction result** · **Minor in Security Management** · Degree requirements completed October 2026, formal graduation expected February 2027
- Microsoft Certified: Azure Fundamentals (AZ-900)
- Google Cybersecurity Professional Certificate
- Google AI Professional Certificate

## Licence and provenance

Website source code is distributed under the repository's MIT licence. Original university-lab screenshot excerpts remain attributed to the author's university work. Do not reuse source evidence as an unrelated project or claim it as your own.

This is a portfolio of educational practical work, not a claim of professional incident-response engagements.
