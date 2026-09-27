import ast
import re
from pathlib import Path


PASSWORD_PATTERN = re.compile(
    r"(password|passwd|pwd|secret)\s*=\s*['\"].+?['\"]",
    re.IGNORECASE
)

API_KEY_PATTERN = re.compile(
    r"(api[_-]?key|token)\s*=\s*['\"].+?['\"]",
    re.IGNORECASE
)


def scan_security(repository_path: str):

    repository = Path(repository_path)

    issues = []

    for file in repository.rglob("*.py"):

        try:

            source = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            # ------------------------
            # Regex checks
            # ------------------------

            for line_number, line in enumerate(
                source.splitlines(),
                start=1
            ):

                if PASSWORD_PATTERN.search(line):

                    issues.append({
                        "type": "Hardcoded Password",
                        "file": str(file.relative_to(repository)),
                        "line": line_number,
                        "code": line.strip()
                    })

                if API_KEY_PATTERN.search(line):

                    issues.append({
                        "type": "Hardcoded API Key",
                        "file": str(file.relative_to(repository)),
                        "line": line_number,
                        "code": line.strip()
                    })

            # ------------------------
            # AST checks
            # ------------------------

            tree = ast.parse(source)

            for node in ast.walk(tree):

                if isinstance(node, ast.Call):

                    if isinstance(node.func, ast.Name):

                        if node.func.id in ("eval", "exec"):

                            issues.append({
                                "type": "Dangerous Function",
                                "file": str(file.relative_to(repository)),
                                "line": node.lineno,
                                "code": node.func.id
                            })

                    elif isinstance(node.func, ast.Attribute):

                        if node.func.attr in ("md5", "sha1"):

                            issues.append({
                                "type": "Weak Hash Function",
                                "file": str(file.relative_to(repository)),
                                "line": node.lineno,
                                "code": node.func.attr
                            })

        except Exception:
            continue

    return {
        "total_issues": len(issues),
        "issues": issues
    }