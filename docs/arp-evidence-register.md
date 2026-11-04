# Evidence register: ARP mapping-change detector

## Source and boundaries

- **Unit:** SIT379 Ethical Hacking, Deakin University, 2026
- **Original exercise:** Module 5, Task 5.2C
- **Source document:** `SIT379-s223136653-portfolio.pdf` (private, not distributed)
- **Project type:** Authorised university networking lab
- **Nature of screenshots:** Authentic cropped extracts from the original assessment report, not images from the later reconstructed implementation.

## Public evidence

| File | Source PDF page | What it demonstrates | Processing |
| --- | --- | --- | --- |
| [baseline-original-crop.png](../../assets/evidence/arp/baseline-original-crop.png) | 132 | Original monitoring output records an IP-to-MAC mapping | Cropped and high-contrast monochrome conversion |
| [alert-original-crop.png](../../assets/evidence/arp/alert-original-crop.png) | 133 | Script reports a possible ARP spoofing event with the old and new MAC addresses | Cropped and high-contrast monochrome conversion |

The source report also contains a screenshot of the original Scapy script (page 131) and a controlled network simulation (page 132). These have not yet been published as standalone images.

The cropped images contain private-range lab addressing and virtual network MAC values. They do not contain passwords, API keys, student IDs, or real client data.

## What is and is not proved

The screenshots support the narrower conclusion that **the script observed a change in the MAC mapping associated with an IP address and printed a possible spoofing alert in a controlled lab**.

They do **not** establish:
- That the tool correctly identifies every ARP spoofing technique.
- That false positives have been measured in a production network.
- That a man-in-the-middle compromise succeeded.
- That the later reconstructed Python source is identical to the original university submission.

The public `projects/arp-detector/arp_detector.py` file is explicitly a reconstruction and improvement for portfolio demonstration. Its unit tests exercise synthetic mapping observations. Live packet-capture behaviour is a separate concern.

## Publication safety

Only high-contrast crops of the original university report are published. Full assignment documents, student details and any environment credentials are not published.
