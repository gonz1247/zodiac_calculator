"""Tests for zodiac.parsing."""

import pytest

from zodiac.parsing import parse_birthdate


@pytest.mark.parametrize(
    ("date_str", "expected"),
    [
        ("3/21/1990", (1990, 3, 21)),
        ("03/21/1990", (1990, 3, 21)),
        ("12/1/2000", (2000, 12, 1)),
        (" 1/5/1990 ", (1990, 1, 5)),
    ],
)
def test_parse_birthdate_valid(date_str: str, expected: tuple[int, int, int]) -> None:
    assert parse_birthdate(date_str) == expected


@pytest.mark.parametrize(
    "date_str",
    [
        "3/21/90",
        "1990-03-21",
        "3-21-1990",
        "2/30/1990",
        "13/1/1990",
        "not-a-date",
        "",
    ],
)
def test_parse_birthdate_invalid(date_str: str) -> None:
    with pytest.raises(ValueError):
        parse_birthdate(date_str)
