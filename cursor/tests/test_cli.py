"""Tests for zodiac_calculator CLI."""

import io
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

import zodiac_calculator as cli
from zodiac.enums import EasternAnimal, WesternSign


def test_is_yes() -> None:
    assert cli.is_yes("y")
    assert cli.is_yes("Y")
    assert cli.is_yes("yes")
    assert cli.is_yes(" YES ")
    assert not cli.is_yes("n")
    assert not cli.is_yes("no")


def test_print_sign_results(capsys) -> None:
    cli.print_sign_results(WesternSign.ARIES, EasternAnimal.HORSE)
    captured = capsys.readouterr()
    assert "Western sign: Aries" in captured.out
    assert "Eastern sign: Horse" in captured.out
    assert "bold, energetic" in captured.out
    assert "free-spirited" in captured.out


def test_print_compatibility_results(capsys) -> None:
    cli.print_compatibility_results(
        WesternSign.ARIES,
        WesternSign.LEO,
        EasternAnimal.RAT,
        EasternAnimal.HORSE,
    )
    captured = capsys.readouterr()
    assert "Western (Aries + Leo): Compatible" in captured.out
    assert "Eastern (Rat + Horse): Challenging" in captured.out


def test_prompt_birthdate_flushes_before_read() -> None:
    inp = io.StringIO("3/21/1990\n")
    out = io.StringIO()
    with patch.object(out, "flush") as mock_flush:
        cli.prompt_birthdate(inp, out)
        mock_flush.assert_called()


def test_prompt_birthdate_valid() -> None:
    inp = io.StringIO("3/21/1990\n")
    out = io.StringIO()
    assert cli.prompt_birthdate(inp, out) == (1990, 3, 21)


def test_prompt_birthdate_retries_on_invalid() -> None:
    inp = io.StringIO("bad\n3/21/1990\n")
    out = io.StringIO()
    assert cli.prompt_birthdate(inp, out) == (1990, 3, 21)
    assert "Error:" in out.getvalue()


def test_prompt_birthdate_eof() -> None:
    inp = io.StringIO("")
    out = io.StringIO()
    with pytest.raises(EOFError):
        cli.prompt_birthdate(inp, out)


def test_run_calculator_single_lookup_then_quit() -> None:
    inp = io.StringIO("3/21/1990\nn\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    text = out.getvalue()
    assert cli.WELCOME_MESSAGE in text
    assert "Western sign: Aries" in text
    assert "Eastern sign: Horse" in text
    assert cli.EXIT_MESSAGE in text


def test_run_calculator_with_compatibility() -> None:
    inp = io.StringIO("3/21/1990\ny\n7/23/1990\nn\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    text = out.getvalue()
    assert "Western (Aries + Leo): Compatible" in text
    assert "Eastern (Horse + Horse):" in text


def test_run_calculator_invalid_then_valid() -> None:
    inp = io.StringIO("2/30/1990\n1/27/1990\nn\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    text = out.getvalue()
    assert "Error:" in text
    assert "Eastern sign: Horse" in text


def test_run_calculator_eof_exits_gracefully() -> None:
    inp = io.StringIO("")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_run_calculator_keyboard_interrupt() -> None:
    class InterruptOnRead(io.StringIO):
        def readline(self, size: int = -1) -> str:
            raise KeyboardInterrupt

    inp = InterruptOnRead("")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_run_calculator_compat_invalid_then_valid() -> None:
    inp = io.StringIO("3/21/1990\ny\nbad\n7/23/1990\nn\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    text = out.getvalue()
    assert "Error:" in text
    assert "Western (Aries + Leo): Compatible" in text


def test_run_calculator_compat_prompt_eof() -> None:
    inp = io.StringIO("3/21/1990\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_run_calculator_compat_prompt_keyboard_interrupt() -> None:
    class CompatPromptInterrupt(io.StringIO):
        def readline(self, size: int = -1) -> str:
            if not hasattr(self, "_calls"):
                self._calls = 0
            self._calls += 1
            if self._calls == 1:
                return "3/21/1990\n"
            raise KeyboardInterrupt

    inp = CompatPromptInterrupt("")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_run_calculator_calculate_another_yes() -> None:
    inp = io.StringIO("3/21/1990\nn\ny\n1/1/2000\nn\nn\n")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    text = out.getvalue()
    assert text.count("Western sign:") == 2
    assert "Capricorn" in text


def test_run_calculator_outer_keyboard_interrupt() -> None:
    with patch("zodiac_calculator.print_sign_results", side_effect=KeyboardInterrupt):
        inp = io.StringIO("3/21/1990\n")
        out = io.StringIO()
        cli.run_calculator(inp, out)
        assert cli.EXIT_MESSAGE in out.getvalue()


def test_main_delegates_to_run_calculator() -> None:
    with patch("zodiac_calculator.run_calculator") as mock_run:
        cli.main()
        mock_run.assert_called_once()


def test_run_calculator_compat_keyboard_interrupt() -> None:
    class CompatInterrupt(io.StringIO):
        def readline(self, size: int = -1) -> str:
            if not hasattr(self, "_calls"):
                self._calls = 0
            self._calls += 1
            if self._calls == 1:
                return "3/21/1990\n"
            if self._calls == 2:
                return "y\n"
            raise KeyboardInterrupt

    inp = CompatInterrupt("")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_run_calculator_another_keyboard_interrupt() -> None:
    class AnotherInterrupt(io.StringIO):
        def readline(self, size: int = -1) -> str:
            if not hasattr(self, "_calls"):
                self._calls = 0
            self._calls += 1
            if self._calls == 1:
                return "3/21/1990\n"
            if self._calls == 2:
                return "n\n"
            raise KeyboardInterrupt

    inp = AnotherInterrupt("")
    out = io.StringIO()
    cli.run_calculator(inp, out)
    assert cli.EXIT_MESSAGE in out.getvalue()


def test_main_entry_point() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "zodiac_calculator.py"],
        input="3/21/1990\nn\n",
        text=True,
        capture_output=True,
        cwd=root,
        check=False,
    )
    assert result.returncode == 0
    assert "Welcome to the Zodiac Calculator!" in result.stdout


def test_prompt_birthdate_keyboard_interrupt() -> None:
    class InterruptOnRead(io.StringIO):
        def readline(self, size: int = -1) -> str:
            raise KeyboardInterrupt

    inp = InterruptOnRead("")
    out = io.StringIO()
    with pytest.raises(KeyboardInterrupt):
        cli.prompt_birthdate(inp, out)
