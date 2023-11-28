#!/usr/bin/python3

# Loop through the ASCII values of lowercase letters (97 to 122)
for ascii_value in range(97, 123):
    # Use the chr() function to convert the ASCII value to a character and print it without a newline
    print(chr(ascii_value), end='')

    # Print a newline after all characters are printed
    print()
