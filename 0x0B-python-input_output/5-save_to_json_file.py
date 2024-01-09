#!/usr/bin/python3
"""Writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
    my_obj: A Python object to be serialized.
    filename (str): The path to the file where the object will be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
