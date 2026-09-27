def calculate_health_score(
    metrics,
    complexity,
    dead_code,
    todos,
    security
):

    score = 100

    # ------------------------
    # Complexity penalty
    # ------------------------

    average_complexity = complexity.get(
        "average_complexity",
        1
    )

    if average_complexity > 10:
        score -= 20

    elif average_complexity > 5:
        score -= 10

    # ------------------------
    # Dead code penalty
    # ------------------------

    score -= min(
        dead_code["unused_count"],
        20
    )

    # ------------------------
    # TODO penalty
    # ------------------------

    score -= min(
        todos["total_items"],
        15
    )

    # ------------------------
    # Security penalty
    # ------------------------

    score -= security["total_issues"] * 5

    score = max(score, 0)

    # ------------------------
    # Grade
    # ------------------------

    if score >= 90:
        grade = "A+"

    elif score >= 80:
        grade = "A"

    elif score >= 70:
        grade = "B"

    elif score >= 60:
        grade = "C"

    elif score >= 50:
        grade = "D"

    else:
        grade = "F"

    return {
        "score": score,
        "grade": grade
    }