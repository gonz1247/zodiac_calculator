# Zodiac Calculator — Requirements

This document is the **source of truth** for behavior, module layout, and acceptance criteria for the Cursor implementation of the Zodiac Calculator.

## 1. Overview

Interactive CLI that accepts a birthdate in `M/D/YYYY` format and reports:

- Western (tropical) zodiac sign
- Eastern (Chinese, Chinese-New-Year-aware) zodiac animal
- A short static horoscope blurb for each
- Optional pairwise compatibility between two birthdates

The user can look up multiple birthdates in a loop until they choose to quit.

## 2. In scope (v1)

| Feature | Behavior |
|---------|----------|
| Western sign | Tropical sign from month/day; returned as `WesternSign` |
| Eastern sign | CNY-aware animal from full birthdate; returned as `EasternAnimal` |
| Horoscope text | Static blurb on each enum member; accessed via `.horoscope` |
| Compatibility | Compare two birthdates; returns `CompatibilityLevel` for Western and Eastern separately |
| CLI loop | Repeated lookups with optional compatibility sub-flow |
| Enumerations | Central enum types hold display names, metadata, and horoscope blurbs |

## 3. Out of scope (v1)

- Time of birth / rising signs
- Lunar calendar conversion UI (displaying lunar month/day)
- Localization beyond English sign names
- Network or external API calls at runtime
- Web UI
- Persistence (save/load birthdates)
- Daily or date-specific horoscopes (only static sign-level personality blurbs)
- Displaying trine or element names in CLI output

## 4. Module layout

| File | Responsibility |
|------|----------------|
| `zodiac_calculator.py` | CLI entry point (`python zodiac_calculator.py`) |
| `zodiac/__init__.py` | Re-exports public API and enum types |
| `zodiac/enums.py` | All enum types, metadata, and horoscope blurbs |
| `zodiac/western.py` | Western sign from month/day → `WesternSign` |
| `zodiac/eastern.py` | Eastern sign from birthdate + CNY rules → `EasternAnimal` |
| `zodiac/cny_dates.py` | Static Chinese New Year date lookup (stdlib-only) |
| `zodiac/compatibility.py` | Element/trine/clash rules → `CompatibilityLevel` |
| `zodiac/parsing.py` | Parse and validate `M/D/YYYY` input strings |
| `tests/test_enums.py` | Enum metadata completeness |
| `tests/test_western.py` | Western sign behavior and boundaries |
| `tests/test_eastern.py` | CNY-aware Eastern sign behavior |
| `tests/test_compatibility.py` | Known compatible/incompatible pairs |
| `tests/test_parsing.py` | Date string parsing edge cases |
| `tests/test_cli.py` | Interactive loop (via `subprocess` or `capsys`) |
| `requirements.txt` | Dev dependencies only (`pytest`, `pytest-cov`, `black`, `ruff`) |

Horoscope blurbs live on enum members in `enums.py`. There is no separate `horoscopes.py` module.

## 5. Enumeration model

Use stdlib `enum.StrEnum` for user-facing types and plain `enum.Enum` for internal-only types.

### 5.1 `WesternSign` (`StrEnum`)

Members: `ARIES`, `TAURUS`, `GEMINI`, `CANCER`, `LEO`, `VIRGO`, `LIBRA`, `SCORPIO`, `SAGITTARIUS`, `CAPRICORN`, `AQUARIUS`, `PISCES`

Display names (enum values): `Aries`, `Taurus`, `Gemini`, `Cancer`, `Leo`, `Virgo`, `Libra`, `Scorpio`, `Sagittarius`, `Capricorn`, `Aquarius`, `Pisces`

Properties on each member:

- `.element` → `WesternElement`
- `.horoscope` → `str` (1–3 sentences)

Element mapping:

| Element | Signs |
|---------|-------|
| `FIRE` | Aries, Leo, Sagittarius |
| `EARTH` | Taurus, Virgo, Capricorn |
| `AIR` | Gemini, Libra, Aquarius |
| `WATER` | Cancer, Scorpio, Pisces |

### 5.2 `EasternAnimal` (`StrEnum`)

Members: `RAT`, `OX`, `TIGER`, `RABBIT`, `DRAGON`, `SNAKE`, `HORSE`, `GOAT`, `MONKEY`, `ROOSTER`, `DOG`, `PIG`

Display names (enum values): `Rat`, `Ox`, `Tiger`, `Rabbit`, `Dragon`, `Snake`, `Horse`, `Goat`, `Monkey`, `Rooster`, `Dog`, `Pig`

Properties on each member:

- `.trine` → `EasternTrine`
- `.horoscope` → `str` (1–3 sentences)
- `.clash_partner` → `EasternAnimal` (animal 6 positions away on the 12-cycle)

Clash pairs:

| Animal | Clash partner |
|--------|---------------|
| Rat | Horse |
| Ox | Goat |
| Tiger | Monkey |
| Rabbit | Rooster |
| Dragon | Dog |
| Snake | Pig |
| Horse | Rat |
| Goat | Ox |
| Monkey | Tiger |
| Rooster | Rabbit |
| Dog | Dragon |
| Pig | Snake |

### 5.3 `WesternElement` (`Enum`)

Members: `FIRE`, `EARTH`, `AIR`, `WATER`

Internal only — used for Western compatibility logic; not printed in CLI output.

### 5.4 `EasternTrine` (`Enum`)

Members: `FIRST`, `SECOND`, `THIRD`, `FOURTH`

Internal only — not shown in CLI output; used for Eastern compatibility via `EasternAnimal.trine`.

| Member | Animals |
|--------|---------|
| `FIRST` | Rat, Dragon, Monkey |
| `SECOND` | Ox, Snake, Rooster |
| `THIRD` | Tiger, Horse, Dog |
| `FOURTH` | Rabbit, Goat, Pig |

### 5.5 `CompatibilityLevel` (`StrEnum`)

Members: `COMPATIBLE`, `NEUTRAL`, `CHALLENGING`

Display names (enum values): `Compatible`, `Neutral`, `Challenging`

### 5.6 Design rules

- Core functions accept and return enums, not free-form strings.
- Only `parsing.py` and the CLI handle raw strings; all other logic uses enums.
- `StrEnum` for user-facing values; plain `Enum` for internal metadata.
- CLI output uses `sign.value` or `str(sign)` for `StrEnum` display names.
- Sign names, animal names, elements, and trines are defined once in `enums.py`.

## 6. Public API

Agents must not change these signatures without explicit approval.

```python
# zodiac/enums.py — re-exported from zodiac/__init__.py
class WesternSign(StrEnum): ...
class EasternAnimal(StrEnum): ...
class WesternElement(Enum): ...
class EasternTrine(Enum): ...
class CompatibilityLevel(StrEnum): ...

# zodiac/parsing.py
def parse_birthdate(date_str: str) -> tuple[int, int, int]: ...  # (year, month, day)

# zodiac/western.py
def western_sign(month: int, day: int) -> WesternSign: ...

# zodiac/eastern.py
def eastern_sign(year: int, month: int, day: int) -> EasternAnimal: ...

# zodiac/cny_dates.py
def chinese_new_year_date(year: int) -> tuple[int, int, int]: ...  # (year, month, day)

# zodiac/compatibility.py
def western_compatibility(sign_a: WesternSign, sign_b: WesternSign) -> CompatibilityLevel: ...
def eastern_compatibility(animal_a: EasternAnimal, animal_b: EasternAnimal) -> CompatibilityLevel: ...
```

Horoscope text is accessed via `.horoscope` on enum members, not via separate lookup functions.

### Error behavior

| Function | Raises `ValueError` when |
|----------|--------------------------|
| `parse_birthdate` | Wrong format, non-4-digit year, or impossible calendar date |
| `western_sign` | Invalid month/day (e.g. month 13, Feb 30) |
| `eastern_sign` | Invalid calendar date |
| `chinese_new_year_date` | Year outside supported lookup range (1900–2100) |

Compatibility functions assume valid enum inputs from `western_sign` / `eastern_sign`.

## 7. Date input parsing

Format: **`M/D/YYYY`**

- Month and day: 1–2 digits; leading zeros optional (`1/5/1990` and `01/05/1990` both valid).
- Year: exactly 4 digits (`3/21/90` is invalid).
- Separator: `/` only (not `-` or `.`).
- Strip surrounding whitespace before parsing.
- Validate with stdlib `datetime` after parsing.

Examples:

| Input | Result |
|-------|--------|
| `3/21/1990` | Valid → `(1990, 3, 21)` |
| `03/21/1990` | Valid → `(1990, 3, 21)` |
| `12/1/2000` | Valid → `(2000, 12, 1)` |
| `3/21/90` | Invalid (2-digit year) |
| `1990-03-21` | Invalid (wrong format) |
| `3-21-1990` | Invalid (wrong separator) |
| `2/30/1990` | Invalid (impossible date) |

## 8. Western zodiac rules

Tropical zodiac from month and day only (birth year is ignored).

Each sign spans an inclusive start date through an inclusive end date. The day after an end date belongs to the next sign.

| Sign | Start | End |
|------|-------|-----|
| Capricorn | Jan 1 | Jan 19 |
| Aquarius | Jan 20 | Feb 18 |
| Pisces | Feb 19 | Mar 20 |
| Aries | Mar 21 | Apr 19 |
| Taurus | Apr 20 | May 20 |
| Gemini | May 21 | Jun 20 |
| Cancer | Jun 21 | Jul 22 |
| Leo | Jul 23 | Aug 22 |
| Virgo | Aug 23 | Sep 22 |
| Libra | Sep 23 | Oct 22 |
| Scorpio | Oct 23 | Nov 21 |
| Sagittarius | Nov 22 | Dec 21 |
| Capricorn | Dec 22 | Dec 31 |

`western_sign(month, day)` returns the matching `WesternSign` member.

### Acceptance examples

| Birthdate | Expected |
|-----------|----------|
| `3/20/1990` | `WesternSign.PISCES` |
| `3/21/1990` | `WesternSign.ARIES` |
| `1/19/1990` | `WesternSign.CAPRICORN` |
| `1/20/1990` | `WesternSign.AQUARIUS` |
| `12/22/1990` | `WesternSign.CAPRICORN` |

## 9. Eastern zodiac rules (CNY-aware)

### Algorithm

1. Look up the Gregorian date of Chinese New Year for the birth year via `chinese_new_year_date(birth_year)`.
2. If the birthdate is **before** CNY → use the animal for `birth_year - 1`.
3. If the birthdate is **on or after** CNY → use the animal for `birth_year`.
4. Map the zodiac year to an animal using reference year 1900 = Rat: index = `(year - 1900) % 12`.

| Index | Animal |
|-------|--------|
| 0 | Rat |
| 1 | Ox |
| 2 | Tiger |
| 3 | Rabbit |
| 4 | Dragon |
| 5 | Snake |
| 6 | Horse |
| 7 | Goat |
| 8 | Monkey |
| 9 | Rooster |
| 10 | Dog |
| 11 | Pig |

Return the matching `EasternAnimal` member.

### Chinese New Year data

- Static lookup table in `cny_dates.py` for years **1900–2100** (inclusive).
- Dates are precomputed and stored at implementation time; not calculated at runtime.
- Cite the calendar source in a code comment during implementation.
- No third-party calendar libraries at runtime.

### Acceptance examples

1990 Chinese New Year: **January 27, 1990**.

| Birthdate | Zodiac year used | Expected |
|-----------|------------------|----------|
| `1/26/1990` | 1989 | `EasternAnimal.SNAKE` |
| `1/27/1990` | 1990 | `EasternAnimal.HORSE` |
| `12/31/1990` | 1990 | `EasternAnimal.HORSE` |

## 10. Horoscope text

- One static personality blurb (1–3 sentences) per `WesternSign` and `EasternAnimal`, stored as the `.horoscope` property on each enum member.
- Sign-level only — not daily or personalized beyond the sign/animal.
- English only for v1.
- Every enum member must have a non-empty `.horoscope`.

### CLI output format

```
Western sign: Aries
  Aries are bold, energetic, and natural leaders.
Eastern sign: Horse
  Horses are free-spirited, witty, and thrive on independence.
```

The indented line is the `.horoscope` value for that sign/animal.

## 11. Sign compatibility

### Western compatibility

Uses `WesternSign.element`:

| Condition | Result |
|-----------|--------|
| Same element | `CompatibilityLevel.COMPATIBLE` |
| Fire + Air, or Earth + Water | `CompatibilityLevel.COMPATIBLE` |
| Fire + Water, Air + Earth, or Fire + Earth | `CompatibilityLevel.CHALLENGING` |
| All other pairings | `CompatibilityLevel.NEUTRAL` |

Evaluate in order: same element first, then challenging pairs, then compatible cross-elements, else neutral.

### Eastern compatibility

Uses `EasternAnimal.trine` and `.clash_partner`:

| Condition | Result |
|-----------|--------|
| Same trine (`animal_a.trine is animal_b.trine`) | `CompatibilityLevel.COMPATIBLE` |
| Clash (`animal_b is animal_a.clash_partner`) | `CompatibilityLevel.CHALLENGING` |
| All other pairings | `CompatibilityLevel.NEUTRAL` |

Evaluate in order: same trine first, then clash, else neutral.

### Acceptance examples

| Pair | Expected | Reason |
|------|----------|--------|
| `WesternSign.ARIES` + `WesternSign.LEO` | `COMPATIBLE` | Both Fire |
| `WesternSign.ARIES` + `WesternSign.CANCER` | `CHALLENGING` | Fire + Water |
| `WesternSign.GEMINI` + `WesternSign.LIBRA` | `COMPATIBLE` | Air + Air |
| `EasternAnimal.RAT` + `EasternAnimal.DRAGON` | `COMPATIBLE` | Same trine (`FIRST`) |
| `EasternAnimal.RAT` + `EasternAnimal.HORSE` | `CHALLENGING` | Clash partners |
| `EasternAnimal.RAT` + `EasternAnimal.OX` | `NEUTRAL` | Different trine, not a clash |

### CLI compatibility sub-flow

After a successful birthdate lookup:

1. Prompt: `Check compatibility with another birthdate? (y/n): `
2. If yes (`y` or `yes`, case-insensitive): prompt `Enter birthdate (M/D/YYYY): ` for the second date.
3. On valid second date, print both pairs' signs and compatibility on one line per system:
   ```
   Western (Aries + Leo): Compatible
   Eastern (Horse + Horse): Compatible
   ```
4. On invalid second date: print an error and re-prompt for that date only (do not restart the full loop).

## 12. CLI behavior

### Flow

1. Print a short welcome banner.
2. Loop until the user chooses to quit:
   - Prompt: `Enter birthdate (M/D/YYYY): `
   - On valid input: print Western sign + horoscope, then Eastern sign + horoscope.
   - On invalid input: print a clear error message and re-prompt (do not exit).
   - Prompt: `Check compatibility with another birthdate? (y/n): ` — run compatibility sub-flow if yes.
   - Prompt: `Calculate another? (y/n): ` — continue on `y`/`yes` (case-insensitive); exit on anything else.
3. Print a brief exit message on quit.

### Error handling

| Case | Behavior |
|------|----------|
| Wrong format (`1990-03-21`, `3-21-1990`) | Error message; re-prompt |
| 2-digit year (`3/21/90`) | Error message; re-prompt |
| Impossible date (`2/30/1990`) | Error message; re-prompt |
| Birth year outside CNY table (1900–2100) | Error message explaining supported range |
| EOF / Ctrl+C | Exit gracefully without traceback |

## 13. Non-functional requirements

- Python **3.13**
- Stdlib-only runtime dependencies
- Type hints on all public functions
- NumPy-style docstrings on public modules and functions
- Format with Black (100-column line length)
- Lint with Ruff
- **100% branch coverage** on public behavior via pytest

## 14. Definition of done

- All acceptance examples in this document pass as pytest cases
- `pytest --cov=. --cov-branch --cov-report=term-missing` passes at 100% coverage
- `python zodiac_calculator.py` runs the interactive loop
- No secrets or virtualenv artifacts committed
