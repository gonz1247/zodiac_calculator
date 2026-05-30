# Zodiac Calculator

Simple CLI that accepts a birthdate (M/D/YYYY) and prints the Western and Eastern zodiac signs with emoji and a short description.

Quick usage (casual user — no venv required):

    python zodiac_calculator.py 3/21/1990

This prints both Western and Eastern zodiac signs with emoji and a short explanation.

Developer setup (optional):

1. Create and activate a virtual environment (recommended for development):

    python -m venv venv
    venv\Scripts\activate

2. Install dev dependencies:

    pip install -r requirements.txt

3. Run tests:

    pytest

Notes:
- The CLI file is `zodiac_calculator.py`.
- If you see encoding issues on Windows consoles, the program replaces unsupported characters so output remains readable.
- Do not commit the `venv/` directory; it's ignored by .gitignore.
