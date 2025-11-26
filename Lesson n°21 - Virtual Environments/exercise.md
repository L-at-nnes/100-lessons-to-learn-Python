# Exercise: Environment Bootstrapper

Automate the setup of a virtual environment for newcomers.

## Requirements

1. Write a script `bootstrap_env.py` that:
   - Creates a virtual environment (using `venv`) inside a `.venv` folder if it doesn’t exist.
   - Installs packages listed in `requirements.txt` (create a sample file with 2 packages).
   - Writes a short `activate.txt` file with instructions for activating the environment.
2. Provide command-line options:
   - `--python` to specify the Python executable path.
   - `--upgrade` flag to reinstall dependencies even if they’re already present.
3. Print clear status messages so beginners understand each step.
4. Handle errors (missing Python executable, pip failures) and exit with a non-zero status code when something goes wrong.
5. Include module-level docstrings explaining why virtual environments are important.

## Stretch Ideas

- Add a `--packages` option to install extra dependencies.
- Detect the operating system and print OS-specific activation instructions.
- Generate a `.env` file with placeholder environment variables.

## Tips

- Use `subprocess.run(..., check=True)` to ensure failures raise `CalledProcessError`.
- Store path references with `pathlib.Path` for clarity.
- Use `textwrap.dedent` to keep multi-line instructions readable.
