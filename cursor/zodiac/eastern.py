"""Eastern Chinese zodiac animal lookup (CNY-aware)."""

from __future__ import annotations

from datetime import date, datetime

from zodiac.cny_dates import chinese_new_year_date
from zodiac.enums import EASTERN_ANIMALS_BY_INDEX, EasternAnimal


def _validate_date(year: int, month: int, day: int) -> None:
    """Raise ValueError if the date is invalid."""
    try:
        datetime(year, month, day)
    except ValueError as exc:
        raise ValueError(f"Invalid date: {month}/{day}/{year}.") from exc


def eastern_sign(year: int, month: int, day: int) -> EasternAnimal:
    """Return the Eastern zodiac animal for a birthdate.

    Uses Chinese New Year boundaries: birthdates before CNY in a given
    Gregorian year belong to the previous zodiac year.

    Parameters
    ----------
    year : int
        Gregorian birth year.
    month : int
        Gregorian birth month.
    day : int
        Gregorian birth day.

    Returns
    -------
    EasternAnimal
        Matching zodiac animal.

    Raises
    ------
    ValueError
        If the date is invalid or the year is outside the CNY lookup range.
    """
    _validate_date(year, month, day)

    cny_year, cny_month, cny_day = chinese_new_year_date(year)
    birth = date(year, month, day)
    cny = date(cny_year, cny_month, cny_day)

    zodiac_year = year if birth >= cny else year - 1
    index = (zodiac_year - 1900) % 12
    return EASTERN_ANIMALS_BY_INDEX[index]
