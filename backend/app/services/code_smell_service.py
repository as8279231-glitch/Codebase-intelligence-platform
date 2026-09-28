import ast
from pathlib import Path


MAX_PARAMETERS = 5
MAX_FUNCTION_LINES = 50
MAX_CLASS_METHODS = 15
MAX_FILE_LINES = 500
MAX_NESTING = 4


class NestingVisitor(ast.NodeVisitor):

    def __init__(self):
        self.current_depth = 0
        self.max_depth = 0

    def generic_visit(self, node):

        if isinstance(
            node,
            (
                ast.If,
                ast.For,
                ast.While,
                ast.Try,
                ast.With,
                ast.Match,
            )
        ):
            self.current_depth += 1
            self.max_depth = max(
                self.max_depth,
                self.current_depth
            )

            super().generic_visit(node)

            self.current_depth -= 1

        else:
            super().generic_visit(node)


def detect_code_smells(repository_path: str):

    repository = Path(repository_path)

    smells = []

    for file in repository.rglob("*.py"):

        try:

            source = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            lines = source.splitlines()

            tree = ast.parse(source)

            # -------------------------
            # Large File
            # -------------------------

            if len(lines) > MAX_FILE_LINES:

                smells.append(
                    {
                        "type": "Large File",
                        "file": str(file.relative_to(repository)),
                        "line": 1,
                        "details": f"{len(lines)} lines"
                    }
                )

            for node in ast.walk(tree):

                # -------------------------
                # Functions
                # -------------------------

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
                            node.end_lineno -
                            node.lineno +
                            1
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

                    visitor = NestingVisitor()

                    visitor.visit(node)

                    if visitor.max_depth > MAX_NESTING:

                        smells.append(
                            {
                                "type": "Deep Nesting",
                                "file": str(file.relative_to(repository)),
                                "name": node.name,
                                "line": node.lineno,
                                "details": f"Depth {visitor.max_depth}"
                            }
                        )

                # -------------------------
                # Classes
                # -------------------------

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

        smell_summary = {}

    for smell in smells:
        smell_type = smell["type"]
        smell_summary[smell_type] = smell_summary.get(smell_type, 0) + 1

    worst_file = None

    if smells:
        file_count = {}

        for smell in smells:
            file_name = smell["file"]
            file_count[file_name] = file_count.get(file_name, 0) + 1

        worst_file = max(
            file_count,
            key=file_count.get
        )

    return {
        "total_smells": len(smells),
        "items": smells,
        "summary": smell_summary,
        "worst_file": worst_file
    }