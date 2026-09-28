def detect_hotspots(
    complexity,
    dead_code,
    todos,
    code_smells
):

    hotspots = []

    complexity_items = {
        item["file"]: item["complexity"]
        for item in complexity.get(
            "functions",
            []
        )
    }

    dead_items = {}

    for item in dead_code.get(
        "unused_functions",
        []
    ):
        dead_items[item["file"]] = (
            dead_items.get(item["file"], 0) + 1
        )

    todo_items = {}

    for item in todos.get(
        "items",
        []
    ):
        todo_items[item["file"]] = (
            todo_items.get(item["file"], 0) + 1
        )

    smell_items = {}

    for item in code_smells.get(
        "items",
        []
    ):
        smell_items[item["file"]] = (
            smell_items.get(item["file"], 0) + 1
        )

    files = set()

    files.update(complexity_items.keys())
    files.update(dead_items.keys())
    files.update(todo_items.keys())
    files.update(smell_items.keys())

    for file in files:

        score = (
            complexity_items.get(file, 0)
            + dead_items.get(file, 0)
            + todo_items.get(file, 0)
            + smell_items.get(file, 0)
        )

        hotspots.append(
            {
                "file": file,
                "hotspot_score": score,
                "complexity": complexity_items.get(file, 0),
                "dead_code": dead_items.get(file, 0),
                "todos": todo_items.get(file, 0),
                "code_smells": smell_items.get(file, 0)
            }
        )

    hotspots.sort(
        key=lambda x: x["hotspot_score"],
        reverse=True
    )

    return hotspots[:15]