#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value


def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dict.items():
        print(f'{key}: {value}')


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    update_dictionary(a_dictionary, 'language', "Python")
    print("-- Sorted by keys --")
    print_sorted_dictionary(a_dictionary)

    print("--")

    update_dictionary(a_dictionary, 'city', "San Francisco")
    print("-- Sorted by keys --")
    print_sorted_dictionary(a_dictionary)
