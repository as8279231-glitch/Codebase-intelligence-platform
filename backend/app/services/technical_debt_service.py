def calculate_technical_debt(
    dead_code,
    todos,
    security,
    code_smells
):

    unused = dead_code.get(
        "unused_count",
        0
    )

    todo_count = todos.get(
        "total_items",
        0
    )

    security_count = security.get(
        "total_issues",
        0
    )

    smell_count = code_smells.get(
        "total_smells",
        0
    )

    estimated_hours = round(
        (
            unused * 0.05 +
            todo_count * 0.03 +
            security_count * 0.50 +
            smell_count * 0.15
        ),
        1
    )

    return {

        "unused_functions": unused,

        "todo_comments": todo_count,

        "security_issues": security_count,

        "code_smells": smell_count,

        "estimated_cleanup_hours": estimated_hours
    }