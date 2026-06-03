from enum import Enum


class ChineseAnimal(Enum):
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


class ChineseElement(Enum):
    WOOD = "Wood"
    FIRE = "Fire"
    EARTH = "Earth"
    METAL = "Metal"
    WATER = "Water"


class Polarity(Enum):
    YANG = "Yang"
    YIN = "Yin"


# Anchors the modular arithmetic to 1900, a verified Yang Metal Rat year:
#   (1900 - CYCLE_ANCHOR) % 12 == 0  → Rat (index 0)
#   (1900 - CYCLE_ANCHOR) % 10 == 6  → Metal (index 3 via // 2)
#   (1900 - CYCLE_ANCHOR) % 2  == 0  → Yang
CYCLE_ANCHOR = 4

_ANIMALS: list[ChineseAnimal] = [
    ChineseAnimal.RAT,
    ChineseAnimal.OX,
    ChineseAnimal.TIGER,
    ChineseAnimal.RABBIT,
    ChineseAnimal.DRAGON,
    ChineseAnimal.SNAKE,
    ChineseAnimal.HORSE,
    ChineseAnimal.GOAT,
    ChineseAnimal.MONKEY,
    ChineseAnimal.ROOSTER,
    ChineseAnimal.DOG,
    ChineseAnimal.PIG,
]

_ELEMENTS: list[ChineseElement] = [
    ChineseElement.WOOD,
    ChineseElement.FIRE,
    ChineseElement.EARTH,
    ChineseElement.METAL,
    ChineseElement.WATER,
]

# Gregorian date of Chinese New Year for each calendar year (1900–2050).
# If a birthday falls before CNY in its year, the prior year's sign applies.
_CNY_DATES: dict[int, tuple[int, int]] = {
    1900: (1, 31),
    1901: (2, 19),
    1902: (2, 8),
    1903: (1, 29),
    1904: (2, 16),
    1905: (2, 4),
    1906: (1, 25),
    1907: (2, 13),
    1908: (2, 2),
    1909: (1, 22),
    1910: (2, 10),
    1911: (1, 30),
    1912: (2, 18),
    1913: (2, 6),
    1914: (1, 26),
    1915: (2, 14),
    1916: (2, 3),
    1917: (1, 23),
    1918: (2, 11),
    1919: (2, 1),
    1920: (2, 20),
    1921: (2, 8),
    1922: (1, 28),
    1923: (2, 16),
    1924: (2, 5),
    1925: (1, 25),
    1926: (2, 13),
    1927: (2, 2),
    1928: (1, 23),
    1929: (2, 10),
    1930: (1, 30),
    1931: (2, 17),
    1932: (2, 6),
    1933: (1, 26),
    1934: (2, 14),
    1935: (2, 4),
    1936: (1, 24),
    1937: (2, 11),
    1938: (1, 31),
    1939: (2, 19),
    1940: (2, 8),
    1941: (1, 27),
    1942: (2, 15),
    1943: (2, 5),
    1944: (1, 25),
    1945: (2, 13),
    1946: (2, 2),
    1947: (1, 22),
    1948: (2, 10),
    1949: (1, 29),
    1950: (2, 17),
    1951: (2, 6),
    1952: (1, 27),
    1953: (2, 14),
    1954: (2, 3),
    1955: (1, 24),
    1956: (2, 12),
    1957: (1, 31),
    1958: (2, 18),
    1959: (2, 8),
    1960: (1, 28),
    1961: (2, 15),
    1962: (2, 5),
    1963: (1, 25),
    1964: (2, 13),
    1965: (2, 2),
    1966: (1, 21),
    1967: (2, 9),
    1968: (1, 30),
    1969: (2, 17),
    1970: (2, 6),
    1971: (1, 27),
    1972: (2, 15),
    1973: (2, 3),
    1974: (1, 23),
    1975: (2, 11),
    1976: (1, 31),
    1977: (2, 18),
    1978: (2, 7),
    1979: (1, 28),
    1980: (2, 16),
    1981: (2, 5),
    1982: (1, 25),
    1983: (2, 13),
    1984: (2, 2),
    1985: (2, 20),
    1986: (2, 9),
    1987: (1, 29),
    1988: (2, 17),
    1989: (2, 6),
    1990: (1, 27),
    1991: (2, 15),
    1992: (2, 4),
    1993: (1, 23),
    1994: (2, 10),
    1995: (1, 31),
    1996: (2, 19),
    1997: (2, 7),
    1998: (1, 28),
    1999: (2, 16),
    2000: (2, 5),
    2001: (1, 24),
    2002: (2, 12),
    2003: (2, 1),
    2004: (1, 22),
    2005: (2, 9),
    2006: (1, 29),
    2007: (2, 18),
    2008: (2, 7),
    2009: (1, 26),
    2010: (2, 14),
    2011: (2, 3),
    2012: (1, 23),
    2013: (2, 10),
    2014: (1, 31),
    2015: (2, 19),
    2016: (2, 8),
    2017: (1, 28),
    2018: (2, 16),
    2019: (2, 5),
    2020: (1, 25),
    2021: (2, 12),
    2022: (2, 1),
    2023: (1, 22),
    2024: (2, 10),
    2025: (1, 29),
    2026: (2, 17),
    2027: (2, 6),
    2028: (1, 26),
    2029: (2, 13),
    2030: (2, 3),
    2031: (1, 23),
    2032: (2, 11),
    2033: (1, 31),
    2034: (2, 19),
    2035: (2, 8),
    2036: (1, 28),
    2037: (2, 15),
    2038: (2, 4),
    2039: (1, 24),
    2040: (2, 12),
    2041: (2, 1),
    2042: (1, 22),
    2043: (2, 10),
    2044: (1, 30),
    2045: (2, 17),
    2046: (2, 6),
    2047: (1, 26),
    2048: (2, 14),
    2049: (2, 2),
    2050: (1, 23),
}

CHINESE_DESCRIPTIONS: dict[ChineseAnimal, str] = {
    ChineseAnimal.RAT: (
        "The Rat is the first sign of the Chinese zodiac, and those born under it are among "
        "the most resourceful and opportunistic of all. Quick-witted and charming, Rats have "
        "a talent for spotting potential where others see none and adapting swiftly to "
        "changing circumstances. They are sociable and imaginative, with a sharp eye for "
        "detail that makes them excellent strategists. Though they can be guarded about their "
        "own feelings, they are deeply loyal to those in their inner circle and will go to "
        "great lengths to protect the people they love."
    ),
    ChineseAnimal.OX: (
        "The Ox is a symbol of diligence, dependability, and quiet strength. Those born in "
        "the Year of the Ox are methodical and patient — they do not rush, but they never "
        "stop moving toward their goals either. They possess a strong moral compass and an "
        "almost unshakeable sense of duty, making them some of the most reliable people you "
        "will ever meet. Oxen can be stubborn and resistant to change, but this same quality "
        "gives them the resolve to see long, difficult projects through to completion when "
        "others have long since given up."
    ),
    ChineseAnimal.TIGER: (
        "The Tiger is bold, passionate, and fiercely independent — a natural leader who "
        "commands respect without asking for it. Born risk-takers, Tigers leap at challenges "
        "that would make others hesitate, driven by an intense competitive spirit and an "
        "unwavering belief in themselves. They are generous and warm to those they love, but "
        "they can be unpredictable and hot-headed when crossed. At their best, Tigers are "
        "courageous protectors who fight for what they believe in; at their worst, they can "
        "be impulsive and difficult to pin down."
    ),
    ChineseAnimal.RABBIT: (
        "The Rabbit is graceful, gentle, and deeply attuned to beauty and harmony. Those born "
        "in the Year of the Rabbit have a natural elegance and a quiet intelligence that "
        "earns them respect without the need for bluster. They are empathetic and kind, "
        "skilled at easing tension in difficult situations and finding diplomatic solutions. "
        "Rabbits value peace and tend to avoid conflict whenever possible, which can sometimes "
        "read as indecisiveness. Beneath their soft exterior, however, lies a keen mind and "
        "a quiet resilience that helps them weather even the most turbulent of times."
    ),
    ChineseAnimal.DRAGON: (
        "The Dragon is the only mythical creature in the Chinese zodiac, and those born under "
        "its sign carry a legendary energy. Dragons are charismatic, ambitious, and utterly "
        "fearless — they set audacious goals and possess the drive and magnetism to achieve "
        "them. They are natural visionaries who inspire others simply by entering a room. "
        "Dragons can be demanding perfectionists and may struggle with arrogance, but their "
        "passion and generosity more than compensate. There is rarely a dull moment in the "
        "life of a Dragon, and even less so for those lucky enough to be close to one."
    ),
    ChineseAnimal.SNAKE: (
        "The Snake is the philosopher of the Chinese zodiac — wise, enigmatic, and deeply "
        "intuitive. Those born in the Year of the Snake tend to think before they speak, "
        "choosing their words with care and projecting a calm self-possession that others "
        "find both compelling and mysterious. They are highly perceptive, often reading "
        "situations and people with uncanny accuracy. Snakes have refined tastes and a love "
        "of beauty in all its forms. They can be private and even suspicious of those they "
        "don't know well, but once trust is established, they are devoted and deeply "
        "thoughtful companions."
    ),
    ChineseAnimal.HORSE: (
        "The Horse is spirited, energetic, and free — at their happiest when moving, exploring, "
        "and embracing the open road. Those born in the Year of the Horse are vivacious and "
        "charming, with a warm, generous nature that makes them popular wherever they go. "
        "They are hardworking and perceptive, with a quick mind that absorbs new ideas "
        "rapidly. Horses crave independence and can grow restless under too many constraints. "
        "Their impatience can lead to scattered energy if they are not careful, but when "
        "focused on something they truly love, their enthusiasm and stamina are extraordinary."
    ),
    ChineseAnimal.GOAT: (
        "The Goat — also known as the Ram or Sheep — is creative, gentle, and deeply "
        "compassionate. Those born under this sign have a rich inner life and a love of art, "
        "nature, and beauty that runs through everything they do. They are kind and empathetic, "
        "often putting others' needs before their own, and they thrive in nurturing, "
        "harmonious environments. Goats can be shy and prone to worry, preferring the comfort "
        "of trusted relationships to the uncertainty of new situations. But within their "
        "element, they bring a warmth and a quiet creativity that enriches the lives of "
        "everyone around them."
    ),
    ChineseAnimal.MONKEY: (
        "The Monkey is the trickster and genius of the Chinese zodiac — curious, inventive, "
        "and endlessly entertaining. Those born in the Year of the Monkey have quick, "
        "versatile minds that delight in solving complex problems and finding creative "
        "shortcuts. They are witty, sociable, and can adapt to almost any situation with "
        "apparent ease. Monkeys love a good challenge and have a mischievous streak that "
        "keeps life interesting for those around them. Though they can be seen as crafty or "
        "inconsistent, their cleverness and enthusiasm make them some of the most magnetic "
        "and stimulating people in any room."
    ),
    ChineseAnimal.ROOSTER: (
        "The Rooster is observant, hardworking, and remarkably self-assured. Those born in "
        "the Year of the Rooster take pride in their appearance and their work, holding "
        "themselves to high standards and expecting the same from others. They are honest — "
        "sometimes bluntly so — and have little patience for inefficiency or dishonesty. "
        "Roosters are highly organized and detail-oriented, making them excellent planners "
        "and administrators. Their confidence can tip into bossiness, but their courage, "
        "loyalty, and dedication to excellence make them invaluable in any endeavor they "
        "choose to pursue."
    ),
    ChineseAnimal.DOG: (
        "The Dog is the most loyal and trustworthy sign in the Chinese zodiac. Those born "
        "under this sign are honest, kind, and deeply devoted to the people they care about. "
        "They have a strong sense of justice and will speak up against wrongdoing even at "
        "personal cost — they simply cannot look the other way. Dogs can be anxious and "
        "prone to pessimism, often worrying about things beyond their control. But their "
        "reliability and warmth are unmatched: when you need someone in your corner without "
        "question or condition, you want a Dog by your side."
    ),
    ChineseAnimal.PIG: (
        "The Pig is generous, compassionate, and full of a genuine, uncomplicated joy for "
        "life. Those born in the Year of the Pig are warm-hearted and sincere, with an "
        "openness and trust in people that is as endearing as it is occasionally naive. They "
        "work hard and are remarkably diligent when pursuing goals they care about, with a "
        "patience and persistence that quietly earns results. Pigs love comfort, good food, "
        "and the company of people they love. Their big-heartedness and lack of pretension "
        "make them some of the most genuinely loveable people in the zodiac."
    ),
}

# Maps each animal to its trine group (1–4). Animals in the same trine share
# natural harmony; those in opposing trines often clash.
CHINESE_TRINES: dict[ChineseAnimal, int] = {
    ChineseAnimal.RAT: 1,
    ChineseAnimal.DRAGON: 1,
    ChineseAnimal.MONKEY: 1,
    ChineseAnimal.OX: 2,
    ChineseAnimal.SNAKE: 2,
    ChineseAnimal.ROOSTER: 2,
    ChineseAnimal.TIGER: 3,
    ChineseAnimal.HORSE: 3,
    ChineseAnimal.DOG: 3,
    ChineseAnimal.RABBIT: 4,
    ChineseAnimal.GOAT: 4,
    ChineseAnimal.PIG: 4,
}

# The six pairs that sit directly opposite each other on the zodiac wheel —
# traditionally considered the most challenging pairings.
CHINESE_OPPOSITES: set[frozenset[ChineseAnimal]] = {
    frozenset([ChineseAnimal.RAT, ChineseAnimal.HORSE]),
    frozenset([ChineseAnimal.OX, ChineseAnimal.GOAT]),
    frozenset([ChineseAnimal.TIGER, ChineseAnimal.MONKEY]),
    frozenset([ChineseAnimal.RABBIT, ChineseAnimal.ROOSTER]),
    frozenset([ChineseAnimal.DRAGON, ChineseAnimal.DOG]),
    frozenset([ChineseAnimal.SNAKE, ChineseAnimal.PIG]),
}


def _get_chinese_year(year: int, month: int, day: int) -> int:
    if year in _CNY_DATES:
        cny_month, cny_day = _CNY_DATES[year]
        if (month, day) < (cny_month, cny_day):
            return year - 1
    return year


def get_chinese_sign(
    year: int, month: int, day: int
) -> tuple[ChineseAnimal, ChineseElement, Polarity]:
    effective_year = _get_chinese_year(year, month, day)
    offset = effective_year - CYCLE_ANCHOR
    animal = _ANIMALS[offset % 12]
    element = _ELEMENTS[(offset % 10) // 2]
    polarity = Polarity.YANG if offset % 2 == 0 else Polarity.YIN
    return animal, element, polarity


def get_chinese_compatibility(animal1: ChineseAnimal, animal2: ChineseAnimal) -> str:
    if animal1 == animal2:
        return (
            f"Two {animal1.value}s share the same instincts, drives, and blind spots. "
            f"This pairing has a natural ease and deep mutual understanding — they rarely "
            f"need to explain themselves to each other. The risk is that they can reinforce "
            f"each other's weaknesses as readily as their strengths, so self-awareness is "
            f"key. At their best, this is a partnership built on genuine kinship and a "
            f"shared vision of the world."
        )

    if frozenset([animal1, animal2]) in CHINESE_OPPOSITES:
        return (
            f"The {animal1.value} and the {animal2.value} sit directly opposite each other "
            f"on the Chinese zodiac wheel, making this one of the most challenging pairings. "
            f"Their fundamental drives and values can pull in opposite directions, creating "
            f"tension that requires real effort to navigate. That said, opposites can "
            f"complement as much as they clash — if both are willing to learn from their "
            f"differences, this pairing can be profoundly transformative for both people."
        )

    trine1 = CHINESE_TRINES[animal1]
    trine2 = CHINESE_TRINES[animal2]

    if trine1 == trine2:
        return (
            f"The {animal1.value} and the {animal2.value} belong to the same trine, one of "
            f"the most auspicious pairings in the Chinese zodiac. They share a fundamental "
            f"compatibility in outlook, values, and approach to life that makes cooperation "
            f"feel natural and effortless. Conflict between them is rare, and when it does "
            f"arise, they tend to resolve it quickly. This is a pairing built on genuine "
            f"mutual respect and an easy, enduring harmony."
        )

    return (
        f"The {animal1.value} and the {animal2.value} come from different trines, bringing "
        f"distinct energies and perspectives to their relationship. There is no natural "
        f"friction between them, but also no automatic harmony — their connection is "
        f"something they build together through shared experience and mutual curiosity. "
        f"With openness and goodwill, this pairing can be richly rewarding, each person "
        f"broadening the other's world in ways neither could have managed alone."
    )
