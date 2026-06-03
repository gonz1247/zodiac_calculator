# Zodiac Calculator

A Python CLI that calculates your Western and Chinese zodiac signs from a birthdate, with full paragraph descriptions and optional compatibility checking between two people.

---

## User Guide

### Running the app

```bash
python main.py
```

The app runs as an interactive loop. Enter a birthdate when prompted and it will display your signs. Type `q` at any birthdate prompt to quit.

### Accepted date formats

| Format | Example |
|---|---|
| `YYYY-MM-DD` | `1990-05-15` or `1990-5-15` |
| `MM/DD/YYYY` | `05/15/1990` or `5/15/1990` |

Leading zeros are optional for month and day in both formats.

### What you'll see

For each birthdate the app shows:

**Western zodiac** — your sun sign (Aries through Pisces) with a full paragraph description of the sign's personality and traits.

**Chinese zodiac** — your full traditional label combining polarity, element, and animal (e.g. *Yang Wood Dragon*) with a full paragraph description of the animal sign.

### Compatibility check

After your signs are displayed, you'll be asked:

```
Check compatibility with another person? (y/n):
```

Enter `y` to provide a second birthdate. The app will show:
- The second person's Western sign and Chinese sign label (no full description — just the label so you know what you're comparing against)
- A Western compatibility summary based on elemental groupings
- A Chinese compatibility summary based on trine groupings

Enter `n` to skip and go straight to the next lookup.

### Example session

```
=== Zodiac Calculator ===
Discover your Western and Chinese zodiac signs.

────────────────────────────────────────────
Enter a birthdate (YYYY-MM-DD or MM/DD/YYYY), or 'q' to quit: 1990-5-15

--- Western Zodiac: Taurus ---
Taurus is an earth sign ruled by Venus...

--- Chinese Zodiac: Yang Metal Horse ---
The Horse is spirited, energetic, and free...

Check compatibility with another person? (y/n): y
Enter their birthdate (YYYY-MM-DD or MM/DD/YYYY): 1988-2-17

--- Western Compatibility (comparing with: Aquarius) ---
Taurus (Earth) and Aquarius (Air) come from elements...

--- Chinese Compatibility (comparing with: Yang Earth Dragon) ---
The Horse and the Dragon belong to different trines...

────────────────────────────────────────────
Enter a birthdate (YYYY-MM-DD or MM/DD/YYYY), or 'q' to quit: q
Goodbye!
```

---

## Developer Guide

### Setup

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Running tests

```bash
pytest --cov=zodiac --cov=main --cov-branch --cov-report=term-missing
```

The suite targets **100% line and branch coverage**. All 98 tests should pass.

### Formatting and linting

```bash
# Auto-format
black main.py zodiac/ tests/

# Lint
ruff check main.py zodiac/ tests/

# Check format without modifying (used in CI)
black --check main.py zodiac/ tests/
```

All code must pass both `black --check` and `ruff check` before committing.

### Project structure

```
claude/
├── main.py              # CLI entry point, display functions, interactive loop
├── zodiac/
│   ├── western.py       # WesternSign + WesternElement enums, sign lookup, compatibility
│   └── chinese.py       # ChineseAnimal, ChineseElement, Polarity enums, CNY table, compatibility
└── tests/
    ├── test_western.py  # Sign boundary tests, element mapping, compatibility tiers
    ├── test_chinese.py  # Animal/element/polarity checks, CNY boundary, compatibility
    └── test_main.py     # parse_date, display functions, mocked run_loop sequences
```

### Key design decisions

- **Enum-first** — every sign, element, and polarity is an `Enum`. Descriptions and compatibility data are `dict[EnumType, str]`. No raw string matching in logic.
- **`CYCLE_ANCHOR = 4`** — anchors Chinese zodiac modular arithmetic to 1900 (Yang Metal Rat). See `zodiac/chinese.py` for the derivation.
- **CNY table** — hardcoded Gregorian dates for Chinese New Year (1900–2050) handle the Jan/Feb boundary correctly. Years outside the table fall back to the calendar year.
- **Inner validation loops** — invalid-date re-prompts stay tight inside their own `while` loops so the visual separator only fires at the start of a genuinely new lookup.
