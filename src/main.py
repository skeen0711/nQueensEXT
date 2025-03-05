def solve_n_queens(n):
    board = [-1] * n  # Consistent numeric type
    solutions = []
    place_queens(board, 0, n, solutions)
    if not solutions:
        print("No solutions found.")
    else:
        print(f"Found {len(solutions)} solutions:")  # Fixed "Founde"
        for i, solution in enumerate(solutions):
            print(f"\nSolution {i + 1}:")  # Fixed "/n"
            print_board(solution, n)

def place_queens(board, row, n, solutions, preplaced=[]):
    if row == n:
        solutions.append(board[:])
        return
    if row in [p[0] for p in preplaced]:
        if underAttack(board, row, board[row], n):
            return
        place_queens(board, row + 1, n, solutions, preplaced)
    for col in range(n):
        if not underAttack(board, row, col, n):
            board[row] = col
            place_queens(board, row + 1, n, solutions, preplaced)
            board[row] = -1  # Consistent reset

def underAttack(board, row, col, n):
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == -1:
            continue
        if prev_col == col or abs(row - prev_row) == abs(col - prev_col):
            return True
    return False

def print_board(board, n):
    for row in range(n):
        line = ['.'] * n
        if board[row] != -1:
            line[board[row]] = 'Q'
        print(' '.join(line))

if __name__ == "__main__":
    n = 4
    solve_n_queens(n)