import ast
from pathlib import Path


MAX_PARAMETERS = 5
MAX_FUNCTION_LINES = 50
MAX_CLASS_METHODS = 15


def detect_code_smells(repository_path: str):

    repository = Path(repository_path)

    smells = []

    for file in repository.rglob("*.py"):

        try:

            source = file.read_text(encoding="utf-8")
            tree = ast.parse(source)

            for node in ast.walk(tree):

                # ---------------------
                # Large Parameter List
                # ---------------------

                if isinstance(node, ast.FunctionDef):

                    parameter_count = len(node.args.args)

                    if parameter_count > MAX_PARAMETERS:

                        smells.append(
                            {
                                "type": "Too Many Parameters",
                                "file": str(file.relative_to(repository)),
                                "name": node.name,
                                "line": node.lineno,
                                "details": f"{parameter_count} parameters"
                            }
                        )

                    if hasattr(node, "end_lineno"):

                        function_length = (
                            node.end_lineno - node.lineno + 1
                        )

                        if function_length > MAX_FUNCTION_LINES:

                            smells.append(
                                {
                                    "type": "Long Function",
                                    "file": str(file.relative_to(repository)),
                                    "name": node.name,
                                    "line": node.lineno,
                                    "details": f"{function_length} lines"
                                }
                            )

                # ---------------------
                # Large Class
                # ---------------------

                elif isinstance(node, ast.ClassDef):

                    method_count = len(
                        [
                            n
                            for n in node.body
                            if isinstance(
                                n,
                                ast.FunctionDef
                            )
                        ]
                    )

                    if method_count > MAX_CLASS_METHODS:

                        smells.append(
                            {
                                "type": "Large Class",
                                "file": str(file.relative_to(repository)),
                                "name": node.name,
                                "line": node.lineno,
                                "details": f"{method_count} methods"
                            }
                        )

        except Exception:
            continue

    return {
        "total_smells": len(smells),
        "items": smells
    }