from pathlib import Path


LICENSE_FILES = [
    "LICENSE",
    "LICENSE.txt",
    "LICENSE.md",
    "COPYING",
]


def detect_license(repository_path: str):

    repository = Path(repository_path)

    for name in LICENSE_FILES:

        file = repository / name

        if file.exists():

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

                if "mit license" in text:
                    license_name = "MIT"

                elif "apache license" in text:
                    license_name = "Apache 2.0"

                elif "gnu general public license" in text:
                    license_name = "GPL"

                elif "bsd" in text:
                    license_name = "BSD"

                else:
                    license_name = "Unknown"

                return {
                    "license_found": True,
                    "license_name": license_name,
                    "license_file": name
                }

            except Exception:
                pass

    return {
        "license_found": False,
        "license_name": "None",
        "license_file": None
    }