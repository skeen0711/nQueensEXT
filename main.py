
def solve_n_queens(n):
    """
    Solve the N-Queens problem for an NxN chessboard.
    Args:
        n (int): the size of the length and width of the chessboard.
    Returns:
        None: Prints all valid solutions to the console.
    """
    board = ["."] * n # one row of the board
    solutions = []
    place_queens(board, 0, n, solutions)

    if not solutions:
        print("No solutions found.")
    else:
        print(f"Founde {len(solutions)} solutions:")
        for i, solution in enumerate(solutions):
            print(f"/nSolution {i + 1}:")
            print_board(solution, n)

def place_queens(board, row, n, solutions):
    """
    Recursively place queens on the board with backtracking.
    Args:
        board (list): the current state of the board.
        row (int): the current row we are placing queens on.
        n (int): Size of the board.
        solutions (list): List of all valid solutions found.
    """

    # If we've reached row n, we have already checked all rows.
    # This is the base case, return the current solutions and go back up the call stack
    if row == n:
        solutions.append(board[:])
        return

    # Attempt to place a queen in each column of the current row
    for col in range(n):
        if not underAttack(board, row, col, n):
            board[row] = col
            place_queens(board, row + 1, n, solutions)
            board[row] = '.' # reset to empty to check next col for a possible Queen location

def underAttack(board, row, col, n):
    """
    Check if the current square is under attack by a currently placed queen.
    :param board: list of column indexes representing the board
    :param row: Square's Row
    :param col: Square's Column
    :param n: Size of the board
    :return: True if under attack, False if safe
    """
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == '.':
            continue
        if prev_col == col or abs(row - prev_row) == abs(col - prev_col):
            return True
    return False

def print_board(board, n):
    """ Print the board to the console. """
    for row in range(n):
        line = ['.'] * n
        if board[row] != '.':
            line[board[row]] = 'Q'
        print(' '.join(line))

if __name__ == "__main__":
    n = 4
    solve_n_queens(n)