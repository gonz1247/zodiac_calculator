# Copilot instructions

Project: [Zodiac Calculator]
Purpose: Simple calculator for determining zodiac signs based on birthdate.

## High-level goals

- Create python program that accepts a birthdate and returns the corresponding zodiac sign.
- Create codebase that is clean, maintainable, and well-tested.

## Voice and behavior

- Tone: concise, professional
- When unsure: ask for clarification before changing public APIs or architecture

## Python environment

- Python: 3.13
- Virtualenv: venv/
- Create a requirements.txt for dependencies; use pip freeze > requirements.txt to update

## Coding conventions

- Line length: 100
- Formatter: black --check
- Linter: ruff --fix
- Type hints: numpy style
- Docstrings: numpy style

## Testing

- Framework: pytest
- Tests location: tests/
- Coverage target: 100% (simple codebase so aim for full coverage)
- Unit tests required for public functions; include edge cases and parametrized inputs

## Security & secrets

- Never add secrets to the repo
- Use environment variables and provide a .env.example
- Mock network calls in tests; avoid external network access in CI


