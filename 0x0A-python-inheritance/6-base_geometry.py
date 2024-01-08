#!/usr/bin/python3
"""Defines a class"""


class BaseGeometry():
    """A base geometry class that other classes will inherit from."""
    def area(self):
        """Calculate the area of the object."""
        raise Exception("area() is not implemented")
