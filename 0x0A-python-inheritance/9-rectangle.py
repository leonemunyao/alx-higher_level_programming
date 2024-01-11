#!/usr/bin/python3
"""Defines a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, inherits from BaseGeometry."""
    def __init__(self, width, height):
        """defines class Rectangle"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height
    def __str__(self):
        """Returns a string representation of the object."""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string