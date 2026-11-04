"""Reconstructed cyber analytics plotting workflows from SIT384 tasks 4.1P and 4.2C.

New portfolio code based on the documented methods, not a verbatim copy of the
submitted source. The original university CSV datasets are not distributed.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CATEGORY_ORDER = ("dos", "u2r", "r2l", "probe")

def summarise_attack_categories(data: pd.DataFrame) -> pd.DataFrame:
    """Distinguish number of attack types from recorded attack volume."""
    required = {"category", "Attack_type", "number_of_attack"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {', '.join(sorted(missing))}")
    clean = data.copy()
    clean["category"] = clean["category"].astype("string").str.strip().str.lower()
    clean["number_of_attack"] = pd.to_numeric(clean["number_of_attack"], errors="raise")
    if clean["number_of_attack"].isna().any() or (clean["number_of_attack"] < 0).any():
        raise ValueError("Attack volumes must be non-negative and non-null")
    if (~clean["category"].isin(CATEGORY_ORDER)).any():
        unexpected = sorted(set(clean.loc[~clean["category"].isin(CATEGORY_ORDER), "category"].dropna()))
        raise ValueError(f"Unexpected attack categories: {unexpected}")
    counts = clean.groupby("category")["Attack_type"].count()
    volume = clean.groupby("category")["number_of_attack"].sum()
    result = pd.DataFrame({"attack_type_count": counts, "attack_volume": volume})
    return result.reindex(CATEGORY_ORDER, fill_value=0)

def validate_sector_table(table: pd.DataFrame) -> pd.DataFrame:
    """Ensure incident types are rows and sectors are columns."""
    if table.empty or table.shape[1] == 0:
        raise ValueError("Sector table must have at least one sector and one row")
    if not table.columns.is_unique or not table.index.is_unique:
        raise ValueError("Sector labels and incident-type labels must be unique")
    numeric = table.apply(pd.to_numeric, errors="raise")
    if not np.isfinite(numeric.to_numpy(dtype=float)).all():
        raise ValueError("Sector counts must be finite")
    if (numeric < 0).any().any():
        raise ValueError("Sector counts must be non-negative")
    return numeric

def plot_attack_categories(summary: pd.DataFrame, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    labels = list(summary.index)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(labels, summary["attack_type_count"])
    ax.set(title="Attack Types by Category", xlabel="Category", ylabel="Number of attack types")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_dir / "attack-types.png", dpi=150)
    plt.close(fig)

    volumes = summary["attack_volume"]
    if volumes.sum() == 0:
        raise ValueError("Pie chart requires positive total attack volume")
    fig, ax = plt.subplots(figsize=(7, 6))
    ax.pie(volumes, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Recorded Attack Volume by Category")
    fig.tight_layout()
    fig.savefig(out_dir / "attack-volume.png", dpi=150)
    plt.close(fig)

def plot_sector_comparison(table: pd.DataFrame, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    clean = validate_sector_table(table)
    sectors = list(clean.columns)
    types = list(clean.index)
    pos = np.arange(len(sectors))
    width = 0.8 / len(types)

    fig, ax = plt.subplots(figsize=(11, 6))
    for i, label in enumerate(types):
        x = pos - 0.4 + (i + 0.5) * width
        ax.bar(x, clean.loc[label].to_numpy(), width=width, label=label)
    ax.set_xticks(pos, sectors, rotation=25, ha="right")
    ax.set(title="Attack Types by Sector", ylabel="Recorded incident count")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "sectors-grouped.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6))
    bottom = np.zeros(len(sectors))
    for label in types:
        values = clean.loc[label].to_numpy(dtype=float)
        ax.bar(pos, values, bottom=bottom, label=label)
        bottom += values
    ax.set_xticks(pos, sectors, rotation=25, ha="right")
    ax.set(title="Total Recorded Incidents by Sector", ylabel="Recorded incident count")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "sectors-stacked.png", dpi=150)
    plt.close(fig)

def main() -> None:
    parser = argparse.ArgumentParser(description="Reproduce SIT384-inspired charts from CSV data")
    sub = parser.add_subparsers(dest="report", required=True)
    by_type = sub.add_parser("categories", help="CSV columns category, Attack_type, number_of_attack")
    by_type.add_argument("csv", type=Path)
    by_sector = sub.add_parser("sectors", help="CSV rows=incident types, columns=sectors")
    by_sector.add_argument("csv", type=Path)
    for command in (by_type, by_sector):
        command.add_argument("--out", type=Path, default=Path("charts"))
    args = parser.parse_args()
    try:
        if args.report == "categories":
            summary = summarise_attack_categories(pd.read_csv(args.csv))
            plot_attack_categories(summary, args.out)
        else:
            table = validate_sector_table(pd.read_csv(args.csv, index_col=0))
            plot_sector_comparison(table, args.out)
    except (OSError, ValueError, pd.errors.ParserError) as exc:
        parser.error(str(exc))
    print(f"Charts written to: {args.out.resolve()}")

if __name__ == "__main__":
    main()
