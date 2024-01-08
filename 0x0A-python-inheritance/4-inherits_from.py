#!/usr/bin/python3
"""Defines a function"""


def inherits_from(obj, a_class):
    """Checks if an object is derived from another class."""
    return issubclass(type(obj), a_class)
