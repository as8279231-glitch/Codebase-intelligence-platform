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

    source = file.read_text(encoding="utf-8")

    tree = ast.parse(source)

    results = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            visitor = ComplexityVisitor()

            visitor.visit(node)

            results.append({
                "function": node.name,
                "line": node.lineno,
                "complexity": visitor.complexity
            })

    return {
        "file_name": file.name,
        "functions": results
    }

def calculate_repository_complexity(repository_path: str):

    repository = Path(repository_path)

    python_files = sorted(repository.rglob("*.py"))

    results = []

    for file in python_files:

        try:
            results.append(
                calculate_file_complexity(str(file))
            )

        except Exception as e:

            results.append({
                "file_name": file.name,
                "error": str(e)
            })

    return {
        "repository": repository.name,
        "total_python_files": len(python_files),
        "complexity": results
    }
