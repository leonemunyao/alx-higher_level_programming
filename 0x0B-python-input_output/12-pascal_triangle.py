#!/usr/bin/python3
"""Defines a function"""


def pascal_triangle(n):
    """Generates the nth row of Pascal's triangle."""
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        last_row = pascal_triangle(n - 1)
        this_row = [last_row[i] + last_row[i-1
                                           ] for i in range(len(last_row))]
        return this_row
