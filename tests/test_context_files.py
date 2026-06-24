from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_context_files_are_useful():
    context_dir = ROOT / "ai_context"
    files = list(context_dir.glob("*.md"))
    assert len(files) >= 15
    for path in files:
        text = path.read_text(encoding="utf-8")
        assert "Propósito" in text
        assert len(text) > 500
