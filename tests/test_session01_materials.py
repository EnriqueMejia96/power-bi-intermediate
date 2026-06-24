from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_session01_materials_exist():
    required = [
        "session_01/lab/LAB_GUIDE.md",
        "session_01/templates/BI_SOLUTION_BLUEPRINT_TEMPLATE.md",
        "session_01/instructor/TIMING_PLAN_2H.md",
        "session_01/student/STUDENT_HANDOUT.md",
        "session_01/powerbi_manual/IMPORT_SAMPLE_DATA_STEPS.md",
    ]
    for relative in required:
        assert (ROOT / relative).exists(), relative
