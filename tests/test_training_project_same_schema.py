from __future__ import annotations

import pandas as pd

from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset
from src.data.schema import TABLE_COLUMNS


def test_training_and_project_clean_tables_keep_same_schema(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    generate_dataset("training", settings, local_tmp_path)
    generate_dataset("project", settings, local_tmp_path)

    for table, expected_columns in TABLE_COLUMNS.items():
        training = pd.read_csv(local_tmp_path / "data" / "training" / "clean" / f"{table}.csv")
        project = pd.read_csv(local_tmp_path / "data" / "project" / "clean" / f"{table}.csv")
        assert list(training.columns) == expected_columns
        assert list(project.columns) == expected_columns
        assert list(training.columns) == list(project.columns)
