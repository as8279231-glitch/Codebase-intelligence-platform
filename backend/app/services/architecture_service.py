from pathlib import Path


def analyze_architecture(repository_path: str):

    repository = Path(repository_path)

    folders = {}

    for file in repository.rglob("*.py"):

        try:
            relative = file.relative_to(repository)

            if len(relative.parts) > 1:
                folder = relative.parts[0]
            else:
                folder = "root"

            folders[folder] = folders.get(folder, 0) + 1

        except Exception:
            continue

    if folders:
        largest_layer = max(
            folders,
            key=folders.get
        )
    else:
        largest_layer = "Unknown"

    architecture_type = "Unknown"

    folder_names = set(
        name.lower()
        for name in folders.keys()
    )

    if {
        "api",
        "services",
        "models"
    }.issubset(folder_names):

        architecture_type = "Layered Architecture"

    elif {
        "controllers",
        "models",
        "views"
    }.issubset(folder_names):

        architecture_type = "MVC"

    elif {
        "routers",
        "schemas",
        "services"
    }.issubset(folder_names):

        architecture_type = "FastAPI Service"

    return {
        "layers": folders,
        "largest_layer": largest_layer,
        "architecture_type": architecture_type
    }