"""Tests for zodiac.western."""

from unittest.mock import patch

import pytest

from zodiac.enums import WesternSign
from zodiac.western import western_sign


@pytest.mark.parametrize(
    ("month", "day", "expected"),
    [
        (3, 20, WesternSign.PISCES),
        (3, 21, WesternSign.ARIES),
        (1, 19, WesternSign.CAPRICORN),
        (1, 20, WesternSign.AQUARIUS),
        (12, 22, WesternSign.CAPRICORN),
        (7, 23, WesternSign.LEO),
        (2, 19, WesternSign.PISCES),
        (11, 22, WesternSign.SAGITTARIUS),
    ],
)
def test_western_sign_boundaries(month: int, day: int, expected: WesternSign) -> None:
    assert western_sign(month, day) is expected


def test_western_sign_invalid_month() -> None:
    with pytest.raises(ValueError, match="Invalid month"):
        western_sign(13, 1)


def test_western_sign_invalid_day() -> None:
    with pytest.raises(ValueError, match="Invalid day"):
        western_sign(2, 30)


def test_western_sign_no_matching_range() -> None:
    with patch("zodiac.western._SIGN_RANGES", ()):
        with pytest.raises(ValueError, match="No Western sign found"):
            western_sign(6, 15)
