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
    extension_count = {}

    for file in repository.rglob("*"):

        # Skip folders
        if file.is_dir():
            continue

        # Skip ignored folders
        if any(folder in file.parts for folder in IGNORE_FOLDERS):
            continue

        # Count file extensions
        extension = file.suffix.lower()

        if extension in extension_count:
            extension_count[extension] += 1
        else:
            extension_count[extension] = 1

        # Store file information
        files.append(
            {
                "name": file.name,
                "path": str(file.relative_to(repository)),
                "extension": file.suffix,
                "size": file.stat().st_size
            }
        )

    return {
        "total_files": len(files),
        "extension_summary": extension_count,
        "files": files
    }