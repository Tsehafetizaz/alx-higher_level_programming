#!/usr/bin/python3
"""Returns a Python object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
    my_str (str): A JSON string to be converted into a Python object.

    Returns:
    A Python object derived from the JSON string.
    """
    return json.loads(my_str)
