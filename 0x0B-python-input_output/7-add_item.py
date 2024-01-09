#!/usr/bin/python3
from sys import argv

# Importing the required functions
# Assume these functions are defined in the respective files
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# The JSON file to store the list
filename = "add_item.json"

try:
    # Load existing items from the file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with an empty list
    items = []

# Adding command line arguments to the list
# argv[0] is the script name, so we take the rest
items.extend(argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
