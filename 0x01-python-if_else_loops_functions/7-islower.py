#!/usr/bin/python3
def islower(c):
    if len(c) != 1:  # Check if the input is not a single character
        return False  # or handle it differently if needed
    return 'a' <= c <= 'z'
