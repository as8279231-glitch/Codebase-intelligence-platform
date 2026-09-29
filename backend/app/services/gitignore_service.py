from pathlib import Path


IMPORTANT_FOLDERS = [
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache"
]


def analyze_gitignore(repository_path: str):

    repository = Path(repository_path)

    gitignore = repository / ".gitignore"

    if not gitignore.exists():

        return {
            "gitignore_present": False,
            "ignored_items": [],
            "missing_recommended": IMPORTANT_FOLDERS
        }

    try:

        content = gitignore.read_text(
            encoding="utf-8",
            errors="ignore"
        ).splitlines()

    except Exception:

        content = []

    ignored = [
        line.strip()
        for line in content
        if line.strip() and not line.startswith("#")
    ]

    missing = []

    for folder in IMPORTANT_FOLDERS:

        if folder not in ignored:

            missing.append(folder)

    return {
        "gitignore_present": True,
        "ignored_items": ignored,
        "missing_recommended": missing
    }