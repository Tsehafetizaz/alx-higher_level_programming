#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()  # Sort the list of keys
    for key in keys:
        print(f"{key}: {a_dictionary[key]}")


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89,
                    'track': "Low level", 'ids': [1, 2, 3]}
    print_sorted_dictionary(a_dictionary)
