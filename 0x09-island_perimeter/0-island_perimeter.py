#!/usr/bin/python3
"""A module for calculating Island perimeter
   Interview question with Python.
"""


def island_perimeter(grid):
    """calculates the perimeter of an island(without lakes).
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        l = len(row)
        for j, k in enumerate(row):
            if k == 0:
                continue
            edge = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == l - 1 or (l > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edge)
    return perimeter
