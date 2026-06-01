"""Western and Eastern zodiac compatibility rules."""

from __future__ import annotations

from zodiac.enums import (
    CompatibilityLevel,
    EasternAnimal,
    WesternElement,
    WesternSign,
)

_COMPATIBLE_CROSS_ELEMENTS: frozenset[frozenset[WesternElement]] = frozenset(
    {
        frozenset({WesternElement.FIRE, WesternElement.AIR}),
        frozenset({WesternElement.EARTH, WesternElement.WATER}),
    }
)

_CHALLENGING_PAIRS: frozenset[frozenset[WesternElement]] = frozenset(
    {
        frozenset({WesternElement.FIRE, WesternElement.WATER}),
        frozenset({WesternElement.AIR, WesternElement.EARTH}),
        frozenset({WesternElement.FIRE, WesternElement.EARTH}),
    }
)


def western_compatibility(
    sign_a: WesternSign, sign_b: WesternSign
) -> CompatibilityLevel:
    """Return Western compatibility based on sign elements.

    Parameters
    ----------
    sign_a : WesternSign
        First sign.
    sign_b : WesternSign
        Second sign.

    Returns
    -------
    CompatibilityLevel
        Compatibility rating for the pair.
    """
    element_a = sign_a.element
    element_b = sign_b.element
    pair = frozenset({element_a, element_b})

    if element_a is element_b:
        return CompatibilityLevel.COMPATIBLE
    if pair in _CHALLENGING_PAIRS:
        return CompatibilityLevel.CHALLENGING
    if pair in _COMPATIBLE_CROSS_ELEMENTS:
        return CompatibilityLevel.COMPATIBLE
    return CompatibilityLevel.NEUTRAL


def eastern_compatibility(
    animal_a: EasternAnimal, animal_b: EasternAnimal
) -> CompatibilityLevel:
    """Return Eastern compatibility based on trine and clash rules.

    Parameters
    ----------
    animal_a : EasternAnimal
        First animal.
    animal_b : EasternAnimal
        Second animal.

    Returns
    -------
    CompatibilityLevel
        Compatibility rating for the pair.
    """
    if animal_a.trine is animal_b.trine:
        return CompatibilityLevel.COMPATIBLE
    if animal_b is animal_a.clash_partner:
        return CompatibilityLevel.CHALLENGING
    return CompatibilityLevel.NEUTRAL
