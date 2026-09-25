from collections import Counter


def generate_repository_summary(repository_analysis):

    total_functions = 0
    total_classes = 0
    total_imports = 0

    largest_file = ""
    largest_function_count = -1

    imports_counter = Counter()

    for file in repository_analysis["parsed_files"]:

        if "error" in file:
            continue

        total_functions += len(file["functions"])
        total_classes += len(file["classes"])
        total_imports += len(file["imports"])

        imports_counter.update(file["imports"])

        if len(file["functions"]) > largest_function_count:
            largest_function_count = len(file["functions"])
            largest_file = file["file_name"]

    return {
        "repository": repository_analysis["repository"],
        "total_python_files": repository_analysis["total_python_files"],
        "total_functions": total_functions,
        "total_classes": total_classes,
        "total_imports": total_imports,
        "largest_file": largest_file,
        "most_imported_modules": imports_counter.most_common(10)
    }