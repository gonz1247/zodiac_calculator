from unittest.mock import patch

import pytest

from main import (
    display_chinese,
    display_chinese_compatibility,
    display_western,
    display_western_compatibility,
    parse_date,
    run_loop,
)
from zodiac.chinese import ChineseAnimal, ChineseElement, Polarity
from zodiac.western import WesternSign

# ---------------------------------------------------------------------------
# parse_date
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("1990-05-15", (1990, 5, 15)),
        ("2000-01-01", (2000, 1, 1)),
        ("2024-02-29", (2024, 2, 29)),  # valid leap day
        ("05/15/1990", (1990, 5, 15)),
        ("1/1/2000", (2000, 1, 1)),
    ],
)
def test_parse_date_valid(date_str, expected):
    assert parse_date(date_str) == expected


@pytest.mark.parametrize(
    "date_str",
    [
        "not-a-date",
        "1990/05/15",  # wrong separator for YYYY format
        "2023-02-29",  # invalid leap day (2023 is not a leap year)
        "2000-13-01",  # invalid month
        "2000-00-01",  # month 0
        "2000-01-00",  # day 0
        "",
        "1990-5-15",  # single-digit month in YYYY-MM-DD (not matched by \d{2})
    ],
)
def test_parse_date_invalid(date_str):
    assert parse_date(date_str) is None


# ---------------------------------------------------------------------------
# display_western
# ---------------------------------------------------------------------------


def test_display_western(capsys):
    display_western(WesternSign.ARIES)
    out = capsys.readouterr().out
    assert "Aries" in out
    assert len(out) > 20


# ---------------------------------------------------------------------------
# display_chinese
# ---------------------------------------------------------------------------


def test_display_chinese(capsys):
    display_chinese(ChineseAnimal.RAT, ChineseElement.METAL, Polarity.YANG)
    out = capsys.readouterr().out
    assert "Yang" in out
    assert "Metal" in out
    assert "Rat" in out
    assert len(out) > 20


# ---------------------------------------------------------------------------
# display_western_compatibility
# ---------------------------------------------------------------------------


def test_display_western_compatibility(capsys):
    display_western_compatibility(WesternSign.ARIES, WesternSign.LEO)
    out = capsys.readouterr().out
    assert "Leo" in out  # comparing-with label
    assert "Aries" in out  # appears in compatibility text


# ---------------------------------------------------------------------------
# display_chinese_compatibility
# ---------------------------------------------------------------------------


def test_display_chinese_compatibility(capsys):
    display_chinese_compatibility(
        ChineseAnimal.RAT,
        ChineseAnimal.DRAGON,
        ChineseElement.WOOD,
        Polarity.YANG,
    )
    out = capsys.readouterr().out
    assert "Yang Wood Dragon" in out  # comparing-with label
    assert "Rat" in out


# ---------------------------------------------------------------------------
# run_loop — mocked input sequences
# ---------------------------------------------------------------------------


def test_run_loop_quit_immediately(capsys):
    with patch("builtins.input", side_effect=["q"]):
        run_loop()
    out = capsys.readouterr().out
    assert "Goodbye" in out


def test_run_loop_basic_lookup_then_quit(capsys):
    inputs = [
        "1990-05-15",  # birthdate
        "n",  # no compatibility
        "q",  # quit
    ]
    with patch("builtins.input", side_effect=inputs):
        run_loop()
    out = capsys.readouterr().out
    assert "Taurus" in out
    assert "Goodbye" in out


def test_run_loop_with_compatibility(capsys):
    inputs = [
        "1990-05-15",  # first birthdate (Taurus)
        "y",  # yes to compatibility
        "1988-02-17",  # second birthdate (born after CNY Feb 17 1988 → Dragon)
        "q",  # quit
    ]
    with patch("builtins.input", side_effect=inputs):
        run_loop()
    out = capsys.readouterr().out
    assert "Taurus" in out
    assert "Compatibility" in out
    assert "Goodbye" in out


def test_run_loop_invalid_date_then_valid(capsys):
    inputs = [
        "not-a-date",  # invalid — should prompt again
        "1990-05-15",  # valid
        "n",
        "q",
    ]
    with patch("builtins.input", side_effect=inputs):
        run_loop()
    out = capsys.readouterr().out
    assert "Invalid" in out
    assert "Taurus" in out


def test_run_loop_invalid_second_date_then_valid(capsys):
    inputs = [
        "1990-05-15",  # first birthdate
        "y",  # yes to compatibility
        "bad-date",  # invalid second date
        "1985-02-20",  # valid second date (after CNY Feb 20 1985 → Ox)
        "q",
    ]
    with patch("builtins.input", side_effect=inputs):
        run_loop()
    out = capsys.readouterr().out
    assert "Invalid" in out
    assert "Compatibility" in out


def test_run_loop_multiple_lookups(capsys):
    inputs = [
        "1990-05-15",  # first birthdate
        "n",
        "2000-12-25",  # second birthdate
        "n",
        "q",
    ]
    with patch("builtins.input", side_effect=inputs):
        run_loop()
    out = capsys.readouterr().out
    assert "Taurus" in out
    assert "Capricorn" in out
    assert "Goodbye" in out
