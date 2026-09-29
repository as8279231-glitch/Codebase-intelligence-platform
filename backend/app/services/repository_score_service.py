def calculate_repository_score(

    health,
    maintainability,
    security,
    documentation,
    complexity,
    duplicate,
    technical_debt

):

    score = 100

    # -------------------------
    # Health
    # -------------------------

    score -= max(
        0,
        100 - health.get("score", 100)
    ) * 0.30

    # -------------------------
    # Maintainability
    # -------------------------

    score -= max(
        0,
        100 - maintainability.get("score", 100)
    ) * 0.20

    # -------------------------
    # Security
    # -------------------------

    score -= security.get(
        "total_issues",
        0
    ) * 2

    # -------------------------
    # Duplicate Code
    # -------------------------

    score -= duplicate.get(
        "duplicate_blocks",
        0
    ) * 1

    # -------------------------
    # Technical Debt
    # -------------------------

    score -= technical_debt.get(
        "estimated_hours",
        0
    ) * 0.5

    # -------------------------
    # Documentation
    # -------------------------

    score -= max(
        0,
        100 - documentation.get(
            "documentation_coverage",
            100
        )
    ) * 0.10

    # -------------------------
    # Complexity
    # -------------------------

    avg = complexity.get(
        "average_complexity",
        0
    )

    if avg > 10:
        score -= (avg - 10) * 2

    score = max(
        0,
        round(score, 2)
    )

    if score >= 90:
        rating = "Excellent"

    elif score >= 75:
        rating = "Good"

    elif score >= 60:
        rating = "Average"

    elif score >= 40:
        rating = "Poor"

    else:
        rating = "Critical"

    return {
        "score": score,
        "rating": rating
    }