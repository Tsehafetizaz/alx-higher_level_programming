#!/usr/bin/python3
"""
This module contains the Base class.
"""

class Base:
    """
    Base class for the project.
    Manages id attribute for all future classes to avoid duplicating code.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int): The id of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
