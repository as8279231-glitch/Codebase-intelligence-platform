def build_dependency_graph(repository_analysis):

    graph = {}

    for file in repository_analysis["parsed_files"]:

        # Skip files that failed to parse
        if "error" in file:
            continue

        graph[file["file_name"]] = sorted(file["imports"])

    return {
        "total_files": len(graph),
        "dependency_graph": graph
    }