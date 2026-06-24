from __future__ import annotations

import argparse
from pathlib import Path

from src.config.settings import load_settings
from src.data.profile_dataset import profile_dataset
from src.data.validate_dataset import validate_dataset
from src.utils.io import write_text


def generate_dataset_report(dataset_kind: str, root: Path | None = None) -> Path:
    settings = load_settings(root)
    root = (root or settings.repo_root).resolve()
    errors = validate_dataset(dataset_kind, root)
    profile_path = profile_dataset(dataset_kind, root)
    status = "OK" if not errors else "Revisar validación"
    output = root / "artifacts" / "reports" / f"{dataset_kind}_dataset_report.md"
    write_text(
        f"# Reporte dataset {dataset_kind}\n\nEstado: {status}\n\nPerfil: `{profile_path.relative_to(root)}`\n\nErrores: {len(errors)}\n",
        output,
        root,
    )
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=["training", "project", "all"], default="all")
    args = parser.parse_args()
    datasets = ["training", "project"] if args.dataset == "all" else [args.dataset]
    for dataset in datasets:
        print(generate_dataset_report(dataset))


if __name__ == "__main__":
    main()
