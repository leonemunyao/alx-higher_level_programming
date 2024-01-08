#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry():
    """A base geometry class for other geometric
      shapes to inherit from.
      """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
