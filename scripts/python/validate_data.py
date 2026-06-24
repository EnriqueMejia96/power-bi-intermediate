from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.data.validate_dataset import validate_dataset

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", choices=["training", "project", "all"], default="all")
args = parser.parse_args()
datasets = ["training", "project"] if args.dataset == "all" else [args.dataset]
all_errors = []
for dataset in datasets:
    errors = validate_dataset(dataset, ROOT)
    all_errors.extend(errors)
    print(f"{dataset}: {'OK' if not errors else str(len(errors)) + ' errores'}")
if all_errors:
    raise SystemExit(1)
