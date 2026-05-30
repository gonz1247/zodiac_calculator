import pytest
from parsers import parse_date, is_leap, valid_month_day
from datetime import date

def test_parse_date_valid():
    assert parse_date("2/29/2020") == date(2020,2,29)
    assert parse_date("1/1/2000") == date(2000,1,1)
    assert parse_date("12/31/1999") == date(1999,12,31)

def test_parse_date_invalid_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        parse_date("2020-01-01")
    with pytest.raises(ValueError, match="Invalid date format"):
        parse_date("13/1/2020/extra")

def test_parse_date_month_bounds():
    with pytest.raises(ValueError, match="Month 0 out of range"):
        parse_date("0/10/2020")
    with pytest.raises(ValueError, match="Month 13 out of range"):
        parse_date("13/10/2020")

def test_parse_date_day_bounds():
    with pytest.raises(ValueError, match="Day 31 out of range for month 4"):
        parse_date("4/31/2020")
    with pytest.raises(ValueError, match="Day 30 out of range for month 2"):
        parse_date("2/30/2021")

def test_parse_date_leap_year():
    with pytest.raises(ValueError, match="not a leap year"):
        parse_date("2/29/2021")
    assert parse_date("2/29/2020") == date(2020,2,29)

def test_is_leap():
    assert is_leap(2000)
    assert not is_leap(1900)
    assert is_leap(2020)
    assert not is_leap(2021)

def test_valid_month_day():
    assert valid_month_day(2020,2,29)
    assert not valid_month_day(2021,2,29)
    assert valid_month_day(2021,1,31)
    assert not valid_month_day(2021,4,31)
