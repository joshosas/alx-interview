#!/usr/bin/python3
"""Silving a question that involves calculating
   the perimeter of an island represented by a grid
"""


def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    if type(grid) != list:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check adjacent cells
                if row > 0 and grid[row - 1][col] == 1:  # Up
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:  # Left
                    perimeter -= 2

    return perimeter
