# Zodiac Calculator

## Project
Python CLI that calculates Western and Chinese zodiac signs from a birthdate.

## Stack
- **Language:** Python 3.13
- **Testing:** pytest, targeting 100% line and branch coverage
- **Formatting:** Black
- **Linting:** Ruff

## Standards
- Every function must have corresponding pytest tests.
- Coverage must remain at 100% lines and branches — no gaps.
- All code must pass `black --check` and `ruff check` before committing.
- No external dependencies beyond what's in `requirements.txt`.
- Keep functions small and pure — prefer returning values over side effects.

## Project Structure
```
claude/
├── CLAUDE.md
├── requirements.txt
├── main.py              # CLI entry point
├── zodiac/
│   ├── __init__.py
│   ├── western.py
│   └── chinese.py
└── tests/
    ├── __init__.py
    ├── test_western.py
    ├── test_chinese.py
    └── test_main.py
```

## Commands
```bash
# Format
black main.py zodiac/ tests/

# Lint
ruff check main.py zodiac/ tests/

# Test with coverage
pytest --cov=zodiac --cov=main --cov-branch --cov-report=term-missing
```
