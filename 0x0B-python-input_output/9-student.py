#!/usr/bin/python3
"""Defines a class"""


class Student:
    """A class to represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize attributes of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a JSON representation of the student."""
        return self.__dict__
