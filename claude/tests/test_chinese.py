import pytest

from zodiac.chinese import (
    CHINESE_DESCRIPTIONS,
    CHINESE_OPPOSITES,
    CHINESE_TRINES,
    ChineseAnimal,
    ChineseElement,
    Polarity,
    get_chinese_compatibility,
    get_chinese_sign,
)

# ---------------------------------------------------------------------------
# get_chinese_sign — animal, element, and polarity spot checks
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "year, month, day, animal, element, polarity",
    [
        # 1900: Yang Metal Rat (CNY Jan 31 — Feb 1 is after CNY)
        (1900, 2, 1, ChineseAnimal.RAT, ChineseElement.METAL, Polarity.YANG),
        # 1901: Yin Metal Ox
        (1901, 3, 1, ChineseAnimal.OX, ChineseElement.METAL, Polarity.YIN),
        # 1902: Yang Water Tiger
        (1902, 3, 1, ChineseAnimal.TIGER, ChineseElement.WATER, Polarity.YANG),
        # 1903: Yin Water Rabbit
        (1903, 3, 1, ChineseAnimal.RABBIT, ChineseElement.WATER, Polarity.YIN),
        # 1904: Yang Wood Dragon
        (1904, 3, 1, ChineseAnimal.DRAGON, ChineseElement.WOOD, Polarity.YANG),
        # 1905: Yin Wood Snake
        (1905, 3, 1, ChineseAnimal.SNAKE, ChineseElement.WOOD, Polarity.YIN),
        # 1906: Yang Fire Horse
        (1906, 3, 1, ChineseAnimal.HORSE, ChineseElement.FIRE, Polarity.YANG),
        # 1907: Yin Fire Goat
        (1907, 3, 1, ChineseAnimal.GOAT, ChineseElement.FIRE, Polarity.YIN),
        # 1908: Yang Earth Monkey
        (1908, 3, 1, ChineseAnimal.MONKEY, ChineseElement.EARTH, Polarity.YANG),
        # 1909: Yin Earth Rooster
        (1909, 3, 1, ChineseAnimal.ROOSTER, ChineseElement.EARTH, Polarity.YIN),
        # 1910: Yang Metal Dog
        (1910, 3, 1, ChineseAnimal.DOG, ChineseElement.METAL, Polarity.YANG),
        # 1911: Yin Metal Pig
        (1911, 3, 1, ChineseAnimal.PIG, ChineseElement.METAL, Polarity.YIN),
        # 2024: Yang Wood Dragon (CNY Feb 10 — Mar 1 is after CNY)
        (2024, 3, 1, ChineseAnimal.DRAGON, ChineseElement.WOOD, Polarity.YANG),
        # 2025: Yin Wood Snake (CNY Jan 29 — Mar 1 is after CNY)
        (2025, 3, 1, ChineseAnimal.SNAKE, ChineseElement.WOOD, Polarity.YIN),
    ],
)
def test_get_chinese_sign(year, month, day, animal, element, polarity):
    result_animal, result_element, result_polarity = get_chinese_sign(year, month, day)
    assert result_animal == animal
    assert result_element == element
    assert result_polarity == polarity


# ---------------------------------------------------------------------------
# Chinese New Year boundary — born before CNY uses prior year's sign
# ---------------------------------------------------------------------------


def test_cny_boundary_before():
    # Jan 1 2024 is before CNY (Feb 10 2024) → sign is 2023 = Rabbit
    animal, element, polarity = get_chinese_sign(2024, 1, 1)
    assert animal == ChineseAnimal.RABBIT


def test_cny_boundary_on_cny_day():
    # Feb 10 2024 is CNY itself → Dragon year starts
    animal, element, polarity = get_chinese_sign(2024, 2, 10)
    assert animal == ChineseAnimal.DRAGON


def test_cny_boundary_after():
    # Feb 11 2024 is after CNY → still Dragon
    animal, element, polarity = get_chinese_sign(2024, 2, 11)
    assert animal == ChineseAnimal.DRAGON


def test_year_not_in_cny_table():
    # Year 1800 is outside the table — falls back to year directly
    # (1800 - 4) % 12 = 1796 % 12 = 8 → Monkey
    animal, element, polarity = get_chinese_sign(1800, 6, 15)
    assert animal == ChineseAnimal.MONKEY


# ---------------------------------------------------------------------------
# CHINESE_TRINES and CHINESE_OPPOSITES — structural checks
# ---------------------------------------------------------------------------


def test_all_animals_in_trines():
    for animal in ChineseAnimal:
        assert animal in CHINESE_TRINES


def test_trine_values_in_range():
    for animal, trine in CHINESE_TRINES.items():
        assert trine in (1, 2, 3, 4)


def test_opposites_count():
    assert len(CHINESE_OPPOSITES) == 6


# ---------------------------------------------------------------------------
# CHINESE_DESCRIPTIONS — every animal has a non-empty description
# ---------------------------------------------------------------------------


def test_chinese_descriptions_complete():
    for animal in ChineseAnimal:
        assert animal in CHINESE_DESCRIPTIONS
        assert len(CHINESE_DESCRIPTIONS[animal]) > 0


# ---------------------------------------------------------------------------
# get_chinese_compatibility — all four branches
# ---------------------------------------------------------------------------


def test_compatibility_same_animal():
    result = get_chinese_compatibility(ChineseAnimal.RAT, ChineseAnimal.RAT)
    assert "Rat" in result


def test_compatibility_opposite_pair():
    # Rat and Horse are opposites
    result = get_chinese_compatibility(ChineseAnimal.RAT, ChineseAnimal.HORSE)
    assert "Rat" in result
    assert "Horse" in result
    assert "opposite" in result.lower() or "challenging" in result.lower()


def test_compatibility_same_trine():
    # Rat, Dragon, Monkey are all in trine 1
    result = get_chinese_compatibility(ChineseAnimal.RAT, ChineseAnimal.DRAGON)
    assert "Rat" in result
    assert "Dragon" in result
    assert "trine" in result.lower()


def test_compatibility_neutral():
    # Rat (trine 1) and Ox (trine 2) — different trines, not opposites
    result = get_chinese_compatibility(ChineseAnimal.RAT, ChineseAnimal.OX)
    assert "Rat" in result
    assert "Ox" in result


def test_compatibility_all_opposite_pairs_covered():
    # Every known opposite pair should hit the "opposite" branch
    expected_opposites = [
        (ChineseAnimal.RAT, ChineseAnimal.HORSE),
        (ChineseAnimal.OX, ChineseAnimal.GOAT),
        (ChineseAnimal.TIGER, ChineseAnimal.MONKEY),
        (ChineseAnimal.RABBIT, ChineseAnimal.ROOSTER),
        (ChineseAnimal.DRAGON, ChineseAnimal.DOG),
        (ChineseAnimal.SNAKE, ChineseAnimal.PIG),
    ]
    for a1, a2 in expected_opposites:
        assert frozenset([a1, a2]) in CHINESE_OPPOSITES
