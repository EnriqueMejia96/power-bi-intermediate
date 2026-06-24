from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.reporting.generate_data_dictionary import generate_data_dictionary

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", choices=["training", "project", "all"], default="all")
args = parser.parse_args()
for dataset in (["training", "project"] if args.dataset == "all" else [args.dataset]):
    print(generate_data_dictionary(dataset, ROOT))
