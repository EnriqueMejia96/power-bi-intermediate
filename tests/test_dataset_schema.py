import pandas as pd

from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset
from src.data.schema import TABLE_COLUMNS, DIMENSION_TABLES, FACT_TABLES


def test_generated_schema_columns(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    generate_dataset("training", settings, local_tmp_path)
    for table, columns in TABLE_COLUMNS.items():
        df = pd.read_csv(local_tmp_path / f"data/training/clean/{table}.csv")
        assert list(df.columns) == columns
    assert len(DIMENSION_TABLES) == 11
    assert len(FACT_TABLES) == 8
