#!/usr/bin/python3
"""
This module provides a function that adds two numbers.
The function ensures that inputs are either integers or floats,
and returns their sum as an integer.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
