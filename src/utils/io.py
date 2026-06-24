from __future__ import annotations

from pathlib import Path
import json
import pandas as pd


def ensure_within_root(root: Path, path: Path) -> Path:
    resolved_root = root.resolve()
    resolved_path = path.resolve()
    resolved_path.relative_to(resolved_root)
    return resolved_path


def write_csv(df: pd.DataFrame, path: Path, root: Path) -> None:
    ensure_within_root(root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8")


def write_text(content: str, path: Path, root: Path) -> None:
    ensure_within_root(root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_json(data: dict, path: Path, root: Path) -> None:
    ensure_within_root(root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype_backend="numpy_nullable")
