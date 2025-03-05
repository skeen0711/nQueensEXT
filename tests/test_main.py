import io
import sys
import time
from src.main import solve_n_queens

def capture_stdout(function, *args, **kwargs):
    captured_output = io.StringIO()
    sys.stdout = captured_output
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()
    sys.stdout = sys.__stdout__
    execution_time = end_time - start_time
    return captured_output.getvalue(), execution_time

def test_n_queens_1():
    captured, exec_time = capture_stdout(solve_n_queens, 1)
    print(f"n=1 execution time: {exec_time:.4f} seconds")
    assert "Found 1 solutions:" in captured
    assert "Q" in captured

def test_n_queens_2():
    captured, exec_time = capture_stdout(solve_n_queens, 2)
    print(f"n=2 execution time: {exec_time:.4f} seconds")
    assert "No solutions found." in captured

def test_n_queens_3():
    captured, exec_time = capture_stdout(solve_n_queens, 3)
    print(f"n=3 execution time: {exec_time:.4f} seconds")
    assert "No solutions found." in captured

def test_n_queens_4():
    captured, exec_time = capture_stdout(solve_n_queens, 4)
    print(f"n=4 execution time: {exec_time:.4f} seconds")
    assert "Found 2 solutions:" in captured
    assert "Q . . ." in captured
    assert ". . Q ." in captured
    assert ". . . Q" in captured
    assert ". Q . ." in captured

def test_n_queens_5():
    captured, exec_time = capture_stdout(solve_n_queens, 5)
    print(f"n=5 execution time: {exec_time:.4f} seconds")
    assert "Found 10 solutions:" in captured
    # Check one specific solution
    assert "Q . . . ." in captured
    assert ". . Q . ." in captured
    assert ". . . . Q" in captured
    assert ". Q . . ." in captured
    assert ". . . Q ." in captured

def test_n_queens_6():
    captured, exec_time = capture_stdout(solve_n_queens, 6)
    print(f"n=6 execution time: {exec_time:.4f} seconds")
    assert "Found 4 solutions:" in captured
    # Check one specific solution
    assert "Q . . . . ." in captured
    assert ". . . Q . ." in captured
    assert ". Q . . . ." in captured
    assert ". . . . Q ." in captured
    assert ". . Q . . ." in captured
    assert ". . . . . Q" in captured

def test_n_queens_7():
    captured, exec_time = capture_stdout(solve_n_queens, 7)
    print(f"n=7 execution time: {exec_time:.4f} seconds")
    assert "Found 40 solutions:" in captured
    # Check one specific solution
    assert "Q . . . . . ." in captured
    assert ". . Q . . . ." in captured
    assert ". . . . Q . ." in captured
    assert ". . . . . . Q" in captured
    assert ". Q . . . . ." in captured
    assert ". . . Q . . ." in captured
    assert ". . . . . Q ." in captured

def test_n_queens_8():
    captured, exec_time = capture_stdout(solve_n_queens, 8)
    print(f"n=8 execution time: {exec_time:.4f} seconds")
    assert "Found 92 solutions:" in captured
    # Check one specific solution (the first one typically generated)
    assert "Q . . . . . . ." in captured
    assert ". . . . Q . . ." in captured
    assert ". Q . . . . . ." in captured
    assert ". . . . . Q . ." in captured
    assert ". . Q . . . . ." in captured
    assert ". . . . . . Q ." in captured
    assert ". . . Q . . . ." in captured
    assert ". . . . . . . Q" in captured

def test_n_queens_10():
    captured, exec_time = capture_stdout(solve_n_queens, 10)
    print(f"n=10 execution time: {exec_time:.4f} seconds")
    assert "Found 724 solutions:" in captured
    # Check one specific solution (a common first solution for N=10)
    assert "Q . . . . . . . . ." in captured
    assert ". . . . . Q . . . ." in captured
    assert ". Q . . . . . . . ." in captured
    assert ". . . . . . . Q . ." in captured
    assert ". . Q . . . . . . ." in captured
    assert ". . . . . . . . Q ." in captured
    assert ". . . Q . . . . . ." in captured
    assert ". . . . . . Q . . ." in captured
    assert ". . . . Q . . . . ." in captured
    assert ". . . . . . . . . Q" in captured

def test_n_queens_12():
    captured, exec_time = capture_stdout(solve_n_queens, 12)
    print(f"n=12 execution time: {exec_time:.4f} seconds")
    assert "Found 14200 solutions:" in captured
    # For large N, just check that output contains boards with queens
    assert "Q" in captured
    assert "." in captured

# Heavy load test, particularly to test effect of parallelization on efficiency
#
# def test_n_queens_15():
#     captured, exec_time = capture_stdout(solve_n_queens, 15)
#     print(f"n=15 execution time: {exec_time:.4f} seconds")
#     assert "Found 2279184 solutions:" in captured
#     # For very large N, verify queens and empty spaces exist in output
#     assert "Q" in captured
#     assert "." in captured

# tests/test_main.py n=1 execution time: 0.0000 seconds
# .n=2 execution time: 0.0000 seconds
# .n=3 execution time: 0.0000 seconds
# .n=4 execution time: 0.0000 seconds
# .n=5 execution time: 0.0003 seconds
# .n=6 execution time: 0.0003 seconds
# .n=7 execution time: 0.0015 seconds
# .n=8 execution time: 0.0084 seconds
# .n=10 execution time: 0.1668 seconds
# .n=12 execution time: 5.4035 seconds
# .^C
#
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! KeyboardInterrupt !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# /Users/user/PycharmProjects/nQueensExt/src/main.py:28: KeyboardInterrupt
# (to show a full traceback on KeyboardInterrupt use --full-trace)
# ================================================================= 10 passed in 552.67s (0:09:12) =================================================================