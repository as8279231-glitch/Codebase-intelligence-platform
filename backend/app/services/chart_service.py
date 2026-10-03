from collections import Counter


def generate_repository_charts(
    metrics,
    complexity,
    language_statistics,
    code_smells,
    security,
    todos,
    dead_code,
    health
):

    charts = {}

    # ----------------------------------
    # Language Distribution
    # ----------------------------------

    charts["language_distribution"] = {
        "type": "pie",
        "title": "Language Distribution",
        "labels": list(
            language_statistics["languages"].keys()
        ),
        "values": list(
            language_statistics["languages"].values()
        ),
    }

    # ----------------------------------
    # Complexity Distribution
    # ----------------------------------

    if "complexity_distribution" in complexity:

        charts["complexity_distribution"] = {
            "type": "bar",
            "title": "Complexity Distribution",
            "labels": complexity["complexity_distribution"]["labels"],
            "values": complexity["complexity_distribution"]["values"],
        }

    else:

        complexity_levels = Counter()

        for file in complexity.get("complexity", []):

            for function in file.get("functions", []):

                score = function.get("complexity", 1)

                if score <= 5:
                    complexity_levels["Low"] += 1
                elif score <= 10:
                    complexity_levels["Medium"] += 1
                else:
                    complexity_levels["High"] += 1

        charts["complexity_distribution"] = {
            "type": "bar",
            "title": "Complexity Distribution",
            "labels": list(complexity_levels.keys()),
            "values": list(complexity_levels.values()),
        }

    # ----------------------------------
    # Repository Issues
    # ----------------------------------

    charts["issue_breakdown"] = {
        "type": "bar",
        "title": "Repository Issues",
        "labels": [
            "Security",
            "Code Smells",
            "TODOs",
            "Dead Code",
        ],
        "values": [
            security.get("total_issues", 0),
            code_smells.get("total_smells", 0),
            todos.get("total_items", 0),
            dead_code.get("unused_count", 0),
        ],
    }

    # ----------------------------------
    # Health Gauge
    # ----------------------------------

    charts["health_score"] = {
        "type": "gauge",
        "title": "Repository Health",
        "value": health.get("score", 0),
    }

    return charts