def generate_quality_badge(
    health,
    maintainability,
    security
):

    score = health.get("score", 0)

    security_issues = security.get(
        "total_issues",
        0
    )

    maintainability_rating = maintainability.get(
        "rating",
        ""
    )

    # -----------------------------
    # Grade
    # -----------------------------

    if score >= 90:
        grade = "A+"
        stars = 5

    elif score >= 80:
        grade = "A"
        stars = 5

    elif score >= 70:
        grade = "B"
        stars = 4

    elif score >= 60:
        grade = "C"
        stars = 3

    elif score >= 40:
        grade = "D"
        stars = 2

    else:
        grade = "F"
        stars = 1

    # -----------------------------
    # Overall Quality
    # -----------------------------

    if (
        security_issues == 0
        and maintainability_rating in (
            "Excellent",
            "Good"
        )
    ):
        quality = "Production Ready"

    elif score >= 70:
        quality = "Good"

    elif score >= 50:
        quality = "Needs Improvement"

    else:
        quality = "Poor"

    return {
        "grade": grade,
        "stars": "★" * stars,
        "quality": quality
    }