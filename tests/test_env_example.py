from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_env_example_contains_required_flags():
    text = (ROOT / ".env.example").read_text(encoding="utf-8")
    for name in ["RANDOM_SEED", "GENERATE_TRAINING_DATASET", "GENERATE_PROJECT_DATASET", "CREATE_PBIX", "AI_API_CALLS_ENABLED"]:
        assert name in text
    assert "CREATE_PBIX=false" in text
    assert "ALLOW_EXTERNAL_AI_CALLS=false" in text
