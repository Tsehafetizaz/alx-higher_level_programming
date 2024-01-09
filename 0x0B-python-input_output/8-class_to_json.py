#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON

    Args:
    obj: An instance of a class.

    Returns:
    A dictionary representation of the instance for JSON serialization.
    """
    return obj.__dict__
