"""Tests for zodiac.compatibility."""

import pytest

from zodiac.compatibility import eastern_compatibility, western_compatibility
from zodiac.enums import CompatibilityLevel, EasternAnimal, WesternSign


@pytest.mark.parametrize(
    ("sign_a", "sign_b", "expected"),
    [
        (WesternSign.ARIES, WesternSign.LEO, CompatibilityLevel.COMPATIBLE),
        (WesternSign.ARIES, WesternSign.CANCER, CompatibilityLevel.CHALLENGING),
        (WesternSign.GEMINI, WesternSign.LIBRA, CompatibilityLevel.COMPATIBLE),
        (WesternSign.GEMINI, WesternSign.SCORPIO, CompatibilityLevel.NEUTRAL),
        (WesternSign.ARIES, WesternSign.SAGITTARIUS, CompatibilityLevel.COMPATIBLE),
        (WesternSign.TAURUS, WesternSign.VIRGO, CompatibilityLevel.COMPATIBLE),
        (WesternSign.TAURUS, WesternSign.CANCER, CompatibilityLevel.COMPATIBLE),
    ],
)
def test_western_compatibility(sign_a, sign_b, expected) -> None:
    assert western_compatibility(sign_a, sign_b) is expected


@pytest.mark.parametrize(
    ("animal_a", "animal_b", "expected"),
    [
        (EasternAnimal.RAT, EasternAnimal.DRAGON, CompatibilityLevel.COMPATIBLE),
        (EasternAnimal.RAT, EasternAnimal.HORSE, CompatibilityLevel.CHALLENGING),
        (EasternAnimal.RAT, EasternAnimal.OX, CompatibilityLevel.NEUTRAL),
        (EasternAnimal.TIGER, EasternAnimal.DOG, CompatibilityLevel.COMPATIBLE),
    ],
)
def test_eastern_compatibility(animal_a, animal_b, expected) -> None:
    assert eastern_compatibility(animal_a, animal_b) is expected
