def generate_recommendations(
    health,
    security,
    todos,
    dead_code,
    complexity
):

    recommendations = []

    # ------------------------
    # Security
    # ------------------------

    if security["total_issues"] > 0:

        recommendations.append(
            f"Found {security['total_issues']} security issue(s). Replace weak hashes and remove hardcoded secrets."
        )

    else:

        recommendations.append(
            "No security issues detected."
        )

    # ------------------------
    # TODOs
    # ------------------------

    if todos["total_items"] > 0:

        recommendations.append(
            f"Resolve {todos['total_items']} TODO/FIXME comments."
        )

    else:

        recommendations.append(
            "No pending TODO comments."
        )

    # ------------------------
    # Dead Code
    # ------------------------

    if dead_code["unused_count"] > 0:

        recommendations.append(
            f"Remove or refactor {dead_code['unused_count']} unused functions."
        )

    else:

        recommendations.append(
            "No dead code detected."
        )

    # ------------------------
    # Complexity
    # ------------------------

    average = complexity.get(
        "average_complexity",
        0
    )

    if average > 10:

        recommendations.append(
            "High cyclomatic complexity. Consider splitting large functions."
        )

    elif average > 5:

        recommendations.append(
            "Moderate complexity. Some functions can be simplified."
        )

    else:

        recommendations.append(
            "Complexity is within a healthy range."
        )

    # ------------------------
    # Overall
    # ------------------------

    if health["score"] >= 90:

        recommendations.append(
            "Repository is in excellent condition."
        )

    elif health["score"] >= 70:

        recommendations.append(
            "Repository quality is good with minor improvements needed."
        )

    else:

        recommendations.append(
            "Repository requires refactoring before production."
        )

    return recommendations