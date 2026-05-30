"""Zodiac Calculator CLI (renamed from cli.py)
Usage: python zodiac_calculator.py M/D/YYYY [--system both|western|eastern]
"""
import sys
from parsers import parse_date
from western import get_western_sign, format_western
from eastern import get_eastern_sign, format_eastern


def run_once(birthdate_str: str, system: str = "both"):
    """Process a single birthdate string and return (rc, out_text, err_text).

    rc: 0 on success, 2 on input parse error.
    out_text: formatted result lines (Western then Eastern when applicable)
    err_text: error message on failure (empty on success)
    """
    try:
        dob = parse_date(birthdate_str)
    except ValueError as e:
        return 2, "", str(e)

    outputs = []
    if system in ("both", "western"):
        w = get_western_sign(dob)
        outputs.append(format_western(w))
    if system in ("both", "eastern"):
        e = get_eastern_sign(dob)
        outputs.append(format_eastern(e))
    out_text = "\n".join(outputs)
    return 0, out_text, ""


def main(argv=None):
    """Interactive loop when run as a terminal program.

    If argv is provided (list), it is ignored — this program is interactive-only.
    """
    # Interactive loop
    try:
        while True:
            try:
                user_in = input("Enter birthdate (M/D/YYYY) or 'q' to quit: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            if not user_in:
                continue
            if user_in.lower() in ("q", "quit"):
                print("Goodbye!")
                return 0

            rc, out_text, err = run_once(user_in)
            if rc != 0:
                print(f"Error: {err}", file=sys.stderr)
                continue

            # write using stream encoding with replacement for unsupported characters
            enc = getattr(sys.stdout, "encoding", None) or "utf-8"
            try:
                sys.stdout.buffer.write((out_text + "\n").encode(enc, errors="replace"))
            except Exception:
                print(out_text.encode(enc, errors="replace").decode(enc))
            # loop for next input
    except Exception:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
