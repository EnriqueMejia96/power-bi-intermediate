from __future__ import annotations
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from src.data.profile_dataset import profile_dataset

parser = argparse.ArgumentParser()
parser.add_argument("--dataset", choices=["training", "project", "all"], default="all")
args = parser.parse_args()
for dataset in (["training", "project"] if args.dataset == "all" else [args.dataset]):
    print(profile_dataset(dataset, ROOT))
