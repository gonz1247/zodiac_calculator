import zodiac_calculator


def test_cli_both(capsys):
    rc = zodiac_calculator.main(["3/21/1990"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Aries" in captured.out
    assert "Horse" in captured.out


def test_cli_western(capsys):
    rc = zodiac_calculator.main(["3/21/1990", "--system", "western"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Aries" in captured.out
    assert "Horse" not in captured.out


def test_cli_eastern(capsys):
    rc = zodiac_calculator.main(["3/21/1990", "--system", "eastern"])
    assert rc == 0
    captured = capsys.readouterr()
    assert "Horse" in captured.out
    assert "Aries" not in captured.out


def test_cli_invalid(capsys):
    rc = zodiac_calculator.main(["2/30/2021"])
    assert rc == 2
    captured = capsys.readouterr()
    assert "Error:" in captured.err


def test_stdout_buffer_write_fallback(monkeypatch):
    import sys
    # Dummy buffer that raises on write
    class DummyBuf:
        def write(self, b):
            raise Exception("boom")
    # Dummy stdout that captures writes
    class DummyStdout:
        def __init__(self):
            self.encoding = 'utf-8'
            self.buffer = DummyBuf()
            self.output = ''
        def write(self, s):
            self.output += s
        def flush(self):
            pass
    dummy = DummyStdout()
    # Monkeypatch the real sys.stdout temporarily
    monkeypatch.setattr(__import__('sys'), 'stdout', dummy)
    rc = zodiac_calculator.main(["3/21/1990"])
    assert rc == 0
    # call flush to exercise the flush() stub
    dummy.flush()
    # The fallback print should have written to our dummy
    assert "Aries" in dummy.output
    assert "Horse" in dummy.output


def test_module_main_runs_as_script(monkeypatch):
    import sys, runpy
    # Ensure sys.argv provides an argument when module runs
    monkeypatch.setattr(__import__('sys'), 'argv', ['zodiac_calculator.py', '3/21/1990'])
    import pytest
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    assert exc.value.code == 0
