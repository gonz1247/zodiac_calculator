import re
from datetime import date

from zodiac.chinese import (
    ChineseAnimal,
    ChineseElement,
    Polarity,
    CHINESE_DESCRIPTIONS,
    get_chinese_compatibility,
    get_chinese_sign,
)
from zodiac.western import (
    WesternSign,
    WESTERN_DESCRIPTIONS,
    get_western_compatibility,
    get_western_sign,
)


def parse_date(date_str: str) -> tuple[int, int, int] | None:
    m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", date_str)
    if m:
        year, month, day = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", date_str)
        if m:
            month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
        else:
            return None

    try:
        date(year, month, day)
    except ValueError:
        return None

    return year, month, day


def display_western(sign: WesternSign) -> None:
    print(f"\n--- Western Zodiac: {sign.value} ---")
    print(WESTERN_DESCRIPTIONS[sign])


def display_chinese(
    animal: ChineseAnimal, element: ChineseElement, polarity: Polarity
) -> None:
    label = f"{polarity.value} {element.value} {animal.value}"
    print(f"\n--- Chinese Zodiac: {label} ---")
    print(CHINESE_DESCRIPTIONS[animal])


def display_western_compatibility(sign1: WesternSign, sign2: WesternSign) -> None:
    print(f"\n--- Western Compatibility (comparing with: {sign2.value}) ---")
    print(get_western_compatibility(sign1, sign2))


def display_chinese_compatibility(
    animal1: ChineseAnimal,
    animal2: ChineseAnimal,
    element2: ChineseElement,
    polarity2: Polarity,
) -> None:
    label2 = f"{polarity2.value} {element2.value} {animal2.value}"
    print(f"\n--- Chinese Compatibility (comparing with: {label2}) ---")
    print(get_chinese_compatibility(animal1, animal2))


def run_loop() -> None:
    print("=== Zodiac Calculator ===")
    print("Discover your Western and Chinese zodiac signs.")

    while True:
        print()
        date_str = input(
            "Enter a birthdate (YYYY-MM-DD or MM/DD/YYYY), or 'q' to quit: "
        ).strip()

        if date_str.lower() in ("q", "quit"):
            print("Goodbye!")
            break

        parsed = parse_date(date_str)
        if parsed is None:
            print("Invalid date. Please use YYYY-MM-DD or MM/DD/YYYY.")
            continue

        year, month, day = parsed

        sign = get_western_sign(month, day)
        display_western(sign)

        animal, element, polarity = get_chinese_sign(year, month, day)
        display_chinese(animal, element, polarity)

        answer = (
            input("\nCheck compatibility with another person? (y/n): ").strip().lower()
        )
        if answer == "y":
            while True:
                date_str2 = input(
                    "Enter their birthdate (YYYY-MM-DD or MM/DD/YYYY): "
                ).strip()
                parsed2 = parse_date(date_str2)
                if parsed2 is None:
                    print("Invalid date. Please use YYYY-MM-DD or MM/DD/YYYY.")
                    continue
                year2, month2, day2 = parsed2
                sign2 = get_western_sign(month2, day2)
                animal2, element2, polarity2 = get_chinese_sign(year2, month2, day2)
                display_western_compatibility(sign, sign2)
                display_chinese_compatibility(animal, animal2, element2, polarity2)
                break


if __name__ == "__main__":  # pragma: no cover
    run_loop()
