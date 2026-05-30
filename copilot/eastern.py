"""Eastern (Chinese) zodiac calculations"""
# Use 1900 as reference year -> Rat
_ANIMALS = [
    ("Rat", "🐀", "Quick-witted, resourceful"),
    ("Ox", "🐂", "Strong, reliable"),
    ("Tiger", "🐅", "Brave, confident"),
    ("Rabbit", "🐇", "Quiet, elegant"),
    ("Dragon", "🐉", "Confident, intelligent"),
    ("Snake", "🐍", "Enigmatic, wise"),
    ("Horse", "🐎", "Energetic, independent"),
    ("Goat", "🐐", "Calm, gentle"),
    ("Monkey", "🐒", "Witty, curious"),
    ("Rooster", "🐓", "Observant, hardworking"),
    ("Dog", "🐕", "Loyal, honest"),
    ("Pig", "🐖", "Generous, diligent"),
]


def get_eastern_sign(d):
    """Return a dict with keys: name, emoji, desc
    Calculation based on birth year. Always returns a single animal.
    """
    year = d.year
    idx = (year - 1900) % 12
    name, emoji, desc = _ANIMALS[idx]
    return {"name": name, "emoji": emoji, "desc": desc}


def format_eastern(sign: dict) -> str:
    """Format an eastern sign dict for CLI output."""
    return f"{sign['emoji']} {sign['name']} — {sign['desc']}"
