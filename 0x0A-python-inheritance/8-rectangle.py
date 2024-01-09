#!/usr/bin/python3
"""Define a class Rectangle that inherits"""


class BaseGeometry():
    """A base geometry class with common attributes & methods."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represent a rectangle and its properties."""
    def __init__(self, width, height):
        """Defines class Rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
