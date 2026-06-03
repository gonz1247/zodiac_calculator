from enum import Enum


class WesternSign(Enum):
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


class WesternElement(Enum):
    FIRE = "Fire"
    EARTH = "Earth"
    AIR = "Air"
    WATER = "Water"


# (sign, end_month, end_day) ordered Jan→Dec. A date belongs to the first entry
# whose (end_month, end_day) >= (month, day). Capricorn wraps: Dec 22+ falls
# through to the default return at the bottom.
_SIGN_CUTOFFS: list[tuple[WesternSign, int, int]] = [
    (WesternSign.CAPRICORN, 1, 19),
    (WesternSign.AQUARIUS, 2, 18),
    (WesternSign.PISCES, 3, 20),
    (WesternSign.ARIES, 4, 19),
    (WesternSign.TAURUS, 5, 20),
    (WesternSign.GEMINI, 6, 20),
    (WesternSign.CANCER, 7, 22),
    (WesternSign.LEO, 8, 22),
    (WesternSign.VIRGO, 9, 22),
    (WesternSign.LIBRA, 10, 22),
    (WesternSign.SCORPIO, 11, 21),
    (WesternSign.SAGITTARIUS, 12, 21),
]

WESTERN_ELEMENT: dict[WesternSign, WesternElement] = {
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

WESTERN_DESCRIPTIONS: dict[WesternSign, str] = {
    WesternSign.ARIES: (
        "Aries is the first sign of the zodiac, ruled by Mars and bursting with energy, "
        "courage, and a pioneering spirit. Rams are natural leaders who dive headfirst into "
        "new challenges with infectious enthusiasm. Their directness can come across as "
        "impulsive, but it stems from a genuine desire to get things moving. Aries thrives "
        "in competitive environments and is at their best when given room to take initiative "
        "and pursue bold goals on their own terms."
    ),
    WesternSign.TAURUS: (
        "Taurus is an earth sign ruled by Venus, embodying patience, reliability, and a deep "
        "appreciation for the finer things in life. Bulls are grounded and dependable, often "
        "serving as a stabilizing force for those around them. They have a strong aesthetic "
        "sense and a love of comfort, whether in food, art, or nature. Their famous "
        "stubbornness is simply perseverance in disguise — once a Taurus commits to something, "
        "they see it through with unwavering determination."
    ),
    WesternSign.GEMINI: (
        "Gemini is an air sign ruled by Mercury, the planet of communication, making Geminis "
        "among the most quick-witted and versatile people of the zodiac. Represented by the "
        "Twins, they possess a dual nature that allows them to see multiple sides of any "
        "situation. Geminis are social, curious, and endlessly adaptable — they thrive in "
        "environments that keep their minds stimulated and hate being bored. Their gift for "
        "language makes them excellent storytellers, writers, and conversationalists."
    ),
    WesternSign.CANCER: (
        "Cancer is a water sign ruled by the Moon, giving Cancers a deep emotional intelligence "
        "and a powerful instinct to nurture. The Crab's hard shell protects a surprisingly "
        "tender interior — once you earn their trust, their loyalty and care are unmatched. "
        "Cancers are highly intuitive, often sensing the emotional undercurrents in any room. "
        "They are fiercely protective of family and home, drawing strength from secure "
        "relationships and the comfort of familiar surroundings."
    ),
    WesternSign.LEO: (
        "Leo is a fire sign ruled by the Sun, radiating warmth, confidence, and a magnetic "
        "charisma that draws people in. Lions have a natural flair for the dramatic and love "
        "to express themselves creatively. They are generous, loyal, and fiercely protective "
        "of the people they love. While they enjoy being in the spotlight, Leos are also "
        "capable leaders who genuinely want those around them to succeed — their enthusiasm "
        "and pride are infectious, lifting the spirits of everyone in their orbit."
    ),
    WesternSign.VIRGO: (
        "Virgo is an earth sign ruled by Mercury, combining sharp analytical thinking with a "
        "deep desire to be of service. Virgos have a keen eye for detail and an innate talent "
        "for organization, making them invaluable in any project requiring precision. They "
        "hold themselves to high standards and can be self-critical, but this perfectionism "
        "comes from a sincere wish to do things well. Beneath their practical exterior is a "
        "genuinely caring and thoughtful person who expresses love through acts of service."
    ),
    WesternSign.LIBRA: (
        "Libra is an air sign ruled by Venus, making Libras natural diplomats who seek balance, "
        "fairness, and harmony in all things. Represented by the Scales, they have an innate "
        "sense of justice and are skilled at seeing all sides of an argument — sometimes to "
        "the point of indecision. Libras are charming, socially graceful, and have a refined "
        "aesthetic sensibility. They thrive in partnership and are at their happiest when "
        "surrounded by beauty, intellectual conversation, and people who share their values."
    ),
    WesternSign.SCORPIO: (
        "Scorpio is a water sign ruled by Mars and Pluto, giving Scorpios a depth and intensity "
        "that few other signs can match. They are passionate, perceptive, and fiercely "
        "determined, with an almost magnetic ability to read people and situations. Scorpios "
        "feel everything deeply and guard their inner world carefully — trust must be earned "
        "slowly, but once given, it is absolute. They are drawn to mystery and transformation, "
        "often emerging from life's difficulties fundamentally changed and stronger for it."
    ),
    WesternSign.SAGITTARIUS: (
        "Sagittarius is a fire sign ruled by Jupiter, the planet of expansion and good fortune. "
        "Archers are eternal optimists with a philosophical mind and an insatiable appetite "
        "for adventure, knowledge, and freedom. They are honest to a fault — sometimes "
        "bluntly so — and believe strongly in speaking their truth. Sagittarians are happiest "
        "when exploring new horizons, whether through travel, education, or big ideas. Their "
        "enthusiasm is contagious, and their broad worldview makes them inspiring companions."
    ),
    WesternSign.CAPRICORN: (
        "Capricorn is an earth sign ruled by Saturn, the planet of discipline and structure. "
        "Capricorns are ambitious, hardworking, and possess a long-game mentality that few "
        "signs can rival. They set high goals and pursue them with quiet, steady determination, "
        "earning respect through their reliability and competence. Beneath their serious "
        "exterior lies a dry wit and a deep sense of loyalty to those they love. Capricorns "
        "understand that lasting success is built slowly, and they are more than willing to "
        "put in the work to get there."
    ),
    WesternSign.AQUARIUS: (
        "Aquarius is an air sign ruled by Uranus, the planet of innovation, making Aquarians "
        "the visionaries of the zodiac. They are independent, intellectual, and deeply "
        "humanitarian, often driven by a desire to improve the world rather than just their "
        "own circumstances. Aquarians march to their own beat and resist conformity, which "
        "can make them seem eccentric, but their originality is one of their greatest strengths. "
        "They are loyal friends who value ideas and progressive thinking above all else."
    ),
    WesternSign.PISCES: (
        "Pisces is a water sign ruled by Neptune, the planet of dreams and intuition. Pisceans "
        "are among the most empathetic and imaginative souls in the zodiac, with a natural "
        "ability to absorb the feelings of those around them. They are creative, compassionate, "
        "and deeply spiritual, often blurring the line between the real and the imagined. "
        "Pisces at their best are selfless and wise, offering a gentle, understanding presence "
        "that makes others feel deeply seen. Their sensitivity is their superpower — and "
        "their greatest challenge."
    ),
}

# Fire+Air and Earth+Water are naturally complementary element pairings.
_COMPLEMENTARY_PAIRS: frozenset[frozenset[WesternElement]] = frozenset(
    [
        frozenset([WesternElement.FIRE, WesternElement.AIR]),
        frozenset([WesternElement.EARTH, WesternElement.WATER]),
    ]
)


def get_western_sign(month: int, day: int) -> WesternSign:
    for sign, end_month, end_day in _SIGN_CUTOFFS:
        if (month, day) <= (end_month, end_day):
            return sign
    return WesternSign.CAPRICORN


def get_western_compatibility(sign1: WesternSign, sign2: WesternSign) -> str:
    elem1 = WESTERN_ELEMENT[sign1]
    elem2 = WESTERN_ELEMENT[sign2]

    if elem1 == elem2:
        return (
            f"{sign1.value} and {sign2.value} share the {elem1.value} element, creating a "
            f"natural understanding between them. They instinctively relate to each other's "
            f"motivations and communication styles, which makes for an easy, comfortable "
            f"connection. The challenge is that their similarities can also amplify each "
            f"other's weaknesses — but their shared values give them a strong foundation."
        )

    if frozenset([elem1, elem2]) in _COMPLEMENTARY_PAIRS:
        return (
            f"{sign1.value} ({elem1.value}) and {sign2.value} ({elem2.value}) belong to "
            f"complementary elements that naturally balance each other. Where one leads with "
            f"instinct, the other provides grounding — their differences are a source of "
            f"strength rather than friction. This pairing often produces a dynamic, "
            f"well-rounded partnership where each person fills in what the other lacks."
        )

    return (
        f"{sign1.value} ({elem1.value}) and {sign2.value} ({elem2.value}) come from elements "
        f"that require conscious effort to harmonize. Their approaches to life can feel "
        f"fundamentally different at first, creating friction but also the potential for "
        f"genuine growth. With patience and a willingness to understand each other's "
        f"perspectives, this pairing can build a relationship that broadens both of them."
    )
