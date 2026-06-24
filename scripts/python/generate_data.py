from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from src.config.settings import load_settings
from src.data.generate_techeng_dataset import generate_all, generate_dataset

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", choices=["training", "project", "all"], default="all")
parser.add_argument("--small", action="store_true", help="Usa volúmenes pequeños para CI o pruebas rápidas.")
parser.add_argument("--require-overwrite", action="store_true", help="Solo ejecuta si OVERWRITE_DATA=true.")
args = parser.parse_args()

settings = load_settings(ROOT)
if args.small:
    settings = settings.with_small_counts()
if args.require_overwrite and not settings.overwrite_data:
    raise SystemExit("reset-data bloqueado: define OVERWRITE_DATA=true para regenerar de forma explícita.")
if args.dataset == "all":
    print(generate_all(settings, ROOT))
else:
    print(generate_dataset(args.dataset, settings, ROOT))
