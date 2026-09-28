print("===== DASHBOARD SERVICE LOADED =====")

def generate_dashboard(
    summary,
    metrics,
    complexity,
    health,
    security,
    dead_code,
    todos,
    code_smells
):

    print("===== DASHBOARD SERVICE LOADED =====")

    score = health.get("score", 0)
    grade = health.get("grade", "N/A")

    critical_issues = security.get("total_issues", 0)

    major_issues = (
        dead_code.get("unused_count", 0)
        + code_smells.get("total_smells", 0)
    )

    minor_issues = todos.get("total_items", 0)

    # -------------------------
    # Risk Level
    # -------------------------

    if score >= 80:
        risk_level = "Low"
    elif score >= 60:
        risk_level = "Medium"
    elif score >= 40:
        risk_level = "High"
    else:
        risk_level = "Critical"

    # -------------------------
    # Maintainability
    # -------------------------

    if grade in ("A+", "A"):
        maintainability = "Excellent"
    elif grade == "B":
        maintainability = "Good"
    elif grade == "C":
        maintainability = "Fair"
    elif grade == "D":
        maintainability = "Poor"
    else:
        maintainability = "Very Poor"

    # -------------------------
    # Security
    # -------------------------

    if critical_issues == 0:
        security_status = "Excellent"
    elif critical_issues <= 5:
        security_status = "Needs Attention"
    else:
        security_status = "Critical"

    # -------------------------
    # Complexity
    # -------------------------

    avg_complexity = complexity.get(
    "average_complexity",
    0
    )

    if avg_complexity <= 5:
        complexity_status = "Good"
    elif avg_complexity <= 10:
        complexity_status = "Moderate"
    else:
        complexity_status = "Complex"

    # -------------------------
    # Documentation
    # -------------------------

    if minor_issues <= 10:
        documentation = "Good"
    elif minor_issues <= 50:
        documentation = "Average"
    else:
        documentation = "Needs Improvement"

    return {
        "health_score": score,
        "grade": grade,
        "critical_issues": critical_issues,
        "major_issues": major_issues,
        "minor_issues": minor_issues,
        "risk_level": risk_level,
        "maintainability": maintainability,
        "security": security_status,
        "complexity": complexity_status,
        "documentation": documentation,
        "quick_stats": {
            "files": summary.get("total_python_files", 0),
            "functions": summary.get("total_functions", 0),
            "classes": summary.get("total_classes", 0),
            "loc": metrics.get("total_lines_of_code", 0)
        }
    }
