#!/usr/bin/python3
"""Defines a class Square with size attribute and comparison on the area."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (float or int): The size of the new square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter for the private size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private size attribute.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If 'value' is not a number.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if square is greater than another square in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if square is greater than or equal to anothee in area."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if square is less than another square in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if square is less than or equal to another square in area."""
        return self.area() <= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
