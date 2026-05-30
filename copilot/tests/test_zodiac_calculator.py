import zodiac_calculator


def test_run_once_both():
    rc, out, err = zodiac_calculator.run_once("3/21/1990")
    assert rc == 0
    assert "Aries" in out
    assert "Horse" in out


def test_run_once_western():
    rc, out, err = zodiac_calculator.run_once("3/21/1990", system="western")
    assert rc == 0
    assert "Aries" in out
    assert "Horse" not in out


def test_run_once_eastern():
    rc, out, err = zodiac_calculator.run_once("3/21/1990", system="eastern")
    assert rc == 0
    assert "Horse" in out
    assert "Aries" not in out


def test_run_once_invalid():
    rc, out, err = zodiac_calculator.run_once("2/30/2021")
    assert rc == 2
    assert "not" in err or "out of range" in err


def test_stdout_buffer_write_fallback(monkeypatch):
    import sys, runpy
    # Provide input sequence: birthday then quit
    inputs = ["3/21/1990", "q"]
    def fake_input(prompt=None):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', fake_input)

    # Monkeypatch stdout.buffer.write to raise to force fallback path
    class DummyBuf:
        def write(self, b):
            raise Exception("boom")
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
    monkeypatch.setattr('sys.stdout', dummy)

    import pytest
    import runpy
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    # module should exit with code 0
    assert exc.value.code == 0
    # fallback should have written to dummy.output
    assert "Aries" in dummy.output
    assert "Horse" in dummy.output


def test_module_main_runs_as_script(monkeypatch):
    import runpy
    # Simulate user input then quit
    inputs = ["3/21/1990", "q"]
    def fake_input(prompt=None):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', fake_input)

    import pytest
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    assert exc.value.code == 0


# Consolidated tests from test_interactive_branches.py

def test_empty_input_then_valid(monkeypatch):
    # Simulate: user presses enter (empty), then valid date, then quit
    inputs = ["", "3/21/1990", "q"]
    def fake_input(prompt=None):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', fake_input)

    class DummyStdout:
        def __init__(self):
            self.encoding = 'utf-8'
            self.buffer = self
            self.output = ''
        def write(self, b):
            try:
                self.output += b.decode('utf-8')
            except Exception:
                self.output += str(b)
        def flush(self):
            pass
    dummy_out = DummyStdout()
    monkeypatch.setattr('sys.stdout', dummy_out)

    class DummyStderr:
        def __init__(self):
            self.output = ''
        def write(self, s):
            self.output += str(s)
        def flush(self):
            pass
    dummy_err = DummyStderr()
    monkeypatch.setattr('sys.stderr', dummy_err)

    import pytest
    import runpy
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    assert exc.value.code == 0
    assert 'Aries' in dummy_out.output
    assert 'Horse' in dummy_out.output


def test_invalid_input_reprompts(monkeypatch):
    # Simulate invalid input then quit
    inputs = ["bad-date", "q"]
    def fake_input(prompt=None):
        return inputs.pop(0)
    monkeypatch.setattr('builtins.input', fake_input)

    class DummyStdout:
        def __init__(self):
            self.encoding = 'utf-8'
            self.buffer = self
            self.output = ''
        def write(self, b):
            try:
                self.output += b.decode('utf-8')
            except Exception:
                self.output += str(b)
        def flush(self):
            pass
    dummy_out = DummyStdout()
    monkeypatch.setattr('sys.stdout', dummy_out)

    class DummyStderr:
        def __init__(self):
            self.output = ''
        def write(self, s):
            self.output += str(s)
        def flush(self):
            pass
    dummy_err = DummyStderr()
    monkeypatch.setattr('sys.stderr', dummy_err)

    import pytest
    import runpy
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    assert exc.value.code == 0
    assert 'Error:' in dummy_err.output


def test_unhandled_exception_returns_1(monkeypatch):
    # Simulate input raising unexpected exception
    def bad_input(prompt=None):
        raise RuntimeError('boom')
    monkeypatch.setattr('builtins.input', bad_input)

    import pytest, runpy
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    # main should return 1 leading to SystemExit(1)
    assert exc.value.code == 1


def test_eof_exits_cleanly(monkeypatch):
    # Simulate EOFError to exercise the EOF/KeyboardInterrupt branch
    def eof_input(prompt=None):
        raise EOFError()
    monkeypatch.setattr('builtins.input', eof_input)

    import pytest, runpy
    with pytest.raises(SystemExit) as exc:
        runpy.run_module('zodiac_calculator', run_name='__main__')
    assert exc.value.code == 0
