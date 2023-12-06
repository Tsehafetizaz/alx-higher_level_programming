#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    update_dictionary(a_dictionary, 'language', "Python")
    print("-- Sorted by keys --")
    print_sorted_dictionary(a_dictionary)

    print("--")

    update_dictionary(a_dictionary, 'city', "San Francisco")
    print("-- Sorted by keys --")
    print_sorted_dictionary(a_dictionary)
