from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset
from src.data.validate_dataset import validate_dataset


def test_referential_integrity_passes_for_clean_dataset(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    generate_dataset("training", settings, local_tmp_path)
    errors = validate_dataset("training", local_tmp_path, write_report=False)
    assert errors == []
