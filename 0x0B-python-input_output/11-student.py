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
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reloads an instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
