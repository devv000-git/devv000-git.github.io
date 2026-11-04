# Cybersecurity Data Analytics and Visualisation

**Academic source:** SIT384 Cyber Security Analytics, Deakin University  
**Original work:** Task 4.1P, “Visualize data using matplotlib”, and Task 4.2C, “Visualize data with grouped bar chart and stacked bar chart”  
**Submission dates in the PDF:** 5–6 April 2025  
**Source pages:** PDF pages 50–63  
**Technologies:** Python, pandas, matplotlib, NumPy (for the reconstructed project)

## Situation

Security-related datasets are difficult to interpret when attack categories and industry sectors appear only as raw tables. Two SIT384 exercises required clear charts that compare attack classifications, recorded attack volumes and attack types across five sectors.

## Task

Visualise two supplied CSV datasets using Python. The first dataset contained `category`, `Attack_type` and `number_of_attack` fields. The second was described in the submission under the filename `Malicious_or_criminal_attacks_breakdown-Top_five_sectors_July-Dec-2023.csv`, with attack types as rows and industry sectors as columns.

## Action

For Task 4.1P, the original source code (PDF p. 52) used pandas `groupby('category')` to compute two **different measures**:

- `count()` of `Attack_type`: number of different attack-type records in each category.
- `sum()` of `number_of_attack`: aggregate volume recorded in each category.

It then produced a bar chart and a pie chart with matplotlib. For Task 4.2C, the source code (p. 59) used a CSV indexed by attack type, plotting grouped columns for within-sector comparisons and a stacked chart for sector totals.

## Result

### 1. Attack-type counts (Task 4.1P)

The original bar chart on **PDF page 53** displays:

| Category | Count of attack types |
| --- | ---: |
| dos | 11 |
| u2r | 8 |
| r2l | 15 |
| probe | 7 |

The **count of attack types is not the number of attack events**. It is a count of rows or type names grouped under each category.

The original pie chart on **PDF page 54** displays the proportions of **attack volume**, a different measure:

| Category | Share of recorded attack volume as displayed |
| --- | ---: |
| dos | 19.7% |
| u2r | 33.3% |
| r2l | 32.2% |
| probe | 14.9% |

The percentages total **100.1% because they are individually rounded to one decimal place**. The raw event totals cannot be reliably recovered from these percentages alone.

### 2. Sector comparisons (Task 4.2C)

The original grouped and stacked plots on **PDF page 63** display four attack/incident types for five sectors. The following integers are **manually transcribed from the labels visible in that figure**, not copied from the original CSV. The chart is labelled **July–December 2023** in the submission.

| Incident category | Health service providers | Finance (incl. superannuation) | Insurance | Retail | Australian Government |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cyber incident | 38 | 14 | 12 | 27 | 1 |
| Social engineering / impersonation | 4 | 12 | 11 | 2 | 8 |
| Rogue employee / insider threat | 9 | 5 | 1 | 2 | 2 |
| Theft of paperwork or data storage device | 4 | 2 | 0 | 1 | 1 |
| **Total from visible labels** | **55** | **33** | **24** | **32** | **12** |

The sector figure compares **counts in the supplied historical dataset**. It does not establish current risk, per-organisation likelihood, or changes over time. Without the original CSV and its documentation, the source population and definitions cannot be independently verified.

## Reconstructed, tested implementation

[analytics.py](analytics.py) is a **newly written portfolio implementation**, adapted from the two original source-code extracts. It is **not** the original university code. It:

- Validates required CSV columns and non-negative numeric values.
- Keeps type counts and attack volumes separate.
- Generates bar and pie charts for category distributions.
- Generates grouped and stacked sector comparisons.
- Saves generated PNG files without requiring a graphical desktop.
- Uses `set_xticks` with explicit labels, avoiding the tick-locator warning visible in the original exercise (PDF p. 61).

The original sector dataset is not provided. For reproducible demonstration, the repository includes [sector counts transcribed from the published figure](examples/sector-counts-transcribed-from-figure.csv), clearly distinguished from the unavailable source CSV. The [synthetic attack-type CSV](examples/synthetic-attack-types.csv) is purely a testing example and **does not reproduce the original submission's results**.

### Run locally

```bash
python -m pip install -r requirements.txt

# Recreate sector charts using values transcribed from the report figure
python analytics.py sectors examples/sector-counts-transcribed-from-figure.csv --out charts/sector

# Exercise category charts with synthetic input, NOT the original dataset
python analytics.py categories examples/synthetic-attack-types.csv --out charts/synthetic

# Run deterministic automated tests
python -m unittest discover -s tests -v
```

The tests use synthetic input. They verify aggregation, validation and creation of the expected output files. They do not verify the original university dataset because that raw dataset was not uploaded.

## Evidence and provenance

- **PDF p. 52:** Original Python `groupby`, `count`, `sum`, bar chart and pie chart code.
- **PDF p. 53:** Original bar-chart output with category type counts.
- **PDF p. 54:** Original pie-chart output with rounded attack-volume percentages.
- **PDF p. 59:** Original grouped and stacked bar-chart source code.
- **PDF p. 61:** Printed `set_ticklabels()` warning from the original implementation.
- **PDF p. 63:** Grouped and stacked output with five sectors, labelled Jul–Dec 2023.

See [the source evidence register](../../docs/sit384-analytics-evidence-register.md).

## Limitations and professional application

This is an **academic analytics case study**, not a production SOC dashboard, an intrusion-detection model, or a live incident feed. The study demonstrates reproducible data transformation and communication of findings, useful foundations for security reporting and investigation work.

The source code references local Windows desktop paths that are not suitable for a public repository. The reconstruction replaces them with CLI arguments and does not include personal paths or the unprovided CSVs.

**[View the live case study](https://devv000-git.github.io/#project/security-analytics)**
