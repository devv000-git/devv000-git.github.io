# SIT384 analytics evidence register

## Origin and scope

Source PDF: **SIT384 Cyber Security Analytics**, university portfolio, 2025 coursework.

Two distinct exercises were used:

- Task **4.1P**, PDF pages **50–56**: `attack-type-frequency.csv`, four attack categories and two distinct metrics.
- Task **4.2C**, PDF pages **57–63**: `Malicious_or_criminal_attacks_breakdown-Top_five_sectors_July-Dec-2023.csv`, incident categories by five sectors.

**The original assessment report includes source-code extracts and chart outputs, but not the raw CSV datasets.**

## Evidence mapping

| PDF page | Artifact | What it directly supports |
| --- | --- | --- |
| **52** | Original Python source | pandas groupby on `category`, `Attack_type.count()`, `number_of_attack.sum()`, separate bar and pie charts |
| **53** | Original bar plot | 11 dos, 8 u2r, 15 r2l and 7 probe attack-type records |
| **54** | Original pie plot | Recorded attack-volume proportions of 19.7%, 33.3%, 32.2% and 14.9%, respectively |
| **59** | Original Python source | pandas indexed CSV, loop over incident categories, grouped chart with per-bar labels, and stacked chart with cumulative bottoms |
| **61** | Python warning + chart preview | The original `set_xticklabels` call lacked a fixed tick locator |
| **63** | Original two-panel chart output | Incident-category counts by Health service providers, Finance, Insurance, Retail, Australian Government |

## Re-created values

The [sector comparison CSV](../projects/cybersecurity-data-analytics/examples/sector-counts-transcribed-from-figure.csv) was **manually transcribed** from visible chart labels on PDF page 63. It is a derivative interpretation for demonstration, not a replacement for the original government-sector data CSV.

The category-type counts and rounded proportions shown on the website were also transcribed from the original chart outputs.

The relative proportions of attack-volume categories must not be treated as equivalent to the per-category counts of attack types. They derive from **different aggregations** documented in the source code.

## Reconstructed implementation

The public [analytics.py](../projects/cybersecurity-data-analytics/analytics.py) and its tests were rewritten for the portfolio from the visible source-code operations. They include input validation, a headless Matplotlib backend and explicit tick placement to avoid the warning recorded on p. 61. The new code was tested on synthetic data.

No claim is made that the reconstructed code is the student's original submitted source file or that the original raw datasets were reprocessed.

## Publication boundaries

Original PDFs, student identifiers, private desktop file paths and unprovided datasets are excluded. Charts on the website are **recreations drawn from published lab figures** unless explicitly identified as original screenshot crops. No network traffic, SOC logs, client incidents or real-time detection statistics are implied.
