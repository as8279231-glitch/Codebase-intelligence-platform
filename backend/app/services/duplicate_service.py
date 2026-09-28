from pathlib import Path


MIN_LINES = 6


def detect_duplicate_blocks(repository_path: str):

    repository = Path(repository_path)

    blocks = {}
    duplicates = []

    for file in repository.rglob("*.py"):

        try:

            lines = file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).splitlines()

            relative = str(file.relative_to(repository))

            for i in range(
                len(lines) - MIN_LINES + 1
            ):

                block = "\n".join(
                    line.strip()
                    for line in lines[i:i + MIN_LINES]
                )

                if len(block.strip()) < 50:
                    continue

                if block in blocks:

                    duplicates.append({
                        "file1": blocks[block]["file"],
                        "line1": blocks[block]["line"],
                        "file2": relative,
                        "line2": i + 1
                    })

                else:

                    blocks[block] = {
                        "file": relative,
                        "line": i + 1
                    }

        except Exception:
            continue

    return {
        "duplicate_blocks": len(duplicates),
        "items": duplicates
    }