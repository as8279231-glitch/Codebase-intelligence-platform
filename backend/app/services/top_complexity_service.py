def get_top_complex_functions(complexity, top_n=10):

    all_functions = []

    for file in complexity.get("complexity", []):

        file_name = file.get("file_name")

        for function in file.get("functions", []):

            all_functions.append({
                "function": function["function"],
                "file": file_name,
                "line": function["line"],
                "complexity": function["complexity"]
            })

    all_functions.sort(
        key=lambda x: x["complexity"],
        reverse=True
    )

    return {
        "total_functions": len(all_functions),
        "top_functions": all_functions[:top_n]
    }