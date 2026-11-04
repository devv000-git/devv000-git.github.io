"""Tests use synthetic fixtures, not the original university datasets."""
from pathlib import Path
from tempfile import TemporaryDirectory
import sys
import unittest
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from analytics import (summarise_attack_categories, validate_sector_table,
                       plot_attack_categories, plot_sector_comparison)

class CategoryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = pd.DataFrame({
            "category": ["dos", "dos", "u2r", "probe", "r2l"],
            "Attack_type": ["a", "b", "c", "d", "e"],
            "number_of_attack": [5, 7, 3, 4, 1],
        })
    def test_type_count_is_not_attack_volume(self):
        actual = summarise_attack_categories(self.fixture)
        self.assertEqual(int(actual.loc["dos", "attack_type_count"]), 2)
        self.assertEqual(int(actual.loc["dos", "attack_volume"]), 12)
        self.assertEqual(list(actual.index), ["dos", "u2r", "r2l", "probe"])
    def test_rejects_missing_column(self):
        with self.assertRaises(ValueError):
            summarise_attack_categories(self.fixture.drop(columns="number_of_attack"))
    def test_rejects_negative_volume(self):
        data = self.fixture.copy()
        data.loc[0, "number_of_attack"] = -4
        with self.assertRaises(ValueError):
            summarise_attack_categories(data)
    def test_generates_charts(self):
        with TemporaryDirectory() as directory:
            plot_attack_categories(summarise_attack_categories(self.fixture), Path(directory))
            self.assertTrue((Path(directory)/"attack-types.png").is_file())
            self.assertTrue((Path(directory)/"attack-volume.png").is_file())

class SectorTests(unittest.TestCase):
    def setUp(self):
        self.fixture = pd.DataFrame({"Healthcare": [4, 2], "Finance": [3, 6]},
                                    index=["cyber incident", "social engineering"])
    def test_validates_numeric_table(self):
        clean = validate_sector_table(self.fixture)
        self.assertEqual(int(clean.loc["cyber incident", "Healthcare"]), 4)
    def test_rejects_negative_values(self):
        bad = self.fixture.copy()
        bad.loc["cyber incident", "Healthcare"] = -1
        with self.assertRaises(ValueError):
            validate_sector_table(bad)
    def test_generates_both_sector_charts(self):
        with TemporaryDirectory() as directory:
            plot_sector_comparison(self.fixture, Path(directory))
            self.assertTrue((Path(directory)/"sectors-grouped.png").is_file())
            self.assertTrue((Path(directory)/"sectors-stacked.png").is_file())

if __name__ == "__main__":
    unittest.main()
