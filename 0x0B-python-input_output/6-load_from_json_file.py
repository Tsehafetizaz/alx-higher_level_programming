#!/usr/bin/python3
"""Creates a Python object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
    filename (str): The path to the JSON file to be read.

    Returns:
    A Python object derived from the JSON file content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
