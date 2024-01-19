#!/usr/bin/python3
"""Defines a rectangle"""

from models.base import Base


class Rectangle(Base):
    """Defines a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """First rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width if it is positive"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height if its positive"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x and validates it's within range of the window."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y and validates it's within range of the window."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must >= 0")
        else:
            self.__y = value

    def area(self):
        """Finds the area"""
        return self.width * self.height

    def display(self):
        """Display #0"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#"*self.width)

    def __str__(self):
        """Override the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update multiple attributes at once"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary with all object's data"""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }

    def to_csv_row(self):
        """Return a CSV row representation of this rectangle."""
        return "{},{},{},{},{}".format(self.id, self.width, self.height, self.x, self.y)

    @classmethod
    def create_from_csv_row(cls, row):
        """Create and return an instance from a CSV row string."""
        return cls(*map(int, row[1:]))
