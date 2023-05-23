#!/usr/bin/python3
"""A module for solving N queens puzzle.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)


def solveNQueens(N):
    """Solve N queens first module
    """
    solutions = []
    chessboard = [[0] * N for _ in range(N)]

    def placeQueen(col):
        """Place queen on a chessboard
        """
        if col >= N:
            solutions.append([row[:] for row in chessboard])
            return

        for row in range(N):
            if isSafe(row, col):
                chessboard[row][col] = 1
                placeQueen(col + 1)
                chessboard[row][col] = 0

    def isSafe(row, col):
        """Check if no queen exists in the same row
        """
        for c in range(col):
            if chessboard[row][c] == 1:
                return False

        # Check if no queen exists in the same diagonal
        r, c = row, col
        while r >= 0 and c >= 0:
            if chessboard[r][c] == 1:
                return False
            r -= 1
            c -= 1

        # Check if no queen exists in the same anti-diagonal
        r, c = row, col
        while r < N and c >= 0:
            if chessboard[r][c] == 1:
                return False
            r += 1
            c -= 1

        return True

    placeQueen(0)

    return solutions


def printSolutions(solutions):
    for solution in solutions:
        for row in solution:
            print(''.join(map(lambda cell: 'Q' if cell == 1 else '.', row)))
        print()
