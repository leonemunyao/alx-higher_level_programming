#!/usr/bin/python3
"""Defines a function"""


def class_to_json(obj):
    """Converts an object to JSON format."""
    return obj.__dict__
