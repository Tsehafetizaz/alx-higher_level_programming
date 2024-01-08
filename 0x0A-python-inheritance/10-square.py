#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        size (int): The size of the square, must be a positive integer.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Validates that size is a positive integer using the
        integer_validator method from BaseGeometry.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Call to Rectangle's __init__
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the Square.

        Returns:
            str: The formatted string representation.
        """
        return super().__str__()  # Rectangle's __str__ is suitable
