#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
            print(upper_char, end="")
            print()  # Print a newline after processing the entire string
