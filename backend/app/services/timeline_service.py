from pathlib import Path
from datetime import datetime


def analyze_repository_timeline(repository_path: str):

    repository = Path(repository_path)

    oldest = None
    newest = None

    python_files = 0

    for file in repository.rglob("*.py"):

        python_files += 1

        try:

            modified = datetime.fromtimestamp(
                file.stat().st_mtime
            )

            if oldest is None or modified < oldest:
                oldest = modified

            if newest is None or modified > newest:
                newest = modified

        except Exception:
            continue

    return {
        "python_files": python_files,
        "oldest_modified": (
            oldest.strftime("%Y-%m-%d %H:%M:%S")
            if oldest else None
        ),
        "latest_modified": (
            newest.strftime("%Y-%m-%d %H:%M:%S")
            if newest else None
        )
    }