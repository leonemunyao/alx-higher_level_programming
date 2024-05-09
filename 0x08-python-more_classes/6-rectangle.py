#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A class that represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize attributes of the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets or sets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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

    """Private class attribute number of instances. Increment during each new instance instantiation. Delete during each instance deletion."""
    number_of_instances = 0

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return (
            2 * (self.__width + self.__height)
            if self.__width and self.__height
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

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
