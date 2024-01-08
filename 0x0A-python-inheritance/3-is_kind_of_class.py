#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a
    class that inherited from, the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be compared against.

    Returns:
        bool: True if obj is an instance or a subclass instance of a_class,
              otherwise False.
    """
    return isinstance(obj, a_class)
