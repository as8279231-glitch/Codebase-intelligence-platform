import ast
from pathlib import Path


class CallVisitor(ast.NodeVisitor):

    def __init__(self):
        self.calls = []

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):
            self.calls.append(node.func.id)

        elif isinstance(node.func, ast.Attribute):
            self.calls.append(node.func.attr)

        self.generic_visit(node)


def build_call_graph(file_path: str):

    file = Path(file_path)

    source = file.read_text(encoding="utf-8")

    tree = ast.parse(source)

    graph = []

    for node in tree.body:

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            visitor = CallVisitor()

            visitor.visit(node)

            graph.append({
                "function": node.name,
                "calls": sorted(set(visitor.calls))
            })

    return {
        "file_name": file.name,
        "call_graph": graph
    }

def build_repository_call_graph(repository_path: str):

    repository = Path(repository_path)

    python_files = sorted(repository.rglob("*.py"))

    results = []

    for file in python_files:

        try:

            results.append(
                build_call_graph(str(file))
            )

        except Exception as e:

            results.append({
                "file_name": file.name,
                "error": str(e)
            })

    return {
        "repository": repository.name,
        "total_python_files": len(python_files),
        "call_graph": results
    }