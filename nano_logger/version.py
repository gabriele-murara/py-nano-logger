import toml
from pathlib import Path

def get_version():
    pyproject_file = Path(__file__).parent.parent / "pyproject.toml"
    pyproject = toml.load(pyproject_file)
    return pyproject.get("project", {}).get("version", "0.0.0")

