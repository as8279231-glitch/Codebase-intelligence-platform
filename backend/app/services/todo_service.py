from pathlib import Path

KEYWORDS = (
    "TODO",
    "FIXME",
    "BUG",
    "HACK"
)


def scan_todos(repository_path: str):

    repository = Path(repository_path)

    items = []

    counts = {
        "TODO": 0,
        "FIXME": 0,
        "BUG": 0,
        "HACK": 0
    }

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        try:

            lines = file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).splitlines()

            for number, line in enumerate(lines, start=1):

                upper = line.upper()

                for keyword in KEYWORDS:

                    if keyword in upper:

                        counts[keyword] += 1

                        items.append({
                            "file": str(file.relative_to(repository)),
                            "line": number,
                            "type": keyword,
                            "comment": line.strip()
                        })

                        break

        except Exception:
            continue

    return {
        "total_items": len(items),
        "counts": counts,
        "items": items
    }