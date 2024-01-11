#!/usr/bin/python3
"""Defines a function"""
import json


def to_json_string(my_obj):
    """Converts an object into a JSON formatted string."""
    return json.dumps(my_obj)
