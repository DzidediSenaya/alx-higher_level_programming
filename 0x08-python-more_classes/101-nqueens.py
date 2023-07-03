#!/usr/bin/python3

import sys


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at the specified
    position on the board.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index of the position to check.
        col (int): The column index of the position to check.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.

    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, N, solutions):
    """
    Recursively solve the N-queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row to place the queen.
        N (int): The size of the chessboard.
        solutions (list): A list to store the found solutions.

    """
    if row == N:
        # Found a solution, append it to the list of solutions
        queens = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens.append([i, j])
        solutions.append(queens)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen and recursively solve for the next row
            board[row][col] = 1
            solve_nqueens(board, row + 1, N, solutions)
            # Backtrack and remove the queen
            board[row][col] = 0


def nqueens(N):
    """
    Solve the N-queens problem and print the solutions.

    Args:
        N (int): The size of the chessboard.

    """
    # Check if N is an integer greater or equal to 4
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)

    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
