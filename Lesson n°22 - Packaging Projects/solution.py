"""Lesson 22 - Packaging Projects (Solution)

Reference scaffolding for the Publishable Study Helper.
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).parent / "study_helper"
PACKAGE = ROOT / "study_helper"


def scaffold_package() -> None:
    PACKAGE.mkdir(parents=True, exist_ok=True)
    (PACKAGE / "__init__.py").write_text("__all__ = ['cli']\n__version__ = '0.1.0'\n", encoding="utf-8")
    (PACKAGE / "cli.py").write_text(
        """def main():\n    print('Study hard, share knowledge!')\n""",
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text("# Study Helper\n\nMotivational CLI.", encoding="utf-8")
    (ROOT / "LICENSE").write_text("MIT License", encoding="utf-8")

    pyproject = ROOT / "pyproject.toml"
    pyproject.write_text(
        """
        [build-system]
        requires = ["setuptools>=68", "wheel"]
        build-backend = "setuptools.build_meta"

        [project]
        name = "study-helper"
        version = "0.1.0"
        description = "CLI assistant for study sessions"
        readme = "README.md"
        license = {text = "MIT"}
        requires-python = ">=3.10"
        dependencies = ["click"]

        [project.scripts]
        study-helper = "study_helper.cli:main"
        """.strip(),
        encoding="utf-8",
    )

def build_artifacts() -> None:
    subprocess.run(["python", "-m", "build"], cwd=ROOT, check=True)


def main() -> None:
    scaffold_package()
    print("Package scaffolded at", ROOT)
    print("Run: python -m build")
    print("Upload with: python -m twine upload --repository testpypi dist/*")


if __name__ == "__main__":
    main()
