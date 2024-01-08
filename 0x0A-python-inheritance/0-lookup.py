#!/usr/bin/python3
"""Defining the lookup function"""

def lookup(obj):
    """
    Returns the list of available attributes and methods
    """
    return [a for a in dir(obj)]
