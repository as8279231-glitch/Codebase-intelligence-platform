from pathlib import Path


KEYWORDS = (
    "TODO",
    "FIXME",
    "BUG",
    "HACK"
)


def scan_todos(repository_path: str):

    repository = Path(repository_path)

    todos = []

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        try:
            lines = file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).splitlines()

            for line_number, line in enumerate(lines, start=1):

                upper_line = line.upper()

                for keyword in KEYWORDS:

                    if keyword in upper_line:

                        todos.append(
                            {
                                "file": str(
                                    file.relative_to(repository)
                                ),
                                "line": line_number,
                                "type": keyword,
                                "comment": line.strip()
                            }
                        )

                        break

        except Exception:
            continue

    return {
        "total_items": len(todos),
        "items": todos
    }