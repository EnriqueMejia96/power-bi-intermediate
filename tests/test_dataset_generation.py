from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_dataset


def test_dataset_generation_creates_both_schemas(local_tmp_path):
    settings = load_settings(local_tmp_path).with_small_counts()
    training = generate_dataset("training", settings, local_tmp_path)
    project = generate_dataset("project", settings, local_tmp_path)
    assert set(training) == set(project)
    assert (local_tmp_path / "data/training/clean/Fact_OrdenesTrabajo.csv").exists()
    assert (local_tmp_path / "data/project/clean/Fact_OrdenesTrabajo.csv").exists()
