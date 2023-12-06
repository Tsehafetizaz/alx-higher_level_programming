#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []

    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary


def print_sorted_dictionary(my_dict):
    for key in sorted(my_dict.keys()):
        print("{}: {}".format(key, my_dict[key]))


if __name__ == "__main__":
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}

    print("Original Dictionary:")
    print_sorted_dictionary(a_dictionary)
    print("--")

    new_dict = complex_delete(a_dictionary, 'C')

    print("Modified Dictionary:")
    print_sorted_dictionary(a_dictionary)
    print("--")

    print("New Dictionary:")
    print_sorted_dictionary(new_dict)
