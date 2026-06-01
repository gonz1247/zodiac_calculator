"""Western tropical zodiac sign lookup."""

from __future__ import annotations

from datetime import datetime

from zodiac.enums import WesternSign

# Each entry: (start_month, start_day, end_month, end_day, sign)
_SIGN_RANGES: tuple[tuple[int, int, int, int, WesternSign], ...] = (
    (1, 1, 1, 19, WesternSign.CAPRICORN),
    (1, 20, 2, 18, WesternSign.AQUARIUS),
    (2, 19, 3, 20, WesternSign.PISCES),
    (3, 21, 4, 19, WesternSign.ARIES),
    (4, 20, 5, 20, WesternSign.TAURUS),
    (5, 21, 6, 20, WesternSign.GEMINI),
    (6, 21, 7, 22, WesternSign.CANCER),
    (7, 23, 8, 22, WesternSign.LEO),
    (8, 23, 9, 22, WesternSign.VIRGO),
    (9, 23, 10, 22, WesternSign.LIBRA),
    (10, 23, 11, 21, WesternSign.SCORPIO),
    (11, 22, 12, 21, WesternSign.SAGITTARIUS),
    (12, 22, 12, 31, WesternSign.CAPRICORN),
)


def _validate_month_day(month: int, day: int) -> None:
    """Raise ValueError if month/day is not a valid calendar date."""
    if month < 1 or month > 12:
        raise ValueError(f"Invalid month: {month}.")
    try:
        datetime(2000, month, day)
    except ValueError as exc:
        raise ValueError(f"Invalid day {day} for month {month}.") from exc


def _month_day_value(month: int, day: int) -> int:
    """Encode month/day as an integer for range comparison."""
    return month * 100 + day


def western_sign(month: int, day: int) -> WesternSign:
    """Return the Western zodiac sign for a month and day.

    Parameters
    ----------
    month : int
        Gregorian month (1-12).
    day : int
        Gregorian day of month.

    Returns
    -------
    WesternSign
        Matching tropical zodiac sign.

    Raises
    ------
    ValueError
        If ``month``/``day`` do not form a valid calendar date.
    """
    _validate_month_day(month, day)
    value = _month_day_value(month, day)

    for start_m, start_d, end_m, end_d, sign in _SIGN_RANGES:
        if (
            _month_day_value(start_m, start_d)
            <= value
            <= _month_day_value(end_m, end_d)
        ):
            return sign

    raise ValueError(f"No Western sign found for month={month}, day={day}.")
