#!/usr/bin/python3
"""Defines a function"""
import json


def load_from_json_file(filename):
    """Loads data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
