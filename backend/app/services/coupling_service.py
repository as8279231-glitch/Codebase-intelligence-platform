import ast
from pathlib import Path


def analyze_coupling(repository_path: str):

    repository = Path(repository_path)

    results = []

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

            imports = set()
            classes = 0
            functions = 0

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:
                        imports.add(alias.name)

                elif isinstance(node, ast.ImportFrom):

                    if node.module:
                        imports.add(node.module)

                elif isinstance(node, ast.ClassDef):

                    classes += 1

                elif isinstance(node, ast.FunctionDef):

                    functions += 1

            coupling = len(imports)

            if coupling <= 5:
                level = "Low"
            elif coupling <= 15:
                level = "Medium"
            else:
                level = "High"

            results.append({
                "file": relative,
                "imports": coupling,
                "classes": classes,
                "functions": functions,
                "coupling": level
            })

        except Exception:
            continue

    if results:

        average = round(
            sum(r["imports"] for r in results)
            / len(results),
            2
        )

    else:

        average = 0

    if average <= 5:
        overall = "Low"
    elif average <= 15:
        overall = "Medium"
    else:
        overall = "High"

    return {
        "average_imports": average,
        "overall_coupling": overall,
        "files": results
    }