from pathlib import Path


def analyze_language_statistics(repository_path: str):

    repository = Path(repository_path)

    extensions = {}
    total_files = 0

    for file in repository.rglob("*"):

        if not file.is_file():
            continue

        total_files += 1

        ext = file.suffix.lower()

        if ext == "":
            ext = "no_extension"

        extensions[ext] = extensions.get(ext, 0) + 1

    languages = {}

    mapping = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".html": "HTML",
        ".css": "CSS",
        ".json": "JSON",
        ".md": "Markdown",
        ".yml": "YAML",
        ".yaml": "YAML",
        ".xml": "XML",
        ".txt": "Text"
    }

    for ext, count in extensions.items():

        language = mapping.get(ext, ext)

        languages[language] = (
            languages.get(language, 0)
            + count
        )

    return {
        "total_files": total_files,
        "languages": dict(
            sorted(
                languages.items(),
                key=lambda x: x[1],
                reverse=True
            )
        )
    }