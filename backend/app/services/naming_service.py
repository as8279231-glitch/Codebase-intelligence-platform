import ast
from pathlib import Path


BAD_NAMES = {
    "a", "b", "c",
    "x", "y", "z",
    "i", "j", "k",
    "tmp", "temp",
    "var", "test",
    "obj", "data",
    "foo", "bar"
}


def analyze_naming_quality(repository_path: str):

    repository = Path(repository_path)

    total_names = 0
    poor_names = []

    for file in repository.rglob("*.py"):

        try:

            tree = ast.parse(
                file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )

            relative = str(
                file.relative_to(repository)
            )

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):

                    total_names += 1

                    if (
                        len(node.name) <= 2
                        or node.name.lower() in BAD_NAMES
                    ):

                        poor_names.append({
                            "type": "Function",
                            "name": node.name,
                            "file": relative,
                            "line": node.lineno
                        })

                elif isinstance(node, ast.ClassDef):

                    total_names += 1

                    if (
                        len(node.name) <= 2
                        or node.name.lower() in BAD_NAMES
                    ):

                        poor_names.append({
                            "type": "Class",
                            "name": node.name,
                            "file": relative,
                            "line": node.lineno
                        })

                elif isinstance(node, ast.Name):

                    total_names += 1

                    if (
                        len(node.id) == 1
                        or node.id.lower() in BAD_NAMES
                    ):

                        poor_names.append({
                            "type": "Variable",
                            "name": node.id,
                            "file": relative,
                            "line": getattr(
                                node,
                                "lineno",
                                0
                            )
                        })

        except Exception:
            continue

    good_names = total_names - len(poor_names)

    score = 100

    if total_names:

        score = round(
            good_names / total_names * 100,
            2
        )

    if score >= 90:
        quality = "Excellent"
    elif score >= 75:
        quality = "Good"
    elif score >= 60:
        quality = "Average"
    else:
        quality = "Poor"

    return {
        "score": score,
        "quality": quality,
        "total_identifiers": total_names,
        "poor_names": len(poor_names),
        "items": poor_names
    }