#!/usr/bin/python3

# Loop through the ASCII values of lowercase letters (97 to 122)
for ascii_value in range(97, 123):
    # Convert the ASCII value to a character
    character = chr(ascii_value)

    # Check if the character is not 'q' and not 'e'
    if character != 'q' and character != 'e':
        # Print the character without a newline
        print(character, end='')

        # Print a newline after all characters are printed
        print()
