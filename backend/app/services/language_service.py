from pathlib import Path


def analyze_languages(repository_path: str):

    repository = Path(repository_path)

    extensions = {}
    total_files = 0

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        extension = file.suffix.lower()

        if extension == "":
            extension = "no_extension"

        extensions[extension] = (
            extensions.get(extension, 0) + 1
        )

        total_files += 1

    sorted_extensions = dict(
        sorted(
            extensions.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )

    return {
        "total_files": total_files,
        "languages": sorted_extensions
    }