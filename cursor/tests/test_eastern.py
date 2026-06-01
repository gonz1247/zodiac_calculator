"""Tests for zodiac.eastern and zodiac.cny_dates."""

import pytest

from zodiac.cny_dates import chinese_new_year_date
from zodiac.eastern import eastern_sign
from zodiac.enums import EasternAnimal


def test_chinese_new_year_1990() -> None:
    assert chinese_new_year_date(1990) == (1990, 1, 27)


def test_chinese_new_year_out_of_range() -> None:
    with pytest.raises(ValueError, match="outside the supported range"):
        chinese_new_year_date(1899)
    with pytest.raises(ValueError, match="outside the supported range"):
        chinese_new_year_date(2101)


@pytest.mark.parametrize(
    ("month", "day", "expected"),
    [
        (1, 26, EasternAnimal.SNAKE),
        (1, 27, EasternAnimal.HORSE),
        (12, 31, EasternAnimal.HORSE),
    ],
)
def test_eastern_sign_cny_boundaries_1990(
    month: int, day: int, expected: EasternAnimal
) -> None:
    assert eastern_sign(1990, month, day) is expected


def test_eastern_sign_invalid_date() -> None:
    with pytest.raises(ValueError, match="Invalid date"):
        eastern_sign(1990, 2, 30)
