"""Zodiac domain enumerations and metadata."""

from __future__ import annotations

from enum import Enum, auto
from enum import StrEnum


class WesternElement(Enum):
    """Classical element for Western zodiac signs."""

    FIRE = auto()
    EARTH = auto()
    AIR = auto()
    WATER = auto()


class EasternTrine(Enum):
    """Trine group for Eastern zodiac animals (internal compatibility metadata)."""

    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    FOURTH = auto()


class CompatibilityLevel(StrEnum):
    """Compatibility result for sign or animal pairs."""

    COMPATIBLE = "Compatible"
    NEUTRAL = "Neutral"
    CHALLENGING = "Challenging"


class WesternSign(StrEnum):
    """Western tropical zodiac sign."""

    ARIES = "Aries"
    TAURUS = "Taurus"
    GEMINI = "Gemini"
    CANCER = "Cancer"
    LEO = "Leo"
    VIRGO = "Virgo"
    LIBRA = "Libra"
    SCORPIO = "Scorpio"
    SAGITTARIUS = "Sagittarius"
    CAPRICORN = "Capricorn"
    AQUARIUS = "Aquarius"
    PISCES = "Pisces"

    @property
    def element(self) -> WesternElement:
        """Return the classical element for this sign."""
        return _WESTERN_ELEMENTS[self]

    @property
    def horoscope(self) -> str:
        """Return the static personality blurb for this sign."""
        return _WESTERN_HOROSCOPES[self]


class EasternAnimal(StrEnum):
    """Chinese zodiac animal."""

    RAT = "Rat"
    OX = "Ox"
    TIGER = "Tiger"
    RABBIT = "Rabbit"
    DRAGON = "Dragon"
    SNAKE = "Snake"
    HORSE = "Horse"
    GOAT = "Goat"
    MONKEY = "Monkey"
    ROOSTER = "Rooster"
    DOG = "Dog"
    PIG = "Pig"

    @property
    def trine(self) -> EasternTrine:
        """Return the trine group for this animal."""
        return _EASTERN_TRINES[self]

    @property
    def horoscope(self) -> str:
        """Return the static personality blurb for this animal."""
        return _EASTERN_HOROSCOPES[self]

    @property
    def clash_partner(self) -> EasternAnimal:
        """Return the animal six positions away on the 12-cycle."""
        return _CLASH_PARTNERS[self]


_WESTERN_ELEMENTS: dict[WesternSign, WesternElement] = {
    WesternSign.ARIES: WesternElement.FIRE,
    WesternSign.TAURUS: WesternElement.EARTH,
    WesternSign.GEMINI: WesternElement.AIR,
    WesternSign.CANCER: WesternElement.WATER,
    WesternSign.LEO: WesternElement.FIRE,
    WesternSign.VIRGO: WesternElement.EARTH,
    WesternSign.LIBRA: WesternElement.AIR,
    WesternSign.SCORPIO: WesternElement.WATER,
    WesternSign.SAGITTARIUS: WesternElement.FIRE,
    WesternSign.CAPRICORN: WesternElement.EARTH,
    WesternSign.AQUARIUS: WesternElement.AIR,
    WesternSign.PISCES: WesternElement.WATER,
}

_WESTERN_HOROSCOPES: dict[WesternSign, str] = {
    WesternSign.ARIES: "Aries are bold, energetic, and natural leaders who thrive on challenge.",
    WesternSign.TAURUS: "Taurus are steady, patient, and appreciate comfort, beauty, and reliability.",
    WesternSign.GEMINI: "Gemini are curious, adaptable, and quick-witted communicators.",
    WesternSign.CANCER: "Cancer are nurturing, intuitive, and deeply connected to home and family.",
    WesternSign.LEO: "Leo are confident, warm-hearted, and drawn to creative self-expression.",
    WesternSign.VIRGO: "Virgo are practical, detail-oriented, and dedicated to improvement.",
    WesternSign.LIBRA: "Libra seek harmony, fairness, and meaningful connection with others.",
    WesternSign.SCORPIO: "Scorpio are passionate, perceptive, and unafraid of life's depths.",
    WesternSign.SAGITTARIUS: "Sagittarius are adventurous, optimistic, and hungry for knowledge.",
    WesternSign.CAPRICORN: "Capricorn are disciplined, ambitious, and built for long-term goals.",
    WesternSign.AQUARIUS: "Aquarius are independent, inventive, and motivated by big ideas.",
    WesternSign.PISCES: "Pisces are compassionate, imaginative, and attuned to emotion.",
}

_EASTERN_TRINES: dict[EasternAnimal, EasternTrine] = {
    EasternAnimal.RAT: EasternTrine.FIRST,
    EasternAnimal.DRAGON: EasternTrine.FIRST,
    EasternAnimal.MONKEY: EasternTrine.FIRST,
    EasternAnimal.OX: EasternTrine.SECOND,
    EasternAnimal.SNAKE: EasternTrine.SECOND,
    EasternAnimal.ROOSTER: EasternTrine.SECOND,
    EasternAnimal.TIGER: EasternTrine.THIRD,
    EasternAnimal.HORSE: EasternTrine.THIRD,
    EasternAnimal.DOG: EasternTrine.THIRD,
    EasternAnimal.RABBIT: EasternTrine.FOURTH,
    EasternAnimal.GOAT: EasternTrine.FOURTH,
    EasternAnimal.PIG: EasternTrine.FOURTH,
}

_EASTERN_HOROSCOPES: dict[EasternAnimal, str] = {
    EasternAnimal.RAT: "Rats are resourceful, charming, and quick to spot opportunity.",
    EasternAnimal.OX: "Oxen are diligent, dependable, and value hard work and honesty.",
    EasternAnimal.TIGER: "Tigers are brave, competitive, and driven by a strong sense of justice.",
    EasternAnimal.RABBIT: "Rabbits are gentle, tactful, and prefer peaceful surroundings.",
    EasternAnimal.DRAGON: "Dragons are charismatic, confident, and natural-born leaders.",
    EasternAnimal.SNAKE: "Snakes are wise, intuitive, and thoughtful in their choices.",
    EasternAnimal.HORSE: "Horses are free-spirited, witty, and thrive on independence.",
    EasternAnimal.GOAT: "Goats are creative, empathetic, and drawn to art and beauty.",
    EasternAnimal.MONKEY: "Monkeys are clever, playful, and skilled at solving problems.",
    EasternAnimal.ROOSTER: "Roosters are observant, hardworking, and proud of their standards.",
    EasternAnimal.DOG: "Dogs are loyal, sincere, and deeply committed to those they trust.",
    EasternAnimal.PIG: "Pigs are generous, sincere, and enjoy life's simple pleasures.",
}

_CLASH_PARTNERS: dict[EasternAnimal, EasternAnimal] = {
    EasternAnimal.RAT: EasternAnimal.HORSE,
    EasternAnimal.OX: EasternAnimal.GOAT,
    EasternAnimal.TIGER: EasternAnimal.MONKEY,
    EasternAnimal.RABBIT: EasternAnimal.ROOSTER,
    EasternAnimal.DRAGON: EasternAnimal.DOG,
    EasternAnimal.SNAKE: EasternAnimal.PIG,
    EasternAnimal.HORSE: EasternAnimal.RAT,
    EasternAnimal.GOAT: EasternAnimal.OX,
    EasternAnimal.MONKEY: EasternAnimal.TIGER,
    EasternAnimal.ROOSTER: EasternAnimal.RABBIT,
    EasternAnimal.DOG: EasternAnimal.DRAGON,
    EasternAnimal.PIG: EasternAnimal.SNAKE,
}

# Ordered by zodiac year index: (year - 1900) % 12
EASTERN_ANIMALS_BY_INDEX: tuple[EasternAnimal, ...] = (
    EasternAnimal.RAT,
    EasternAnimal.OX,
    EasternAnimal.TIGER,
    EasternAnimal.RABBIT,
    EasternAnimal.DRAGON,
    EasternAnimal.SNAKE,
    EasternAnimal.HORSE,
    EasternAnimal.GOAT,
    EasternAnimal.MONKEY,
    EasternAnimal.ROOSTER,
    EasternAnimal.DOG,
    EasternAnimal.PIG,
)
