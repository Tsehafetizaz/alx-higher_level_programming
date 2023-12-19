import math


class MagicClass:
    def __init__(self, radius=0):
        """Initialize the MagicClass with a given radius."""
        self.__check_type(radius)
        self.__radius = radius

    def __check_type(self, radius):
        """Check if the type of radius is int or float."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

    def area(self):
        """Calculate the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle."""
        return 2 * math.pi * self.__radius
