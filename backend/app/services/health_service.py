def calculate_health_score(
    metrics,
    complexity,
    dead_code,
    todos,
    security
):

    score = 100

    avg = complexity.get(
        "average_complexity",
        1
    )

    if avg > 10:
        score -= 20
    elif avg > 5:
        score -= 10

    score -= min(
        dead_code.get(
            "unused_count",
            0
        ),
        20
    )

    score -= min(
        todos.get(
            "total_items",
            0
        ),
        15
    )

    score -= security.get(
        "total_issues",
        0
    ) * 5

    score = max(score, 0)

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