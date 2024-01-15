#!/usr/bin/python3
"""
Module for the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle.
    Represents a square with equal width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        Args:
            size (int): The size of the square.
            x (int): The x position of the square.
            y (int): The y position of the square.
            id (int): The id of the object.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get or set the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        The width and height of the square are set to this value.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square instance attributes.
        Args:
            *args: Non-keyword variable length argument list.
            **kwargs: Keyword variable length argument list.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for attr, value in zip(attributes, args):
                if attr == "size":
                    self.size = value
                else:
                    setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        Return the string representation of the Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
