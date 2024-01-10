#!/usr/bin/python3
"""Defines a function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices."""
    for m in [m_a, m_b]:
        # Check if m is a list
        if not isinstance(m, list):
            raise TypeError("m_a must be a list or m_b must be a list")

        # Check if m is a list of lists
        if not all(isinstance(row, list) for row in m):
            raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

        # Check if m is not empty
        if not m or any(not row for row in m):
            raise ValueError("m_a can't be empty or m_b can't be empty")

        # Check if all elements are integers or floats
        if any(not isinstance(elem, (int, float)) for row in m for elem in row):
            raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles (all rows of the same size)
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
