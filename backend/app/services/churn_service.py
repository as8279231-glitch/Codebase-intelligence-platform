from pathlib import Path
from datetime import datetime


def estimate_code_churn(repository_path: str):

    repository = Path(repository_path)

    recently_modified = 0
    stale_files = 0

    newest = None
    oldest = None

    now = datetime.now().timestamp()

    for file in repository.rglob("*.py"):

        try:

            modified = file.stat().st_mtime

            age_days = (now - modified) / 86400

            if age_days <= 30:
                recently_modified += 1
            else:
                stale_files += 1

            if newest is None or modified > newest:
                newest = modified

            if oldest is None or modified < oldest:
                oldest = modified

        except Exception:
            continue

    if newest:
        newest = datetime.fromtimestamp(
            newest
        ).strftime("%Y-%m-%d")

    if oldest:
        oldest = datetime.fromtimestamp(
            oldest
        ).strftime("%Y-%m-%d")

    if recently_modified >= stale_files:
        activity = "Active"
    elif recently_modified > 0:
        activity = "Moderate"
    else:
        activity = "Inactive"

    return {
        "recently_modified_files": recently_modified,
        "stale_files": stale_files,
        "repository_activity": activity,
        "newest_file": newest,
        "oldest_file": oldest
    }