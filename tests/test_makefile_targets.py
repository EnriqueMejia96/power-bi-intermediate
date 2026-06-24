from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_makefile_has_expected_targets():
    text = (ROOT / "Makefile").read_text(encoding="utf-8")
    for target in ["help", "setup", "check-env", "lint-structure", "data", "data-training", "data-project", "data-dictionary", "validate-data", "profile-data", "session01-materials", "report", "test", "clean-local", "reset-data"]:
        assert f"{target}:" in text
