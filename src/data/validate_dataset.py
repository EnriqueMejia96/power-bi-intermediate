from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.config.settings import load_settings
from src.data.schema import TABLE_COLUMNS, PRIMARY_KEYS, RELATIONSHIPS
from src.utils.io import read_csv, write_text


def _key_set(series: pd.Series) -> set:
    numeric = pd.to_numeric(series, errors="coerce")
    if numeric.notna().all():
        return set(numeric.dropna().astype("int64").astype(str))
    return set(series.dropna().astype(str))


def validate_dataset(dataset_kind: str, root: Path | None = None, write_report: bool = True) -> list[str]:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    base = root / "data" / dataset_kind / "clean"
    errors: list[str] = []
    tables: dict[str, pd.DataFrame] = {}
    for table, expected_columns in TABLE_COLUMNS.items():
        path = base / f"{table}.csv"
        if not path.exists():
            errors.append(f"Falta {path}")
            continue
        df = read_csv(path)
        tables[table] = df
        if list(df.columns) != expected_columns:
            errors.append(f"{table}: columnas no coinciden con el esquema esperado.")
        pk = PRIMARY_KEYS[table]
        if df[pk].isna().any():
            errors.append(f"{table}: llave primaria {pk} contiene nulos.")
        if df[pk].duplicated().any():
            errors.append(f"{table}: llave primaria {pk} contiene duplicados.")

    for parent, parent_key, child, child_key in RELATIONSHIPS:
        if parent not in tables or child not in tables:
            continue
        parent_values = _key_set(tables[parent][parent_key])
        child_values = _key_set(tables[child][child_key])
        missing = child_values - parent_values
        if missing:
            sample = sorted(list(missing))[:5]
            errors.append(f"Integridad referencial: {child}.{child_key} tiene valores fuera de {parent}.{parent_key}: {sample}")

    raw_root = root / "data" / dataset_kind / "raw"
    if raw_root.exists():
        if not (raw_root / "Fact_Energia_Wide.csv").exists():
            errors.append(f"{dataset_kind}: falta archivo raw ancho Fact_Energia_Wide.csv")
        wo_raw = raw_root / "Fact_OrdenesTrabajo.csv"
        if wo_raw.exists():
            wo = pd.read_csv(wo_raw)
            if not wo["WorkOrderID"].duplicated().any():
                errors.append(f"{dataset_kind}: raw Fact_OrdenesTrabajo no contiene duplicados controlados.")
            if "_SourceFile" not in wo.columns:
                errors.append(f"{dataset_kind}: raw no contiene columnas de exportación fuente.")

    if write_report:
        status = "OK" if not errors else "CON ERRORES"
        body = f"# Validación dataset {dataset_kind}\n\nEstado: {status}\n\n"
        body += "\n".join(f"- {error}" for error in errors) if errors else "- Schema, llaves y relaciones principales validadas.\n"
        write_text(body, root / "reports" / "data_quality" / f"{dataset_kind}_validation.md", root)
    return errors


def validate_all(root: Path | None = None) -> dict[str, list[str]]:
    return {kind: validate_dataset(kind, root) for kind in ["training", "project"]}
