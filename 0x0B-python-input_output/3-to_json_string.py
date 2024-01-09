#!/usr/bin/python3
"""Returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
    my_obj: A Python object to be converted into a JSON formatted string.

    Returns:
    A string: JSON representation of `my_obj`.
    """
    return json.dumps(my_obj)
