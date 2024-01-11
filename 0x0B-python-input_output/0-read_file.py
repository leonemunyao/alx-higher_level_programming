#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """Reads the contents of a file and returns it as a string."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
