import pytest

from zodiac.western import (
    WESTERN_DESCRIPTIONS,
    WESTERN_ELEMENT,
    WesternElement,
    WesternSign,
    get_western_compatibility,
    get_western_sign,
)

# ---------------------------------------------------------------------------
# get_western_sign — one boundary test per sign, plus cusp edges
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "month, day, expected",
    [
        # Capricorn: Dec 22 – Jan 19
        (12, 22, WesternSign.CAPRICORN),
        (1, 1, WesternSign.CAPRICORN),
        (1, 19, WesternSign.CAPRICORN),
        # Aquarius: Jan 20 – Feb 18
        (1, 20, WesternSign.AQUARIUS),
        (2, 18, WesternSign.AQUARIUS),
        # Pisces: Feb 19 – Mar 20
        (2, 19, WesternSign.PISCES),
        (3, 20, WesternSign.PISCES),
        # Aries: Mar 21 – Apr 19
        (3, 21, WesternSign.ARIES),
        (4, 19, WesternSign.ARIES),
        # Taurus: Apr 20 – May 20
        (4, 20, WesternSign.TAURUS),
        (5, 20, WesternSign.TAURUS),
        # Gemini: May 21 – Jun 20
        (5, 21, WesternSign.GEMINI),
        (6, 20, WesternSign.GEMINI),
        # Cancer: Jun 21 – Jul 22
        (6, 21, WesternSign.CANCER),
        (7, 22, WesternSign.CANCER),
        # Leo: Jul 23 – Aug 22
        (7, 23, WesternSign.LEO),
        (8, 22, WesternSign.LEO),
        # Virgo: Aug 23 – Sep 22
        (8, 23, WesternSign.VIRGO),
        (9, 22, WesternSign.VIRGO),
        # Libra: Sep 23 – Oct 22
        (9, 23, WesternSign.LIBRA),
        (10, 22, WesternSign.LIBRA),
        # Scorpio: Oct 23 – Nov 21
        (10, 23, WesternSign.SCORPIO),
        (11, 21, WesternSign.SCORPIO),
        # Sagittarius: Nov 22 – Dec 21
        (11, 22, WesternSign.SAGITTARIUS),
        (12, 21, WesternSign.SAGITTARIUS),
        # Dec 31 → Capricorn (wraps to default)
        (12, 31, WesternSign.CAPRICORN),
    ],
)
def test_get_western_sign(month, day, expected):
    assert get_western_sign(month, day) == expected


# ---------------------------------------------------------------------------
# WESTERN_ELEMENT — every sign maps to the correct element
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "sign, expected_element",
    [
        (WesternSign.ARIES, WesternElement.FIRE),
        (WesternSign.LEO, WesternElement.FIRE),
        (WesternSign.SAGITTARIUS, WesternElement.FIRE),
        (WesternSign.TAURUS, WesternElement.EARTH),
        (WesternSign.VIRGO, WesternElement.EARTH),
        (WesternSign.CAPRICORN, WesternElement.EARTH),
        (WesternSign.GEMINI, WesternElement.AIR),
        (WesternSign.LIBRA, WesternElement.AIR),
        (WesternSign.AQUARIUS, WesternElement.AIR),
        (WesternSign.CANCER, WesternElement.WATER),
        (WesternSign.SCORPIO, WesternElement.WATER),
        (WesternSign.PISCES, WesternElement.WATER),
    ],
)
def test_western_element_mapping(sign, expected_element):
    assert WESTERN_ELEMENT[sign] == expected_element


# ---------------------------------------------------------------------------
# WESTERN_DESCRIPTIONS — every sign has a non-empty description
# ---------------------------------------------------------------------------


def test_western_descriptions_complete():
    for sign in WesternSign:
        assert sign in WESTERN_DESCRIPTIONS
        assert len(WESTERN_DESCRIPTIONS[sign]) > 0


# ---------------------------------------------------------------------------
# get_western_compatibility — all three tiers
# ---------------------------------------------------------------------------


def test_compatibility_same_element():
    # Aries and Leo are both Fire
    result = get_western_compatibility(WesternSign.ARIES, WesternSign.LEO)
    assert "Fire" in result
    assert "Aries" in result
    assert "Leo" in result


def test_compatibility_complementary_fire_air():
    # Fire + Air are complementary
    result = get_western_compatibility(WesternSign.ARIES, WesternSign.GEMINI)
    assert "Aries" in result
    assert "Gemini" in result
    assert "complementary" in result.lower() or "balance" in result.lower()


def test_compatibility_complementary_earth_water():
    # Earth + Water are complementary
    result = get_western_compatibility(WesternSign.TAURUS, WesternSign.CANCER)
    assert "Taurus" in result
    assert "Cancer" in result


def test_compatibility_neutral_fire_earth():
    # Fire + Earth — neither same nor complementary
    result = get_western_compatibility(WesternSign.ARIES, WesternSign.TAURUS)
    assert "Aries" in result
    assert "Taurus" in result


def test_compatibility_neutral_fire_water():
    # Fire + Water — challenging pairing
    result = get_western_compatibility(WesternSign.LEO, WesternSign.SCORPIO)
    assert "Leo" in result
    assert "Scorpio" in result


def test_compatibility_neutral_air_earth():
    result = get_western_compatibility(WesternSign.GEMINI, WesternSign.VIRGO)
    assert "Gemini" in result
    assert "Virgo" in result


def test_compatibility_neutral_air_water():
    result = get_western_compatibility(WesternSign.AQUARIUS, WesternSign.PISCES)
    assert "Aquarius" in result
    assert "Pisces" in result
