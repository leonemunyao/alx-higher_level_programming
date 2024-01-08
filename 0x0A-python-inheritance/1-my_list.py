#!/usr/bin/python3
"""Defines Mylist class"""


class MyList(list):
    """Mylist class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
