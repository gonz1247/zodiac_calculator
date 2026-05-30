import subprocess
import sys


def run_cli(args):
    cmd = [sys.executable, "zodiac_calculator.py"] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def test_cli_both():
    result = run_cli(["3/21/1990"])
    assert "Aries" in result.stdout
    assert "Horse" in result.stdout
    assert result.returncode == 0


def test_cli_western():
    result = run_cli(["3/21/1990", "--system", "western"])
    assert "Aries" in result.stdout
    assert "Horse" not in result.stdout
    assert result.returncode == 0


def test_cli_eastern():
    result = run_cli(["3/21/1990", "--system", "eastern"])
    assert "Aries" not in result.stdout
    assert "Horse" in result.stdout
    assert result.returncode == 0


def test_cli_invalid():
    result = run_cli(["2/30/2021"])
    assert "Error:" in result.stderr
    assert result.returncode == 2
