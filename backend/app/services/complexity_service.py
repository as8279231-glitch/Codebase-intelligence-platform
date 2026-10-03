import ast
from pathlib import Path


class ComplexityVisitor(ast.NodeVisitor):

    def __init__(self):
        self.complexity = 1

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_Try(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complexity += len(node.values) - 1
        self.generic_visit(node)

    def visit_Match(self, node):
        self.complexity += len(node.cases)
        self.generic_visit(node)


def calculate_file_complexity(file_path: str):

    file = Path(file_path)

    source = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    tree = ast.parse(source)

    results = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            visitor = ComplexityVisitor()

            visitor.visit(node)

            results.append(
                {
                    "function": node.name,
                    "line": node.lineno,
                    "complexity": visitor.complexity
                }
            )

    return {
        "file_name": file.name,
        "functions": results
    }


def calculate_repository_complexity(repository_path: str):

    repository = Path(repository_path)

    python_files = sorted(
        repository.rglob("*.py")
    )
    results = []

    total_functions = 0
    total_complexity = 0

    highest_complexity = 0
    highest_complexity_function = "N/A"
    highest_complexity_file = "N/A"

# -------------------------
# Complexity Distribution
# -------------------------
    complexity_distribution = {}

    for file in python_files:

        try:

            file_result = calculate_file_complexity(
                str(file)
            )

            results.append(file_result)

            for function in file_result["functions"]:

                total_functions += 1

                total_complexity += function["complexity"]

                level = function["complexity"]

                if level not in complexity_distribution:
                   complexity_distribution[level] = 0

                complexity_distribution[level] += 1

                if function["complexity"] > highest_complexity:

                    highest_complexity = function["complexity"]

                    highest_complexity_function = function["function"]

                    highest_complexity_file = file.name

        except Exception as e:

            results.append(
                {
                    "file_name": file.name,
                    "error": str(e)
                }
            )

    if total_functions > 0:

        average_complexity = round(
            total_complexity / total_functions,
            2
        )

    else:

        average_complexity = 0

    return {
    "repository": repository.name,

    "total_python_files": len(python_files),

    "total_functions": total_functions,

    "average_complexity": average_complexity,

    "highest_complexity": highest_complexity,

    "highest_complexity_function": highest_complexity_function,

    "highest_complexity_file": highest_complexity_file,

    "complexity_distribution": {
        "labels": [
            str(x)
            for x in sorted(complexity_distribution.keys())
        ],
        "values": [
            complexity_distribution[x]
            for x in sorted(complexity_distribution.keys())
        ]
    },

    "complexity": results
}