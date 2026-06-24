from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_ai_materials_include_privacy_and_validation():
    files = list((ROOT / "ai_tools/prompt_library").glob("*.md"))
    assert len(files) >= 4
    joined = "\n".join(path.read_text(encoding="utf-8") for path in files)
    assert "privacidad" in joined.lower()
    assert "validación humana" in joined.lower()
    assert (ROOT / "ai_tools/responsible_ai/responsible_ai_checklist.md").exists()
