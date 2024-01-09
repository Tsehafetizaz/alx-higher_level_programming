#!/usr/bin/python3
"""Inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific str

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line where
                          search_string is found.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
