#!/usr/bin/python3
"""Defines a function"""


def append_write(filename="", text=""):
    """Appends the given text to filename and writes it."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
