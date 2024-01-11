#!/usr/bin/python3
"""Defines a function"""
import json


def from_json_string(my_str):
    """Converts a JSON string to a dictionary."""
    return json.loads(my_str)
