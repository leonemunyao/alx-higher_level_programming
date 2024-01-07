#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialize attributes of the rectangle object.
        
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"""
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height) if self.__width and self.__height else 0
