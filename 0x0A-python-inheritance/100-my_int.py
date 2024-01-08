#!/usr/bin/python3

class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the == operator to behave like !=.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to behave like ==.

        Args:
            other (any): The object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        return super().__eq__(other)

if __name__ == "__main__":
    # Test cases

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
