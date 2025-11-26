"""Lesson 21 - Virtual Environments (Solution)

Environment bootstrapper implementation.
"""

import argparse
import subprocess
import sys
from pathlib import Path
from textwrap import dedent

PROJECT_DIR = Path(__file__).parent
VENV_DIR = PROJECT_DIR / ".venv"
REQUIREMENTS = PROJECT_DIR / "requirements.txt"
ACTIVATE_INSTRUCTIONS = PROJECT_DIR / "activate.txt"

def run(command: list[str]) -> None:
    print("$", " ".join(command))
    subprocess.run(command, check=True)

def ensure_requirements_file() -> None:
    if not REQUIREMENTS.exists():
        REQUIREMENTS.write_text("requests\nrich\n", encoding="utf-8")

def write_instructions() -> None:
    instructions = dedent(
        f"""
        Activate your environment:
        - Windows: {VENV_DIR}\\Scripts\\activate
        - macOS/Linux: source {VENV_DIR}/bin/activate
        """
    ).strip()
    ACTIVATE_INSTRUCTIONS.write_text(instructions, encoding="utf-8")

def create_venv(python_executable: str) -> None:
    if VENV_DIR.exists():
        print("Virtual environment already exists.")
        return
    run([python_executable, "-m", "venv", str(VENV_DIR)])

def install_dependencies(upgrade: bool) -> None:
    pip_executable = VENV_DIR / "Scripts" / "pip"
    command = [str(pip_executable), "install", "-r", str(REQUIREMENTS)]
    if upgrade:
        command.insert(2, "--upgrade")
    run(command)

def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap a Python environment")
    parser.add_argument("--python", default=sys.executable, help="Python executable to use")
    parser.add_argument("--upgrade", action="store_true", help="Reinstall dependencies")
    return parser.parse_args(argv)

def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        ensure_requirements_file()
        create_venv(args.python)
        install_dependencies(args.upgrade)
        write_instructions()
    except subprocess.CalledProcessError as exc:
        print("Command failed:", exc)
        return 1
    except FileNotFoundError as exc:
        print("File error:", exc)
        return 1
    print("Environment ready. See activate.txt for next steps.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
