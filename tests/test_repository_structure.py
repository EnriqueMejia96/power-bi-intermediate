from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_expected_directories_exist():
    expected = [
        "ai_context", "session_01/lab", "data/training/raw", "data/training/clean",
        "data/project/raw", "data/project/clean", "src/data", "powerbi/manual_steps",
        "ai_tools/prompt_library", "notebooklm/prompts",
    ]
    for item in expected:
        assert (ROOT / item).is_dir(), item
