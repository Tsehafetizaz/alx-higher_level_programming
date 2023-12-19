#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
