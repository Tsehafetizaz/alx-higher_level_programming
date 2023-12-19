#!/usr/bin/python3
"""Defines a class Square with size and position attributes."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
            position (tuple): The position of the new square. Defaults to (0,0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the private position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the private position attribute.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If 'value' is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
            return

        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
