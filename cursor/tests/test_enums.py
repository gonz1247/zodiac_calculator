"""Tests for zodiac.enums."""

from zodiac.enums import (
    CompatibilityLevel,
    EASTERN_ANIMALS_BY_INDEX,
    EasternAnimal,
    EasternTrine,
    WesternElement,
    WesternSign,
)


def test_western_sign_display_names() -> None:
    assert WesternSign.ARIES.value == "Aries"
    assert WesternSign.PISCES.value == "Pisces"
    assert len(WesternSign) == 12


def test_eastern_animal_display_names() -> None:
    assert EasternAnimal.RAT.value == "Rat"
    assert EasternAnimal.PIG.value == "Pig"
    assert len(EasternAnimal) == 12


def test_compatibility_level_display_names() -> None:
    assert CompatibilityLevel.COMPATIBLE.value == "Compatible"
    assert CompatibilityLevel.NEUTRAL.value == "Neutral"
    assert CompatibilityLevel.CHALLENGING.value == "Challenging"


def test_every_western_sign_has_element_and_horoscope() -> None:
    for sign in WesternSign:
        assert isinstance(sign.element, WesternElement)
        assert sign.horoscope.strip()


def test_every_eastern_animal_has_trine_horoscope_and_clash() -> None:
    for animal in EasternAnimal:
        assert isinstance(animal.trine, EasternTrine)
        assert animal.horoscope.strip()
        assert isinstance(animal.clash_partner, EasternAnimal)
        assert animal.clash_partner.clash_partner is animal


def test_eastern_animals_by_index_starts_with_rat() -> None:
    assert EASTERN_ANIMALS_BY_INDEX[0] is EasternAnimal.RAT
    assert len(EASTERN_ANIMALS_BY_INDEX) == 12


def test_trine_group_membership() -> None:
    assert EasternAnimal.RAT.trine is EasternTrine.FIRST
    assert EasternAnimal.DRAGON.trine is EasternTrine.FIRST
    assert EasternAnimal.OX.trine is EasternTrine.SECOND
    assert EasternAnimal.TIGER.trine is EasternTrine.THIRD
    assert EasternAnimal.RABBIT.trine is EasternTrine.FOURTH
