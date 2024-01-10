#!/usr/bin/python3
"""Defines a function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides each element in the given matrix by the divisor."""
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for
               elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("Division by zero")
    
    my_result = [[round(elem / div, 2) for elem in row] for row in matrix]

    return my_result

    