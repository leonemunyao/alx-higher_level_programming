#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get or set the width"""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Get or set the height"""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
