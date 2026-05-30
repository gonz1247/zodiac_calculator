"""Zodiac Calculator CLI (renamed from cli.py)
Usage: python zodiac_calculator.py M/D/YYYY [--system both|western|eastern]
"""
import argparse
import sys
from parsers import parse_date
from western import get_western_sign, format_western
from eastern import get_eastern_sign, format_eastern


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description="Zodiac Calculator: print Western and Eastern zodiac for a birthdate")
    parser.add_argument("birthdate", help="Birthdate in M/D/YYYY format, e.g. 3/21/1990")
    parser.add_argument("--system", choices=("both", "western", "eastern"), default="both", help="Which zodiac system to show")
    args = parser.parse_args(argv)

    try:
        dob = parse_date(args.birthdate)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    outputs = []
    if args.system in ("both", "western"):
        w = get_western_sign(dob)
        outputs.append(format_western(w))
    if args.system in ("both", "eastern"):
        e = get_eastern_sign(dob)
        outputs.append(format_eastern(e))

    out_text = "\n".join(outputs)
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        sys.stdout.buffer.write((out_text + "\n").encode(enc, errors="replace"))
    except Exception:
        print(out_text.encode(enc, errors="replace").decode(enc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
