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

    @property
    def width(self):
        """Getter for width"""
        return super().width

    @width.setter
    def width(self, value):
        """Setter for width"""
        super(Square, Square).width.fset(self, value)
        super(Square, Square).height.fset(self, value)

    @property
    def height(self):
        """Getter for width"""
        return super().height

    @height.setter
    def height(self, value):
        """Setter for height"""
        super(Square, Square).width.fset(self, value)
        super(Square, Square).height.fset(self, value)

    def update(self, *args, **kwargs):
        """Assings attribues"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }

    def to_csv_row(self):
        """Returns a CSV row representing the square instance"""
        return "{},{},{},{},{}".format(self.id, self.width, self.height, self.x, self.y)

    @classmethod
    def create_from_csv_row(cls, row):
        """Creates an instance of cls from a given csv row string"""
        return cls(*map(int, row[1:]))
