# Zodiac Calculator — Cursor Implementation

Interactive CLI that reports Western (tropical) and Eastern (Chinese, Chinese-New-Year-aware) zodiac signs from a birthdate, with personality blurbs and optional compatibility between two dates.

## Features

- **Western sign** — tropical zodiac from month and day
- **Eastern sign** — zodiac animal with Chinese New Year boundary handling
- **Horoscope text** — short static personality blurb for each sign and animal
- **Compatibility check** — optional comparison of two birthdates (Western elements and Eastern trines/clashes)
- **Interactive loop** — look up multiple birthdates until you choose to quit

## Setup

```bash
cd cursor
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

## Run

```bash
python zodiac_calculator.py
```

### Input format

- Dates use **`M/D/YYYY`** (e.g. `3/21/1990`, `01/05/1990`)
- Month and day may be 1 or 2 digits; year must be 4 digits
- Supported birth years for Eastern signs: **1900–2100**
- Invalid dates show an error and re-prompt — the program does not exit

### Example session

```
Welcome to the Zodiac Calculator!
Enter birthdate (M/D/YYYY): 3/21/1990
Western sign: Aries
  Aries are bold, energetic, and natural leaders who thrive on challenge.
Eastern sign: Horse
  Horses are free-spirited, witty, and thrive on independence.
Check compatibility with another birthdate? (y/n): y
Enter birthdate (M/D/YYYY): 7/23/1990
Western (Aries + Leo): Compatible
Eastern (Horse + Horse): Compatible
Calculate another? (y/n): n
Goodbye!
```

### Interaction flow

1. Enter a birthdate → see Western sign, Eastern sign, and a horoscope blurb for each
2. Optionally check compatibility with a second birthdate (sign pairs and rating on one line per system)
3. Choose whether to look up another birthdate or quit

Answer **`y`** or **`yes`** (case-insensitive) to continue at yes/no prompts; anything else exits at "Calculate another?".

Press **Ctrl+C** or send EOF to exit gracefully.

## Test

```bash
pytest --cov=. --cov-branch --cov-report=term-missing
```

## Requirements

Full behavioral spec, public API, and acceptance criteria: [REQUIREMENTS.md](REQUIREMENTS.md)

## Cursor project rules

Project rules live in `.cursor/rules/`. For them to apply automatically, **open this `cursor/` folder as your Cursor workspace** (File → Open Folder → select `cursor/`).

Rules cover:

- Project scope and module layout (`project-scope.mdc`)
- Python style and structure (`python-standards.mdc`)
- pytest conventions (`testing.mdc`)
- Agent implementation workflow (`agent-workflow.mdc`)
