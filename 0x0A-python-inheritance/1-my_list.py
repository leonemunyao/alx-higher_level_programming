#!/usr/bin/python3
"""Defines Mylist class"""


class MyList(list):

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
