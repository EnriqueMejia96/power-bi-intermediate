from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.config.settings import load_settings
from src.data.schema import TABLE_COLUMNS, TABLE_DESCRIPTIONS, PRIMARY_KEYS, DIMENSION_TABLES, FACT_TABLES
from src.utils.io import write_text


def build_dictionary_frame() -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for table, columns in TABLE_COLUMNS.items():
        for column in columns:
            role = "PK" if PRIMARY_KEYS.get(table) == column else ("FK/atributo" if column.endswith("ID") or column.endswith("Key") else "Métrica/atributo")
            rows.append({
                "TableName": table,
                "TableType": "Dimensión" if table in DIMENSION_TABLES else "Hecho",
                "ColumnName": column,
                "Role": role,
                "Description": f"{column} de {table}. {TABLE_DESCRIPTIONS.get(table, '')}",
            })
    return pd.DataFrame(rows)


def generate_data_dictionary(dataset_kind: str, root: Path | None = None) -> tuple[Path, Path | None]:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    out_dir = root / "data" / dataset_kind / "dictionary"
    out_dir.mkdir(parents=True, exist_ok=True)
    df = build_dictionary_frame()
    lines = [f"# Diccionario de datos - {dataset_kind}", "", "Datos 100% sintéticos. Schema común para Dataset A y Dataset B.", ""]
    for table in DIMENSION_TABLES + FACT_TABLES:
        lines.append(f"## {table}")
        lines.append(TABLE_DESCRIPTIONS.get(table, ""))
        lines.append("")
        lines.append("| Columna | Rol | Descripción |")
        lines.append("|---|---|---|")
        subset = df[df["TableName"] == table]
        for _, row in subset.iterrows():
            lines.append(f"| {row['ColumnName']} | {row['Role']} | {row['Description']} |")
        lines.append("")
    md_path = out_dir / "data_dictionary.md"
    write_text("\n".join(lines), md_path, root)
    xlsx_path: Path | None = None
    if settings.export_excel_dictionary:
        xlsx_path = out_dir / "data_dictionary.xlsx"
        with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Dictionary")
            pd.DataFrame({"DimensionTables": DIMENSION_TABLES}).to_excel(writer, index=False, sheet_name="Dimensions")
            pd.DataFrame({"FactTables": FACT_TABLES}).to_excel(writer, index=False, sheet_name="Facts")
    return md_path, xlsx_path


def generate_all_dictionaries(root: Path | None = None) -> dict[str, tuple[Path, Path | None]]:
    return {kind: generate_data_dictionary(kind, root) for kind in ["training", "project"]}
