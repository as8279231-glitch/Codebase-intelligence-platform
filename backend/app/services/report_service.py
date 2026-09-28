def generate_analysis_report(analysis: dict):

    summary = analysis.get("summary", {})
    metrics = analysis.get("metrics", {})
    complexity = analysis.get("complexity", {})
    security = analysis.get("security", {})
    todos = analysis.get("todos", {})
    dead_code = analysis.get("dead_code", {})
    health = analysis.get(
        "health",
        {
            "score": 0,
            "grade": "N/A"
        }
    )

    report = []

    report.append("=" * 50)
    report.append("CODEBASE INTELLIGENCE REPORT")
    report.append("=" * 50)

    report.append("")
    report.append(f"Repository : {analysis.get('repository', 'Unknown')}")
    report.append("")
    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 20)

    report.append(
    f"Health Score : {health['score']}/100 ({health['grade']})"
    )

    report.append(
    f"Security Issues : {security['total_issues']}"
    )

    report.append(
    f"Unused Functions : {dead_code['unused_count']}"
    )

    report.append(
    f"TODO Comments : {todos['total_items']}"
    )

    report.append(
    f"Average Complexity : {complexity['average_complexity']}"
    )

    # -------------------------
    # SUMMARY
    # -------------------------

    report.append("")
    report.append("SUMMARY")
    report.append("-" * 20)
    report.append(f"Python Files : {summary.get('total_python_files', 0)}")
    report.append(f"Functions    : {summary.get('total_functions', 0)}")
    report.append(f"Classes      : {summary.get('total_classes', 0)}")
    report.append(f"Imports      : {summary.get('total_imports', 0)}")

    # -------------------------
    # METRICS
    # -------------------------

    report.append("")
    report.append("METRICS")
    report.append("-" * 20)
    report.append(f"Lines of Code    : {metrics.get('total_lines_of_code', 0)}")
    report.append(f"Average LOC/File : {metrics.get('average_lines_per_file', 0)}")
    report.append(f"Largest File     : {metrics.get('largest_file', 'N/A')}")

    # -------------------------
    # COMPLEXITY
    # -------------------------

    report.append("")
    report.append("COMPLEXITY")
    report.append("-" * 20)

    files = complexity.get("complexity", [])

    total_functions = 0
    total_complexity = 0

    highest_file = "N/A"
    highest_function = "N/A"
    highest_complexity = 0

    for file in files:

        for function in file.get("functions", []):

            total_functions += 1
            total_complexity += function["complexity"]

            if function["complexity"] > highest_complexity:

                highest_complexity = function["complexity"]
                highest_function = function["function"]
                highest_file = file["file_name"]

    if total_functions > 0:
        average_complexity = round(
            total_complexity / total_functions,
            2
        )
    else:
        average_complexity = 0

    report.append(f"Functions Analyzed : {total_functions}")
    report.append(f"Average Complexity : {average_complexity}")
    report.append(
        f"Highest Complexity : {highest_function} ({highest_complexity}) in {highest_file}"
    )

    # -------------------------
    # HEALTH
    # -------------------------

    report.append("")
    report.append("HEALTH")
    report.append("-" * 20)
    report.append(f"Score : {health.get('score', 0)}")
    report.append(f"Grade : {health.get('grade', 'N/A')}")

    # -------------------------
    # SECURITY
    # -------------------------

    report.append("")
    report.append("SECURITY ISSUES")
    report.append("-" * 20)

    issues = security.get("issues", [])

    if issues:

       for i, issue in enumerate(issues, start=1):

        report.append(f"{i}. {issue['type']}")
        report.append(f"   File : {issue['file']}")
        report.append(f"   Line : {issue['line']}")
        report.append(f"   Code : {issue['code']}")
        report.append("")

    else:

          report.append("No security issues found.")

    # -------------------------
    # TODOS
    # -------------------------

    report.append("")
    report.append("TODOS")
    report.append("-" * 20)

    todo_items = todos.get("items", [])

    if todo_items:

       for i, todo in enumerate(todo_items[:10], start=1):

        report.append(f"{i}. {todo['type']}")
        report.append(f"   File : {todo['file']}")
        report.append(f"   Line : {todo['line']}")
        report.append(f"   Comment : {todo['comment']}")
        report.append("")

    else:

        report.append("No TODO comments found.")

    
    # -------------------------
    # RECOMMENDATIONS
    # -------------------------

    report.append("")
    report.append("RECOMMENDATIONS")
    report.append("-" * 20)

    recommendations = analysis.get(
       "recommendations",
        []
    )

    for i, recommendation in enumerate(recommendations, start=1):

       report.append(f"{i}. {recommendation}")


    # -------------------------
    # DEAD CODE
    # -------------------------

    report.append("")
    report.append("DEAD CODE")
    report.append("-" * 20)

    unused = dead_code.get("unused_functions", [])

    if unused:

     report.append(
        f"Unused Functions : {dead_code['unused_count']}"
    )

    report.append("")

    for i, function in enumerate(unused[:10], start=1):

        report.append(f"{i}. {function}")

    else:

        report.append("No unused functions detected.")

    return "\n".join(report)