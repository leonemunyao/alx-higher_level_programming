#!/usr/bin/python3
def lookup(obj):
    """Returns the list of available attributes and methods"""
    return [a for a in dir(obj)]
