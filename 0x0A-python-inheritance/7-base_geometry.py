#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    BaseGeometry class with methods for area and integer validation.

    The area method is intended to be overridden in derived classes.
    The integer_validator method checks if a given value is an integer
    and whether it is greater than 0.
    """

    def area(self):
        """
        Raises an Exception with the message that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a specified value is an integer and greater than 0.

        Args:
            name (str): The name of the variable.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
