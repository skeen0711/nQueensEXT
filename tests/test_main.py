import io
import sys
import time
from src.main import solve_n_queens, board_to_grid

def capture_solutions(function, n, preplaced=None):
    start_time = time.time()
    solutions = function(n, preplaced)
    end_time = time.time()
    execution_time = end_time - start_time
    grids = [board_to_grid(board, n) for board in solutions]
    return grids, execution_time

def test_n_queens_1():
    grids, exec_time = capture_solutions(solve_n_queens, 1)
    print(f"n=1 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 1
    assert grids[0] == [["Q"]]

def test_n_queens_2():
    grids, exec_time = capture_solutions(solve_n_queens, 2)
    print(f"n=2 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 0

def test_n_queens_3():
    grids, exec_time = capture_solutions(solve_n_queens, 3)
    print(f"n=3 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 0

def test_n_queens_4():
    grids, exec_time = capture_solutions(solve_n_queens, 4)
    assert len(grids) == 2
    assert grids[0] == [[".", "Q", ".", "."], [".", ".", ".", "Q"], ["Q", ".", ".", "."], [".", ".", "Q", "."]]

def test_n_queens_5():
    grids, exec_time = capture_solutions(solve_n_queens, 5)
    assert len(grids) == 10
    assert grids[0] == [["Q", ".", ".", ".", "."], [".", ".", "Q", ".", "."], [".", ".", ".", ".", "Q"], [".", "Q", ".", ".", "."], [".", ".", ".", "Q", "."]]

def test_n_queens_6():
    grids, exec_time = capture_solutions(solve_n_queens, 6)
    assert len(grids) == 4
    assert grids[0] == [[".", "Q", ".", ".", ".", "."], [".", ".", ".", "Q", ".", "."], [".", ".", ".", ".", "Q", "."], [".", ".", "Q", ".", ".", "."], ["Q", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "Q"]]

def test_n_queens_7():
    grids, exec_time = capture_solutions(solve_n_queens, 7)
    print(f"n=7 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 40

def test_n_queens_8():
    grids, exec_time = capture_solutions(solve_n_queens, 8)
    print(f"n=8 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 92

def test_n_queens_10():
    grids, exec_time = capture_solutions(solve_n_queens, 10)
    print(f"n=10 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 724

def test_n_queens_12():
    grids, exec_time = capture_solutions(solve_n_queens, 12)
    print(f"n=12 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 14200

def test_n_queens_13():
    grids, exec_time = capture_solutions(solve_n_queens, 13)
    print(f"n=13 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 73712

# Heavy load testing -- Use only for testing efficiency of Parallel routines
# def test_n_queens_15():
#     grids, exec_time = capture_solutions(solve_n_queens, 15)
#     print(f"n=15 execution time: {exec_time:.4f} seconds")
#     assert len(grids) == 2279184

def test_n_queens_5_preplaced():
    grids, exec_time = capture_solutions(solve_n_queens, 5, [(0, 1)])
    print(f"n=5 with preplaced (0,1) execution time: {exec_time:.4f} seconds")
    assert len(grids) > 0  # Exact count depends, but should be less than 10
    assert grids[0][0] == [".", "Q", ".", ".", "."]  # First row has queen at col 1