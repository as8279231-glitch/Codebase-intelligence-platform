def generate_repository_insights(
    summary,
    metrics,
    complexity,
    dead_code,
    todos,
    security,
    health,
):

    print("\n===== INSIGHTS SERVICE RUNNING =====")

    score = health.get("score", 0)
    grade = health.get("grade", "N/A")

    total_files = summary.get("total_python_files", 0)
    total_functions = summary.get("total_functions", 0)

    average_complexity = complexity.get(
        "average_complexity",
        0
    )

    security_issues = security.get(
        "total_issues",
        0
    )

    unused_functions = dead_code.get(
        "unused_count",
        0
    )

    todo_items = todos.get(
        "total_items",
        0
    )

    executive_summary = (
        f"This repository contains {total_files} Python files "
        f"with {total_functions} functions. "
        f"The average cyclomatic complexity is "
        f"{average_complexity:.2f}. "
        f"The project has {security_issues} security issues, "
        f"{unused_functions} unused functions, and "
        f"{todo_items} TODO comments. "
        f"Overall repository health is "
        f"{score}/100 ({grade})."
    )

    strengths = []

    if average_complexity <= 5:
        strengths.append(
            "Low average cyclomatic complexity indicates simple and maintainable functions."
        )

    if security_issues == 0:
        strengths.append(
            "No security vulnerabilities were detected."
        )

    if score >= 80:
        strengths.append(
            "Repository health score is excellent."
        )

    if total_files > 20:
        strengths.append(
            "Project is well structured with multiple Python modules."
        )

    risks = []

    if security_issues > 0:
        risks.append(
            f"{security_issues} security issues require immediate attention."
        )

    if unused_functions > 50:
        risks.append(
            f"{unused_functions} unused functions increase maintenance cost."
        )

    if todo_items > 20:
        risks.append(
            f"{todo_items} TODO/FIXME comments indicate unfinished work."
        )

    if score < 60:
        risks.append(
            "Overall repository health is below acceptable standards."
        )

    recommendations = []

    if security_issues > 0:
        recommendations.append(
            "Replace insecure hashing algorithms and remove hardcoded credentials."
        )

    if unused_functions > 50:
        recommendations.append(
            "Remove or refactor unused functions."
        )

    if todo_items > 20:
        recommendations.append(
            "Resolve TODO, FIXME and BUG comments."
        )

    if average_complexity > 10:
        recommendations.append(
            "Refactor highly complex functions into smaller units."
        )

    if score < 70:
        recommendations.append(
            "Improve maintainability before adding new features."
        )

    insights = {
        "executive_summary": executive_summary,
        "strengths": strengths,
        "risks": risks,
        "recommendations": recommendations
    }

    print("\n===== GENERATED INSIGHTS =====")
    print(insights)

    return insights