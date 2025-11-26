"""Lesson 21 - Virtual Environments

Goal: manage project dependencies cleanly with venv, pip, and requirements files.
"""

import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
VENV_DIR = PROJECT_DIR / "venv"


def run(command: list[str]) -> None:
    print("$", " ".join(command))
    subprocess.run(command, check=True)

def create_venv() -> None:
    if VENV_DIR.exists():
        print("Virtual environment already exists.")
        return
    run(["python", "-m", "venv", str(VENV_DIR)])

def install_requirements(requirements: list[str]) -> None:
    pip = VENV_DIR / "Scripts" / "pip" if Path("/dev/null").exists() else VENV_DIR / "Scripts" / "pip.exe"
    command = [str(pip), "install"] + requirements
    run(command)

def freeze_requirements() -> None:
    pip = VENV_DIR / "Scripts" / "pip.exe"
    with open(PROJECT_DIR / "requirements.txt", "w", encoding="utf-8") as file:
        subprocess.run([str(pip), "freeze"], check=True, stdout=file)

if __name__ == "__main__":
    create_venv()
    install_requirements(["requests", "rich"])
    freeze_requirements()
    print("Virtual environment ready. Activate and run your scripts!")
