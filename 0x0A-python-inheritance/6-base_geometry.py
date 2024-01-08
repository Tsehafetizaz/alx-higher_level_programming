#!/usr/bin/python3
"""Define base geometry class BaseGeometry."""


class BaseGeometry:
    """
    BaseGeometry class with an area method.

    This method is intended to be overridden in derived classes.
    """

    def area(self):
        """
        Raises an Exception with the message that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")
