def solve_n_queens(n, preplaced=None):
    board = [-1] * n
    if preplaced:
        for row, col in preplaced:
            if row >= n or col >= n or row < 0 or col < 0:
                raise ValueError("Preplaced position out of bounds")
            board[row] = col
    solutions = []
    place_queens(board, 0, n, solutions, preplaced or [])
    return solutions

def place_queens(board, row, n, solutions, preplaced):
    if row == n:
        solutions.append(board[:])
        return
    # If this row has a preplaced queen, skip to next row
    preplaced_rows = {r for r, _ in preplaced}
    if row in preplaced_rows:
        if not underAttack(board, row, board[row], n):
            place_queens(board, row + 1, n, solutions, preplaced)
        return
    # Otherwise, try placing a queen in each column
    for col in range(n):
        if not underAttack(board, row, col, n):
            board[row] = col
            place_queens(board, row + 1, n, solutions, preplaced)
            board[row] = -1

def underAttack(board, row, col, n):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == -1:
            continue
        if prev_col == col or abs(row - prev_row) == abs(col - prev_col):
            return True
    return False

def board_to_grid(board, n):
    grid = [["." for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(board):
        if col != -1:
            grid[row][col] = "Q"
    return grid

if __name__ == "__main__":
    import sys
    import json
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    preplaced = []
    if len(sys.argv) > 2 and sys.argv[2]:
        pairs = sys.argv[2].split(",")
        preplaced = [(int(pairs[i]), int(pairs[i+1])) for i in range(0, len(pairs), 2)]
    solutions = solve_n_queens(n, preplaced)
    grids = [board_to_grid(board, n) for board in solutions]
    print(json.dumps(grids))