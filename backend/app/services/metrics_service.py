from pathlib import Path


def calculate_repository_metrics(repository_path: str, repository_analysis):

    repository = Path(repository_path)

    total_lines = 0
    total_files = 0
    total_functions = 0
    total_classes = 0

    largest_file = ""
    largest_file_lines = 0

    for file in repository.rglob("*.py"):

        try:
            with open(file, "r", encoding="utf-8") as f:
                line_count = len(f.readlines())

            total_lines += line_count
            total_files += 1

            if line_count > largest_file_lines:
                largest_file_lines = line_count
                largest_file = file.name

        except Exception:
            continue

    for parsed_file in repository_analysis["parsed_files"]:

        if "error" in parsed_file:
            continue

        total_functions += len(parsed_file["functions"])
        total_classes += len(parsed_file["classes"])

    average_lines = (
        total_lines / total_files
        if total_files else 0
    )

    average_functions = (
        total_functions / total_files
        if total_files else 0
    )

    average_classes = (
        total_classes / total_files
        if total_files else 0
    )

    return {
        "total_lines_of_code": total_lines,
        "average_lines_per_file": round(average_lines, 2),
        "average_functions_per_file": round(average_functions, 2),
        "average_classes_per_file": round(average_classes, 2),
        "largest_file": largest_file,
        "largest_file_lines": largest_file_lines
    }