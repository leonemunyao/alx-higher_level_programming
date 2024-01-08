#!/usr/bin/python3
"""Defines a function"""


def is_kind_of_class(obj, a_class):
    """Checks if an object belongs to a class or its subclass."""
    return isinstance(obj, a_class)
