#!/usr/bin/python3
'''A module for calculating copyALL & Paste
   Minimum Operations
'''


def minOperations(n):
    '''
    calculates the number of times required to copy
    and paste a single character n number times
    '''
    if n == 1:
        return 0

    operations = []

    for i in range(1, n):
        if n % i == 0:
            operations.append(minOperations(i) + (n // i))

    return min(operations)
