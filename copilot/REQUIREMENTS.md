# Zodiac Calculator — Requirements

Project: Zodiac Calculator
Purpose: Simple CLI program that accepts a birthdate and returns the corresponding zodiac signs for both Western and Eastern systems.

Core requirements
- Interface: Command-line (argparse). Single executable entrypoint: cli.py
- Input format: M/D/YYYY (e.g., 3/21/1990). Strict validation with clear user feedback on parse errors.
- Zodiac systems: Always return both Western (tropical) and Eastern (Chinese) signs for the provided birthdate.
- Year handling: Use the provided year for leap-day handling and any year-dependent rules.
- Cusp behavior: Return a single sign per system (no ambiguous dual-sign output).
- Output: Plain-text printed to terminal, include emoji for each sign and a short explanation (e.g., "♈ Aries — Mar 21–Apr 19: The Ram"). Show Western then Eastern.
- Error handling: Friendly human-readable messages; program exits with non-zero status on fatal errors.

Testing & quality
- Tests: pytest-based test suite in tests/ covering parsing, Western logic (including leap years and edge dates), and Eastern mapping.
- Coverage: Aim for 100% coverage (small codebase). Include edge and invalid-input tests.
- CI: Not required now. Local venv + pytest sufficient.

Environment & layout
- Python: 3.13 target
- Virtual environment: use python -m venv venv; do not commit venv/ to repo
- Source layout: modules at repo root: cli.py, parsers.py, western.py, eastern.py, utils.py
- Tests: tests/*.py
- Dependencies: prefer stdlib; explicitly list pytest in requirements.txt for dev testing

Files to include (scaffold)
- README.md: usage examples and venv instructions
- REQUIREMENTS.md (this file)
- .gitignore: exclude venv/, __pycache__/, .pytest_cache/

Notes
- Keep dependencies minimal; add third-party libs only if justified.
- Update this file if behavior changes (e.g., cusp policy, additional output formats).