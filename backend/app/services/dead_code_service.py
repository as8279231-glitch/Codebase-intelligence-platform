import ast
from pathlib import Path


def detect_dead_code(repository_path: str):

    repository = Path(repository_path)

    defined_functions = set()
    called_functions = set()

    for file in repository.rglob("*.py"):

        try:
            source_code = file.read_text(encoding="utf-8")
            tree = ast.parse(source_code)

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):
                    defined_functions.add(node.name)

                elif isinstance(node, ast.Call):

                    if isinstance(node.func, ast.Name):
                        called_functions.add(node.func.id)

                    elif isinstance(node.func, ast.Attribute):
                        called_functions.add(node.func.attr)

        except Exception:
            continue

    unused_functions = sorted(
        defined_functions - called_functions
    )

    return {
        "total_functions": len(defined_functions),
        "used_functions": len(called_functions),
        "unused_functions": unused_functions,
        "unused_count": len(unused_functions)
    }