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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
