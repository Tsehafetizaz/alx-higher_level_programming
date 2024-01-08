#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
