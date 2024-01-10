#!/usr/bin/python3
"""Defines a function"""


def text_indentation(text):
    """Removes leading and trailing spaces from each line"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    current_line = ""

    for char in text:
        if char in ['.', '?', ':']:
            print(current_line.strip())
            print()
            current_line = ""
        
        else:
            current_line += char

    print(current_line.strip())
    print()
