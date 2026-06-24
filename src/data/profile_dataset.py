from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.config.settings import load_settings
from src.data.schema import TABLE_COLUMNS
from src.utils.io import read_csv, write_text


def profile_dataset(dataset_kind: str, root: Path | None = None) -> Path:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    clean_root = root / "data" / dataset_kind / "clean"
    lines = [f"# Perfil dataset {dataset_kind}", ""]
    for table in TABLE_COLUMNS:
        path = clean_root / f"{table}.csv"
        if not path.exists():
            lines.append(f"## {table}\nArchivo no encontrado.\n")
            continue
        df = read_csv(path)
        lines.append(f"## {table}")
        lines.append(f"- Filas: {len(df)}")
        lines.append(f"- Columnas: {len(df.columns)}")
        nulls = df.isna().sum()
        top_nulls = nulls[nulls > 0].sort_values(ascending=False).head(5)
        if len(top_nulls):
            lines.append("- Nulos principales: " + ", ".join(f"{col}={int(val)}" for col, val in top_nulls.items()))
        else:
            lines.append("- Nulos principales: sin nulos críticos.")
        numeric = df.select_dtypes(include="number")
        if not numeric.empty:
            lines.append("- Columnas numéricas: " + ", ".join(numeric.columns[:8]))
        lines.append("")
    output = root / "reports" / "dataset_profile" / f"{dataset_kind}_profile.md"
    write_text("\n".join(lines), output, root)
    return output
