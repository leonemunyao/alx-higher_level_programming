#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, height=0, width=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get or set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get or set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
