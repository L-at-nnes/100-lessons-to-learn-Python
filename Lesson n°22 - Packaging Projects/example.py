"""Lesson 22 - Packaging Projects

Goal: structure a Python package with pyproject.toml, setup.cfg, and entry points.
"""

import subprocess
from pathlib import Path

PROJECT = Path(__file__).parent / "study_package"
PACKAGE_DIR = PROJECT / "studyhelper"


def scaffold() -> None:
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    (PACKAGE_DIR / "__init__.py").write_text("__all__ = ['tracker']\n")
    (PACKAGE_DIR / "tracker.py").write_text(
        "def greet(name):\n    return f'Keep going, {name}!"\n",
        encoding="utf-8",
    )

    pyproject = PROJECT / "pyproject.toml"
    pyproject.write_text(
        """
        [build-system]
        requires = ["setuptools", "wheel"]
        build-backend = "setuptools.build_meta"
        
        [project]
        name = "studyhelper"
        version = "0.1.0"
        description = "Helpers for tracking study sessions"
        readme = "README.md"
        authors = [{name = "Alex Learner"}]
        license = {text = "MIT"}
        dependencies = ["rich"]
        
        [project.scripts]
        study-helper = "studyhelper.tracker:greet"
        """
        .strip(),
        encoding="utf-8",
    )

def build_package() -> None:
    subprocess.run(["python", "-m", "build"], cwd=PROJECT, check=True)

if __name__ == "__main__":
    scaffold()
    print("Project scaffolded at", PROJECT)
    print("Run python -m build to create distributions.")
