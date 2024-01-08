#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    MyList is a subclass of the built-in list type, with an additional method
    to print the list in a sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        print(sorted(self))
