#!/usr/bin/pyhthon3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
