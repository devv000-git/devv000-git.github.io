# Evidence register: SIT327 packet-capture malware investigation

## Source

**SIT327 Network Forensics, Pass Task 5.1P**  
Portfolio PDF pages **49–59**, submitted in 2026. The report analyses a supplied historical `malware.pcap` in Wireshark. The original full portfolio is stored privately and is not shared here.

## Public screenshots

| File | Page | What it actually shows | Processing |
| --- | --- | --- | --- |
| [host-endpoint.png](../assets/evidence/network-forensics/host-endpoint.png) | 52 | IPv4 endpoint `172.16.254.128` selected in Wireshark | Original screenshot cropped to relevant rows, contrast-enhanced, monochrome |
| [get-request.png](../assets/evidence/network-forensics/get-request.png) | 56 | HTTP request to `www.harveycartel.org` for `/nv2/Nv2-PC.zip` | Cropped and converted to high-contrast monochrome |
| [executable-header.png](../assets/evidence/network-forensics/executable-header.png) | 56 | HTTP response `Content-Disposition` naming `Nv2-PC.exe`, with visible `MZ` and DOS-stub string | Cropped and converted to high-contrast monochrome |

The screenshots were not fabricated or rendered from sample text. They are cropped original evidence embedded in the student's report.

## Cross-check of the source

The report's p. 57 caption identifies the screenshot as showing the malicious `Nv2-PC.zip` stream. **Visual inspection shows that this image is actually Wireshark `tcp.stream eq 72`, containing a JPEG request to `img-9gag-ftw.9cache.com`.** It does **not** demonstrate the archive-named download. This image was deliberately excluded.

The relevant executable-delivery screenshot is on **p. 56**, showing `tcp.stream eq 142` and the HTTP request/response used in this portfolio case study.

The report describes later suspicious POST traffic to `ninja-game.org` on pp. 58–59. No directly matching POST screenshot appears in the included report pages. Portfolio text clearly attributes that claim to the written report rather than treating it as independently corroborated packet evidence.

## Security boundaries

Historical lab network addresses and domain names are retained as identifiers solely for forensic explanation. This repository does not distribute the PCAP or any extracted executable. The website must not imply a live compromise or production investigation.

## Confidence

- **High**: The embedded screenshot shows the HTTP request, executable file disposition, and `MZ` signature.
- **Moderate**: The provided endpoint lists and written report associate the traffic with the identified internal host.
- **Unverified from the available screenshots**: Execution, persistence, successful exfiltration and actual command-and-control activity.
