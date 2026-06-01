#!/usr/bin/env python3
"""Interactive CLI for Western and Eastern zodiac signs."""

from __future__ import annotations

import sys
from typing import TextIO

from zodiac.compatibility import eastern_compatibility, western_compatibility
from zodiac.eastern import eastern_sign
from zodiac.enums import EasternAnimal, WesternSign
from zodiac.parsing import parse_birthdate
from zodiac.western import western_sign

WELCOME_MESSAGE = "Welcome to the Zodiac Calculator!"
EXIT_MESSAGE = "Goodbye!"
BIRTHDATE_PROMPT = "Enter birthdate (M/D/YYYY): "
COMPAT_PROMPT = "Check compatibility with another birthdate? (y/n): "
ANOTHER_PROMPT = "Calculate another? (y/n): "


def _write_prompt(output_stream: TextIO, prompt: str) -> None:
    """Write a prompt and flush so it appears before ``readline()`` waits."""
    print(prompt, end="", file=output_stream, flush=True)


def is_yes(response: str) -> bool:
    """Return True if the response means yes (y or yes, case-insensitive)."""
    return response.strip().lower() in {"y", "yes"}


def print_sign_results(
    western: WesternSign,
    eastern: EasternAnimal,
    *,
    output: TextIO | None = None,
) -> None:
    """Print Western and Eastern sign results with horoscope blurbs."""
    out = output or sys.stdout
    print(f"Western sign: {western.value}", file=out)
    print(f"  {western.horoscope}", file=out)
    print(f"Eastern sign: {eastern.value}", file=out)
    print(f"  {eastern.horoscope}", file=out)


def print_compatibility_results(
    sign_a: WesternSign,
    sign_b: WesternSign,
    animal_a: EasternAnimal,
    animal_b: EasternAnimal,
    *,
    output: TextIO | None = None,
) -> None:
    """Print sign pairs and compatibility on one line per zodiac system."""
    out = output or sys.stdout
    western_level = western_compatibility(sign_a, sign_b)
    eastern_level = eastern_compatibility(animal_a, animal_b)
    print(
        f"Western ({sign_a.value} + {sign_b.value}): {western_level.value}",
        file=out,
    )
    print(
        f"Eastern ({animal_a.value} + {animal_b.value}): {eastern_level.value}",
        file=out,
    )


def prompt_birthdate(
    input_stream: TextIO,
    output_stream: TextIO,
    prompt: str = BIRTHDATE_PROMPT,
) -> tuple[int, int, int]:
    """Prompt until a valid birthdate is entered.

    Returns
    -------
    tuple[int, int, int]
        Parsed ``(year, month, day)``.
    """
    while True:
        _write_prompt(output_stream, prompt)
        try:
            line = input_stream.readline()
        except KeyboardInterrupt:
            print(file=output_stream)
            raise

        if line == "":
            raise EOFError

        try:
            return parse_birthdate(line)
        except ValueError as exc:
            print(f"Error: {exc}", file=output_stream, flush=True)


def run_compatibility_subflow(
    sign_a: WesternSign,
    animal_a: EasternAnimal,
    input_stream: TextIO,
    output_stream: TextIO,
) -> None:
    """Prompt for a second birthdate and print compatibility results."""
    while True:
        try:
            year, month, day = prompt_birthdate(input_stream, output_stream)
        except (EOFError, KeyboardInterrupt):
            raise

        sign_b = western_sign(month, day)
        animal_b = eastern_sign(year, month, day)
        print_compatibility_results(
            sign_a, sign_b, animal_a, animal_b, output=output_stream
        )
        return


def run_calculator(
    input_stream: TextIO | None = None,
    output_stream: TextIO | None = None,
) -> None:
    """Run the interactive zodiac calculator loop."""
    inp = input_stream or sys.stdin
    out = output_stream or sys.stdout

    print(WELCOME_MESSAGE, file=out)

    try:
        while True:
            try:
                year, month, day = prompt_birthdate(inp, out)
            except (EOFError, KeyboardInterrupt):
                break

            western = western_sign(month, day)
            eastern = eastern_sign(year, month, day)
            print_sign_results(western, eastern, output=out)

            _write_prompt(out, COMPAT_PROMPT)
            try:
                compat_response = inp.readline()
            except KeyboardInterrupt:
                print(file=out)
                break

            if compat_response == "":
                break

            if is_yes(compat_response):
                try:
                    run_compatibility_subflow(western, eastern, inp, out)
                except (EOFError, KeyboardInterrupt):
                    break

            _write_prompt(out, ANOTHER_PROMPT)
            try:
                another_response = inp.readline()
            except KeyboardInterrupt:
                print(file=out)
                break

            if another_response == "" or not is_yes(another_response):
                break
    except KeyboardInterrupt:
        print(file=out)

    print(EXIT_MESSAGE, file=out)


def main() -> None:
    """Entry point for ``python zodiac_calculator.py``."""
    run_calculator()


if __name__ == "__main__":  # pragma: no cover
    main()
