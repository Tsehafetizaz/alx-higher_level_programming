#!/usr/bin/python3

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


if __name__ == "__main__":
    # Test cases

    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
