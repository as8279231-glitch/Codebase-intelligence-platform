from pathlib import Path

# Folders we never want to scan
IGNORE_FOLDERS = {
    ".git",
    "__pycache__",
    "node_modules",
    "venv",
    ".venv"
}


def scan_repository(repository_path: str):

    repository = Path(repository_path)

    files = []

    for file in repository.rglob("*"):

        if file.is_dir():
            continue

        if any(folder in file.parts for folder in IGNORE_FOLDERS):
            continue

        files.append(str(file.relative_to(repository)))

    return sorted(files)