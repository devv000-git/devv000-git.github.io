# Devin Kalansuriya | Cybersecurity Portfolio

**Live website:** https://devv000-git.github.io/

A public record of university laboratory investigations, defensive security projects and technical exercises completed during the Bachelor of Cybersecurity at Deakin University.

The portfolio supports graduate and junior roles in security operations, cybersecurity analysis, digital forensics and security engineering.

## Featured work

| Case study | Primary technologies | Evidence |
| --- | --- | --- |
| [Python ARP spoofing detector](https://devv000-git.github.io/#project/arp-detector) | Python, Scapy, Linux | Original monitoring and alert screenshots, reconstructed code and unit tests |
| [Malware network traffic investigation](https://devv000-git.github.io/#project/malware-pcap) | Wireshark, PCAP, HTTP | Original endpoint, HTTP request and executable-header screenshot crops |
| [Malware behaviour and ATT&CK mapping](https://devv000-git.github.io/#project/malware-analysis) | Ghidra, VirusTotal, MITRE ATT&CK | Original Ghidra and VirusTotal screenshot crops, documented ATT&CK mapping and confidence limits |
| [Windows memory forensics](https://devv000-git.github.io/#project/memory-forensics) | Volatility, FTK Imager | Two separately sourced investigations, PID correlation, memory-region findings and page-referenced evidence register |
| [Web application security assessment](https://devv000-git.github.io/#project/web-security) | Burp Suite, DVWA | Original XSS and MIME-request screenshots, five documented findings, and remediation notes |
| [Cybersecurity data analytics](https://devv000-git.github.io/#project/security-analytics) | Python, pandas, matplotlib | Source report references, further screenshots being prepared |

Seven additional supporting investigations are accessible through the [projects catalogue](https://devv000-git.github.io/#projects).

## Evidence standards

- Each case study identifies its originating university unit and the relevant PDF page references.
- Public images are selected excerpts, not complete assessment submissions.
- Evidence galleries are available for [SIT379 ARP detector screenshots](docs/arp-evidence-register.md), [SIT327 packet-capture analysis](docs/network-forensics-evidence-register.md), and [SIT324 malware analysis](docs/malware-analysis-evidence-register.md).
- The [SIT324 Windows memory forensics project](docs/memory-forensics-evidence-register.md) now has a detailed, page-referenced evidence register and two clearly separated investigations. Original memory screenshots are not yet published in that case study.
- [SIT379 Web Security](docs/web-security-evidence-register.md) has two original screenshot excerpts and page-specific validation of five vulnerability demonstrations.
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

## Reconstructed ARP monitor

The [ARP detector folder](projects/arp-detector/) contains a documented Python/Scapy implementation and deterministic unit tests. The [GitHub Actions workflow](.github/workflows/arp-tests.yml) runs its tests automatically for code changes.

## Credentials

- Bachelor of Cybersecurity, Deakin University, completed October 2026
- Microsoft Certified: Azure Fundamentals (AZ-900)
- Google Cybersecurity Professional Certificate
- Google AI Professional Certificate

## Licence and provenance

Website source code is distributed under the repository's MIT licence. Original university-lab screenshot excerpts remain attributed to the author's university work. Do not reuse source evidence as an unrelated project or claim it as your own.

This is a portfolio of educational practical work, not a claim of professional incident-response engagements.
