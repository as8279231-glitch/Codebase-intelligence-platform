from pathlib import Path


def analyze_documentation(repository_path: str):

    repository = Path(repository_path)

    python_files = 0
    files_with_docstring = 0
    total_comments = 0
    readme_exists = False

    for file in repository.rglob("*.py"):

        python_files += 1

        try:

            content = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if '"""' in content or "'''" in content:
                files_with_docstring += 1

            total_comments += sum(
                1
                for line in content.splitlines()
                if line.strip().startswith("#")
            )

        except Exception:
            continue

    if (repository / "README.md").exists():
        readme_exists = True

    coverage = 0

    if python_files:
        coverage = round(
            files_with_docstring / python_files * 100,
            2
        )

    if coverage >= 80:
        quality = "Excellent"
    elif coverage >= 60:
        quality = "Good"
    elif coverage >= 40:
        quality = "Average"
    else:
        quality = "Poor"

    return {
        "python_files": python_files,
        "files_with_docstrings": files_with_docstring,
        "documentation_coverage": coverage,
        "comment_lines": total_comments,
        "readme_present": readme_exists,
        "documentation_quality": quality
    }