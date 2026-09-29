from pathlib import Path


def analyze_code_ownership(repository_path: str):

    repository = Path(repository_path)

    folders = {}

    for file in repository.rglob("*.py"):

        try:

            relative = file.relative_to(repository)

            if len(relative.parts) > 1:
                owner = relative.parts[0]
            else:
                owner = "root"

            folders[owner] = folders.get(owner, 0) + 1

        except Exception:
            continue

    largest_owner = None
    largest_files = 0

    if folders:
        largest_owner = max(
            folders,
            key=folders.get
        )
        largest_files = folders[largest_owner]

    return {
        "ownership": folders,
        "largest_module": largest_owner,
        "largest_module_files": largest_files
    }