"""Date parsing with error messages for zodiac calculator.
Covers leap years and valid month/day bounds."""
from datetime import date
import re

def is_leap(year: int) -> bool:
    """Leap year logic: divisible by 4, not 100 unless 400."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def valid_month_day(year: int, month: int, day: int) -> bool:
    """Return True if (month, day) is valid for year (leap year aware)."""
    if not (1 <= month <= 12):
        return False
    days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2:
        max_day = 29 if is_leap(year) else 28
    else:
        max_day = days_in_month[month]
    return 1 <= day <= max_day

def parse_date(s: str) -> date:
    """Parse M/D/YYYY string to date, raising ValueError with clear message on error.
    Handles leap years and month/day bounds.
    """
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", s.strip())
    if not m:
        raise ValueError(f"Invalid date format: '{s}'. Use M/D/YYYY.")
    month, day, year = map(int, m.groups())
    if not (1 <= month <= 12):
        raise ValueError(f"Month {month} out of range (1-12)")
    if not valid_month_day(year, month, day):
        if month == 2 and day == 29:
            raise ValueError(f"{year} is not a leap year; Feb 29 is invalid")
        raise ValueError(f"Day {day} out of range for month {month} in {year}")
    return date(year, month, day)
