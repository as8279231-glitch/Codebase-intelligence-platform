from pathlib import Path
import ast


def analyze_imports(repository_path: str):

    repository = Path(repository_path)

    imports = {}

    for file in repository.rglob("*.py"):

        try:

            tree = ast.parse(
                file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        imports[alias.name] = (
                            imports.get(alias.name, 0) + 1
                        )

                elif isinstance(node, ast.ImportFrom):

                    if node.module:

                        imports[node.module] = (
                            imports.get(node.module, 0) + 1
                        )

        except Exception:
            continue

    return {
        "total_unique_imports": len(imports),
        "top_imports": dict(
            sorted(
                imports.items(),
                key=lambda x: x[1],
                reverse=True
            )[:15]
        )
    }