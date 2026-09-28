from pathlib import Path


IGNORE = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    ".idea",
    ".vscode",
    ".pytest_cache",
    "dist",
    "build"
}


def build_repository_tree(repository_path: str):

    repository = Path(repository_path)

    tree = []

    def walk(directory: Path, prefix: str = ""):

        items = sorted(
            directory.iterdir(),
            key=lambda x: (x.is_file(), x.name.lower())
        )

        items = [
            item
            for item in items
            if item.name not in IGNORE
        ]

        for index, item in enumerate(items):

            connector = "└── " if index == len(items) - 1 else "├── "

            tree.append(
                prefix + connector + item.name
            )

            if item.is_dir():

                extension = (
                    "    "
                    if index == len(items) - 1
                    else "│   "
                )

                walk(
                    item,
                    prefix + extension
                )

    tree.append(repository.name)

    walk(repository)

    return {
        "repository": repository.name,
        "tree": "\n".join(tree)
    }