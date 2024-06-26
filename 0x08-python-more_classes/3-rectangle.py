#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize attributes of the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets or sets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets or sets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return (
            2 * (self.__width + self.__height)
            if self.__width and self.__width
            else 0
            )

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle__str = ""
            for i in range(self.__height):
                rectangle__str += "#" * self.__width
                if i < self.__height - 1:
                    rectangle__str += "\n"
            return rectangle__str
