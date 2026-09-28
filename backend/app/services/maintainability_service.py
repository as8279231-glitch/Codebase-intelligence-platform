def calculate_maintainability_index(
    metrics,
    complexity,
    dead_code,
    code_smells
):

    score = 100

    avg_complexity = complexity.get(
        "average_complexity",
        0
    )

    score -= avg_complexity * 2

    score -= (
        dead_code.get(
            "unused_count",
            0
        ) * 0.05
    )

    score -= (
        code_smells.get(
            "total_smells",
            0
        ) * 0.5
    )

    if score < 0:
        score = 0

    if score >= 85:
        grade = "Excellent"
    elif score >= 70:
        grade = "Good"
    elif score >= 55:
        grade = "Fair"
    elif score >= 40:
        grade = "Poor"
    else:
        grade = "Very Poor"

    return {
        "index": round(score, 2),
        "rating": grade
    }