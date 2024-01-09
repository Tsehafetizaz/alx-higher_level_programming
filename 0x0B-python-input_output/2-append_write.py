#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file returns the number of characters written.

    Args:
    filename (str): The path to the file where the text will be written.
    text (str): The text to be written to the file.

    Returns:
    int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
