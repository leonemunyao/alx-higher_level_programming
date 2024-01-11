#!/usr/bin/python3
"""Defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new string after the
    first occurrence of the search string in filename."""
    # Open file for reading and writing.
    text = ""

    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
