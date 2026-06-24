from __future__ import annotations

from pathlib import Path
import re
import shutil

import pytest


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def local_tmp_path(request: pytest.FixtureRequest) -> Path:
    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.name)
    path = ROOT / "artifacts" / "local" / "pytest_tmp" / safe_name
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)
    yield path
    shutil.rmtree(path, ignore_errors=True)
