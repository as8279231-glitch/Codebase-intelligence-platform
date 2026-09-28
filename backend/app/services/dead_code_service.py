import ast
from pathlib import Path


def detect_dead_code(repository_path: str):

    repository = Path(repository_path)

    defined = {}
    called = set()

    for file in repository.rglob("*.py"):

        try:
            tree = ast.parse(
                file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )

            relative = str(file.relative_to(repository))

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):

                    defined[node.name] = {
                        "file": relative,
                        "line": node.lineno
                    }

                elif isinstance(node, ast.Call):

                    if isinstance(node.func, ast.Name):
                        called.add(node.func.id)

                    elif isinstance(node.func, ast.Attribute):
                        called.add(node.func.attr)

        except Exception:
            continue

    unused = []

    for function, info in defined.items():

        if function not in called:

            unused.append({
                "function": function,
                "file": info["file"],
                "line": info["line"]
            })

    unused.sort(
        key=lambda x: x["function"]
    )

    return {
        "total_functions": len(defined),
        "used_functions": len(called),
        "unused_count": len(unused),
        "unused_functions": unused
    }