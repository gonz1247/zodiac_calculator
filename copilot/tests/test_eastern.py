from datetime import date
from eastern import get_eastern_sign

def test_eastern_cycle():
    # 1900 is Rat, 1901 is Ox, ...
    animals = [
        "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"
    ]
    for i, name in enumerate(animals):
        d = date(1900+i, 1, 1)
        assert get_eastern_sign(d)["name"] == name

def test_eastern_cycle_wrap():
    # 1912 is Rat again
    assert get_eastern_sign(date(1912,1,1))["name"] == "Rat"
    assert get_eastern_sign(date(2020,1,1))["name"] == "Rat"
    assert get_eastern_sign(date(2021,1,1))["name"] == "Ox"
