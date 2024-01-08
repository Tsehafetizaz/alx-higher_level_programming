#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add an attribute to.
        attr (str): The name of the attribute to add.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

if __name__ == "__main__":
    # Test cases

    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
