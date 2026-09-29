import ast
from pathlib import Path


def analyze_cohesion(repository_path: str):

    repository = Path(repository_path)

    classes = []

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

            for node in tree.body:

                if not isinstance(node, ast.ClassDef):
                    continue

                methods = 0
                attributes = set()

                for item in node.body:

                    if isinstance(item, ast.FunctionDef):

                        methods += 1

                        for child in ast.walk(item):

                            if (
                                isinstance(child, ast.Attribute)
                                and isinstance(child.value, ast.Name)
                                and child.value.id == "self"
                            ):
                                attributes.add(child.attr)

                if methods == 0:

                    score = 100

                else:

                    score = round(
                        min(
                            100,
                            len(attributes) / methods * 100
                        ),
                        2
                    )

                if score >= 80:
                    quality = "High"
                elif score >= 60:
                    quality = "Medium"
                else:
                    quality = "Low"

                classes.append({
                    "class": node.name,
                    "file": relative,
                    "methods": methods,
                    "shared_attributes": len(attributes),
                    "cohesion_score": score,
                    "quality": quality
                })

        except Exception:
            continue

    if classes:

        average = round(
            sum(
                c["cohesion_score"]
                for c in classes
            ) / len(classes),
            2
        )

    else:

        average = 100

    if average >= 80:
        overall = "High"
    elif average >= 60:
        overall = "Medium"
    else:
        overall = "Low"

    return {
        "average_cohesion": average,
        "overall_quality": overall,
        "classes": classes
    }