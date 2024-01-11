#!/usr/bin/python3
"""Defines a class"""


class Student:
    """A class to represent a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize attributes of the student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a JSON representation of the student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
