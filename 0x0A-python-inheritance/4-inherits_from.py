#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, 
              otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class


if __name__ == "__main__":
    # Test cases

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
