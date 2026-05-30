# Zodiac Calculator — Requirements

Project: Zodiac Calculator
Purpose: Simple CLI program that accepts a birthdate and returns the corresponding zodiac signs for both Western and Eastern systems.

Core requirements
- Interface: command-line. Entrypoint: python zodiac_calculator.py
- Input format: M/D/YYYY (e.g., 3/21/1990). Strict validation with clear user feedback on parse errors.
- Zodiac systems: always return both Western and Eastern signs for the provided birthdate.
- Year handling: use the provided year for leap-day handling and any year-dependent rules.
- Cusp behavior: return a single sign per system (no dual-sign output).
- Output: plain-text printed to terminal; include emoji and a short explanation for each sign (Western then Eastern).
- Error handling: friendly human-readable messages; program exits with non-zero status on fatal errors.

Testing & quality
- Tests: pytest-based test suite located in tests/ covering parsing, Western logic (including leap years and edge dates), and Eastern mapping.
- Coverage: target 100% for this small codebase.
- CI: optional; local venv + pytest is sufficient for development.

Environment & layout
- Python: 3.13 target
- Development venv: recommend python -m venv venv (do not commit venv/)
- Source layout: root modules: zodiac_calculator.py, parsers.py, western.py, eastern.py
- Tests: tests/*.py
- Dependencies: prefer stdlib; list pytest in requirements.txt for development testing

Files to include
- README.md (usage and casual-user note)
- REQUIREMENTS.md (this file)
- .gitignore (exclude venv/, __pycache__/, .pytest_cache/)
