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
    print(f"n={n} execution time: {execution_time:.4f} seconds")
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
    print(f"n=4 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 2
    assert grids[0] == [[".", "Q", ".", "."], [".", ".", ".", "Q"], ["Q", ".", ".", "."], [".", ".", "Q", "."]]

def test_n_queens_5():
    grids, exec_time = capture_solutions(solve_n_queens, 5)
    print(f"n=5 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 10
    assert grids[0] == [["Q", ".", ".", ".", "."], [".", ".", "Q", ".", "."], [".", ".", ".", ".", "Q"], [".", "Q", ".", ".", "."], [".", ".", ".", "Q", "."]]

def test_n_queens_6():
    grids, exec_time = capture_solutions(solve_n_queens, 6)
    print(f"n=6 execution time: {exec_time:.4f} seconds")
    assert len(grids) == 4, f"Expected 4 solutions, got {len(grids)}"
    grid = grids[0]
    # Check one queen per row
    for row in grid:
        assert row.count("Q") == 1, f"Row {row} should have exactly one queen"
    # Check columns (no two queens in same column)
    cols = [row.index("Q") for row in grid]
    assert len(set(cols)) == 6, "Queens must be in unique columns"
    # Check diagonals (no two queens on same diagonal)
    for i in range(6):
        for j in range(i + 1, 6):
            row_diff = j - i
            col_diff = abs(cols[j] - cols[i])
            assert row_diff != col_diff, f"Queens at ({i}, {cols[i]}) and ({j}, {cols[j]}) attack diagonally"

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

# Heavy Load testing -- AVG 35 seconds prior to concurrency optimizations
# def test_n_queens_13():
#     grids, exec_time = capture_solutions(solve_n_queens, 13)
#     print(f"n=13 execution time: {exec_time:.4f} seconds")
#     assert len(grids) == 73712

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