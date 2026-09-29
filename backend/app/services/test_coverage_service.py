from pathlib import Path


def estimate_test_coverage(repository_path: str):

    repository = Path(repository_path)

    total_python_files = 0
    production_files = 0
    test_files = 0

    for file in repository.rglob("*.py"):

        total_python_files += 1

        name = file.name.lower()

        if (
            name.startswith("test_")
            or name.endswith("_test.py")
            or "tests" in str(file.parent).lower()
        ):
            test_files += 1
        else:
            production_files += 1

    estimated = 0

    if production_files > 0:
        estimated = round(
            (test_files / production_files) * 100,
            2
        )

    if estimated >= 80:
        quality = "Excellent"
    elif estimated >= 60:
        quality = "Good"
    elif estimated >= 30:
        quality = "Average"
    else:
        quality = "Poor"

    return {
        "production_files": production_files,
        "test_files": test_files,
        "estimated_coverage": estimated,
        "coverage_quality": quality
    }