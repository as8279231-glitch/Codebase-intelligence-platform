from collections import defaultdict
import os


def analyze_module_dependencies(analysis):

    module_dependencies = defaultdict(set)

    for file in analysis["parsed_files"]:

        if "error" in file:
            continue

        current_module = os.path.splitext(
            file["file_name"]
        )[0]

        for imported in file["imports"]:

            imported_module = imported.split(".")[0]

            module_dependencies[current_module].add(
                imported_module
            )

    return {
        "total_modules": len(module_dependencies),
        "dependencies": {
            module: sorted(list(deps))
            for module, deps in module_dependencies.items()
        }
    }