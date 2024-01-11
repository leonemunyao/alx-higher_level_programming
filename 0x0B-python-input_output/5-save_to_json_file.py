#!/usr/bin/python3
"""Defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
