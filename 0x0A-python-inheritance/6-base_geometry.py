#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class with an area method.

    This method is intended to be overridden in derived classes.
    """

    def area(self):
        """
        Raises an Exception with the message that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    # Test cases

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
