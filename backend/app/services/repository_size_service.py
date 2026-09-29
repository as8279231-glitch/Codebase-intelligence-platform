from pathlib import Path


def analyze_repository_size(repository_path: str):

    repository = Path(repository_path)

    total_size = 0
    largest_file = None
    largest_size = 0

    python_files = 0
    total_files = 0

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        total_files += 1

        if file.suffix == ".py":
            python_files += 1

        try:

            size = file.stat().st_size

            total_size += size

            if size > largest_size:
                largest_size = size
                largest_file = str(
                    file.relative_to(repository)
                )

        except Exception:
            continue

    return {
        "repository_size_mb": round(
            total_size / (1024 * 1024),
            2
        ),
        "total_files": total_files,
        "python_files": python_files,
        "largest_file": largest_file,
        "largest_file_size_kb": round(
            largest_size / 1024,
            2
        )
    }