#!/usr/bin/python3
"""Defines a function"""


def write_file(filename="", text=""):
    """Writes the given text to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
