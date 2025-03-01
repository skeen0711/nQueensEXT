import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # add parent directory to path

from main import solve_n_queens
import io

def capture_stdout(function, *args, **kwargs):
    """Captures stdout from a function."""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    function(*args, **kwargs)
    sys.stdout = sys.__stdout__  # reset stdout
    return captured_output.getvalue()

def test_n_queens_4():
    captured = capture_stdout(solve_n_queens, 4)
    assert "Founde 2 solutions:" in captured
    assert "Q . . ." in captured
    assert ". . Q ." in captured
    assert ". . . Q" in captured
    assert ". Q . ." in captured

def test_n_queens_1():
    captured = capture_stdout(solve_n_queens, 1)
    assert "Founde 1 solutions:" in captured
    assert "Q" in captured

def test_n_queens_2():
    captured = capture_stdout(solve_n_queens, 2)
    assert "No solutions found." in captured

def test_n_queens_3():
    captured = capture_stdout(solve_n_queens, 3)
    assert "No solutions found." in captured