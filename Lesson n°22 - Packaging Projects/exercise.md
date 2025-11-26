# Exercise: Publishable Study Helper

Prepare a minimal package ready for upload to PyPI/TestPyPI.

## Requirements

1. Create a folder `study_helper/` with:
   - `study_helper/__init__.py`
   - `study_helper/cli.py` exposing a `main()` function that prints a motivational quote.
2. Add a `pyproject.toml` using setuptools with metadata: name, version, description, license, authors, dependencies (at least `click`).
3. Configure console entry points so `study-helper` runs `study_helper.cli:main`.
4. Include a README and LICENSE file in the package directory.
5. Run `python -m build` to produce wheel + sdist (document command in comments).
6. Provide instructions for uploading to TestPyPI using `python -m twine upload --repository testpypi dist/*`.

## Stretch Ideas

- Add package data (e.g., templates) and include them via `package_data`.
- Use `setuptools_scm` for automatic versioning.
- Add a `requirements-dev.txt` listing build tools.

## Tips

- Keep package names lowercase with underscores.
- Ensure `__init__.py` sets `__all__` and optionally `__version__`.
- Use `python -m venv` before building to avoid polluting global installs.
