#!/usr/bin/python3
from 9-rectangle import Rectangle

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
        super().__init__(size, size)  # Call Rectangle's __init__
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the Square.

        Returns:
            str: The formatted string representation in the format
                 [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

if __name__ == "__main__":
    # Test cases

    s = Square(13)

    print(s)
    print(s.area())
