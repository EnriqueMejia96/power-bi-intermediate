from src.reporting.generate_data_dictionary import generate_data_dictionary


def test_dictionary_markdown_and_excel_created(local_tmp_path):
    md_path, xlsx_path = generate_data_dictionary("training", local_tmp_path)
    assert md_path.exists()
    assert "Fact_OrdenesTrabajo" in md_path.read_text(encoding="utf-8")
    assert xlsx_path is not None and xlsx_path.exists()
