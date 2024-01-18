#!/usr/bin/python3
"""Defines a square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """A class to represent a square, inheriting from the Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """setter for ize"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the str method"""
        return f"[square] ({self.id}) {self.x}/{self.y} - {self.width}"