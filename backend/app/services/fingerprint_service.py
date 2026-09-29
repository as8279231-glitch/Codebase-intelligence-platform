from pathlib import Path
import hashlib


def generate_repository_fingerprint(repository_path: str):

    repository = Path(repository_path)

    sha = hashlib.sha256()

    file_count = 0

    for file in sorted(repository.rglob("*")):

        if not file.is_file():
            continue

        file_count += 1

        try:

            sha.update(
                str(file.relative_to(repository)).encode()
            )

            sha.update(
                str(file.stat().st_size).encode()
            )

        except Exception:
            continue

    return {
        "repository_hash": sha.hexdigest(),
        "files_hashed": file_count
    }