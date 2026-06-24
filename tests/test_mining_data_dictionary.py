from __future__ import annotations

from src.reporting.generate_data_dictionary import generate_data_dictionary


def test_mining_dictionary_explains_key_fields(local_tmp_path):
    md_path, xlsx_path = generate_data_dictionary("training", local_tmp_path)
    text = md_path.read_text(encoding="utf-8")

    for term in ["ActualOutput", "OutputUnits", "DowntimeHours", "RepairHours", "RiskScore", "DelayDays"]:
        assert term in text
    for mining_term in ["Chancado", "Molienda", "Relaves", "SCADA", "raw", "clean", "Dataset A", "Dataset B"]:
        assert mining_term in text
    assert "Granularidad" in text
    assert "Uso analítico" in text
    assert xlsx_path is not None and xlsx_path.exists()
