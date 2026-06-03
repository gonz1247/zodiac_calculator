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
├── README.md
├── requirements.txt
├── .gitignore
├── main.py              # CLI entry point and display logic
├── zodiac/
│   ├── __init__.py
│   ├── western.py       # WesternSign, WesternElement enums + logic
│   └── chinese.py       # ChineseAnimal, ChineseElement, Polarity enums + logic
└── tests/
    ├── __init__.py
    ├── test_western.py
    ├── test_chinese.py
    └── test_main.py
```

## Architecture

### Enum-first design
All signs, elements, and polarities are Python `Enum`s. Descriptions and compatibility data are stored as `dict[<EnumType>, str]`, keyed by enum values. No raw string matching occurs anywhere in the logic — this eliminates typo bugs and makes invalid states unrepresentable.

```
WesternSign, WesternElement          — zodiac/western.py
ChineseAnimal, ChineseElement, Polarity — zodiac/chinese.py
```

### Western zodiac (`zodiac/western.py`)
- Sign lookup uses a `_SIGN_CUTOFFS` list of `(sign, end_month, end_day)` tuples ordered Jan→Dec. A date belongs to the first entry whose end date ≥ the input date; Capricorn (Dec 22+) is the default fallback.
- Compatibility is element-based: same element → highly compatible; Fire+Air or Earth+Water → complementary; all other combos → neutral/challenging.

### Chinese zodiac (`zodiac/chinese.py`)
- **`CYCLE_ANCHOR = 4`** — a named constant that anchors the modular arithmetic to 1900 (a verified Yang Metal Rat year): `(1900 - 4) % 12 == 0` (Rat), `(1900 - 4) % 10 == 6 → // 2 == 3` (Metal), `(1900 - 4) % 2 == 0` (Yang).
- **CNY date table** (`_CNY_DATES`) — a hardcoded `dict[int, tuple[int, int]]` covering 1900–2050. If a birthday falls before Chinese New Year in its calendar year, the prior year's sign is used. Years outside the table fall back to using the calendar year directly.
- **Compatibility** uses `CHINESE_TRINES` (trine group 1–4 per animal) and `CHINESE_OPPOSITES` (6 conflicting pairs as `frozenset`s). Priority: same animal → same trine → opposite pair → neutral.

### App loop (`main.py`)
```
[Welcome]
loop:
  ──────────────────────── (separator — marks a new lookup clearly)
  inner loop: prompt for birthdate until valid or 'q'
  → display Western sign + full paragraph description
  → display Chinese sign (Polarity Element Animal) + full paragraph description
  → optional: inner loop for second birthdate → Western + Chinese compatibility
```
Invalid-date re-prompts and the compatibility sub-prompt stay tight inside their own inner loops so the separator only fires at the start of a genuinely new lookup.

## Commands
```bash
# Format
black main.py zodiac/ tests/

# Lint
ruff check main.py zodiac/ tests/

# Test with coverage
pytest --cov=zodiac --cov=main --cov-branch --cov-report=term-missing
```
