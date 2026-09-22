from git import Repo
from pathlib import Path


# Folder where all cloned repositories will be stored
REPOSITORY_FOLDER = Path("repositories")


def clone_repository(github_url: str):
    """
    Clone a GitHub repository into the repositories folder.

    Args:
        github_url (str): GitHub repository URL

    Returns:
        dict: Information about the cloned repository
    """

    # Extract repository name from URL
    repository_name = github_url.rstrip("/").split("/")[-1]

    # Create destination path
    destination_path = REPOSITORY_FOLDER / repository_name

    # Create repositories folder if it doesn't exist
    REPOSITORY_FOLDER.mkdir(exist_ok=True)

    # Check if repository already exists
    if destination_path.exists():
        return {
            "status": "Repository already exists",
            "repository_name": repository_name,
            "path": str(destination_path)
        }

    # Clone repository
    Repo.clone_from(github_url, destination_path)

    return {
        "status": "Repository cloned successfully",
        "repository_name": repository_name,
        "path": str(destination_path)
    }
