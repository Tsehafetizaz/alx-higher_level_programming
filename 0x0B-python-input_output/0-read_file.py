#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
    filename (str): The path to the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
