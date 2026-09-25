import ast
from pathlib import Path


def parse_python_file(file_path: str):

    file = Path(file_path)

    if not file.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")

    source_code = file.read_text(encoding="utf-8")

    tree = ast.parse(source_code)

    imports = []
    classes = []
    functions = []

    for node in ast.walk(tree):

        # -----------------------
        # Imports
        # -----------------------

        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)

        # -----------------------
        # Classes
        # -----------------------

        elif isinstance(node, ast.ClassDef):

            classes.append({
                "name": node.name,
                "line": node.lineno,
                "methods": len(
                    [
                        n for n in node.body
                        if isinstance(n, ast.FunctionDef)
                    ]
                )
            })

        # -----------------------
        # Functions
        # -----------------------

        elif isinstance(node, ast.FunctionDef):

            functions.append({
                "name": node.name,
                "arguments": [
                    arg.arg
                    for arg in node.args.args
                ],
                "line": node.lineno,
                "async": False,
                "docstring": ast.get_docstring(node)
            })

        elif isinstance(node, ast.AsyncFunctionDef):

            functions.append({
                "name": node.name,
                "arguments": [
                    arg.arg
                    for arg in node.args.args
                ],
                "line": node.lineno,
                "async": True,
                "docstring": ast.get_docstring(node)
            })

    return {
        "file_name": file.name,
        "imports": sorted(set(imports)),
        "classes": classes,
        "functions": functions
    }

def parse_repository(repository_path: str):

    repository = Path(repository_path)

    if not repository.exists():
        raise FileNotFoundError(f"{repository_path} does not exist.")

    python_files = sorted(repository.rglob("*.py"))

    results = []

    for file in python_files:

        try:
            parsed = parse_python_file(str(file))
            results.append(parsed)

        except Exception as e:

            results.append({
                "file_name": file.name,
                "error": str(e)
            })

    return {
        "repository": repository.name,
        "total_python_files": len(python_files),
        "parsed_files": results
    }