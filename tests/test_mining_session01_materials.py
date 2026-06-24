from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_session01_materials_explicitly_use_mining_case():
    files = [
        "session_01/README_SESSION_01.md",
        "session_01/lab/LAB_GUIDE.md",
        "session_01/lab/LAB_STEPS.md",
        "session_01/student/STUDENT_HANDOUT.md",
        "session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md",
        "session_01/prompts/AI_PROMPT_LIBRARY_SESSION_01.md",
    ]
    joined = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in files).lower()
    for term in ["minera", "chancado", "backlog", "energ", "hse", "power bi"]:
        assert term in joined


def test_mining_make_targets_and_instructor_only_report_are_present():
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    for target in ["mining-gap", "mining-upgrade", "data-mining", "validate-mining", "profile-mining", "mining-report"]:
        assert f"{target}:" in makefile

    instructor_report = ROOT / "reports" / "dataset_profile" / "MINING_ROOT_CAUSE_PATTERNS_INSTRUCTOR.md"
    assert instructor_report.exists()
    assert "INSTRUCTOR-ONLY" in instructor_report.read_text(encoding="utf-8")
    assert not (ROOT / "session_01" / "student" / "MINING_ROOT_CAUSE_PATTERNS_INSTRUCTOR.md").exists()
