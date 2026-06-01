"""Parse and validate M/D/YYYY birthdate strings."""

from __future__ import annotations

import re
from datetime import datetime

_DATE_PATTERN = re.compile(r"^\s*(\d{1,2})/(\d{1,2})/(\d{4})\s*$")


def parse_birthdate(date_str: str) -> tuple[int, int, int]:
    """Parse a birthdate string in M/D/YYYY format.

    Parameters
    ----------
    date_str : str
        Date string with month/day as 1-2 digits and a 4-digit year.

    Returns
    -------
    tuple[int, int, int]
        ``(year, month, day)`` parsed from the input.

    Raises
    ------
    ValueError
        If the format is invalid or the date does not exist.
    """
    match = _DATE_PATTERN.match(date_str)
    if match is None:
        raise ValueError(
            f"Invalid date format: {date_str!r}. Expected M/D/YYYY (e.g. 3/21/1990)."
        )

    month = int(match.group(1))
    day = int(match.group(2))
    year = int(match.group(3))

    try:
        datetime(year, month, day)
    except ValueError as exc:
        raise ValueError(f"Invalid date: {date_str!r}.") from exc

    return year, month, day
