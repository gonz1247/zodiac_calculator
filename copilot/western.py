"""Western (tropical) zodiac calculations"""
from datetime import date

# Each entry is (start_month, start_day, name, emoji, short_desc, range_str)
_ZODIAC = [
    (1, 20, "Aquarius", "♒", "The Water Bearer", "Jan 20–Feb 18"),
    (2, 19, "Pisces", "♓", "The Fish", "Feb 19–Mar 20"),
    (3, 21, "Aries", "♈", "The Ram", "Mar 21–Apr 19"),
    (4, 20, "Taurus", "♉", "The Bull", "Apr 20–May 20"),
    (5, 21, "Gemini", "♊", "The Twins", "May 21–Jun 20"),
    (6, 21, "Cancer", "♋", "The Crab", "Jun 21–Jul 22"),
    (7, 23, "Leo", "♌", "The Lion", "Jul 23–Aug 22"),
    (8, 23, "Virgo", "♍", "The Maiden", "Aug 23–Sep 22"),
    (9, 23, "Libra", "♎", "The Scales", "Sep 23–Oct 22"),
    (10, 23, "Scorpio", "♏", "The Scorpion", "Oct 23–Nov 21"),
    (11, 22, "Sagittarius", "♐", "The Archer", "Nov 22–Dec 21"),
    (12, 22, "Capricorn", "♑", "The Goat", "Dec 22–Jan 19"),
]


def get_western_sign(d: date) -> dict:
    """Return a dict with keys: name, emoji, desc, range
    Picks a single sign for the given date. Year-aware only in that the provided
    date is a full date (useful for Feb 29 validation upstream).
    """
    mday = (d.month, d.day)
    # Find the last zodiac with start <= mday, else Capricorn
    chosen = None
    for start_m, start_d, name, emoji, desc, rangestr in _ZODIAC:
        if mday >= (start_m, start_d):
            chosen = (name, emoji, desc, rangestr)
    if chosen is None:
        # before Jan 20 -> Capricorn
        name, emoji, desc, rangestr = _ZODIAC[-1][2:]
        return {"name": name, "emoji": emoji, "desc": desc, "range": rangestr}
    name, emoji, desc, rangestr = chosen
    return {"name": name, "emoji": emoji, "desc": desc, "range": rangestr}


def format_western(sign: dict) -> str:
    """Format a western sign dict for CLI output."""
    return f"{sign['emoji']} {sign['name']} — {sign['range']}: {sign['desc']}"
