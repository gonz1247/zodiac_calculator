from datetime import date
from western import get_western_sign

def test_western_signs():
    # Aries: Mar 21–Apr 19
    assert get_western_sign(date(2020,3,21))["name"] == "Aries"
    assert get_western_sign(date(2020,4,19))["name"] == "Aries"
    # Capricorn: Dec 22–Jan 19
    assert get_western_sign(date(2020,12,22))["name"] == "Capricorn"
    assert get_western_sign(date(2021,1,19))["name"] == "Capricorn"
    # Pisces: Feb 19–Mar 20
    assert get_western_sign(date(2020,2,19))["name"] == "Pisces"
    assert get_western_sign(date(2020,3,20))["name"] == "Pisces"
    # Libra: Sep 23–Oct 22
    assert get_western_sign(date(2020,9,23))["name"] == "Libra"
    assert get_western_sign(date(2020,10,22))["name"] == "Libra"

def test_western_sign_range_wrap():
    # Before Jan 20 is Capricorn
    assert get_western_sign(date(2020,1,1))["name"] == "Capricorn"
    assert get_western_sign(date(2020,1,19))["name"] == "Capricorn"
