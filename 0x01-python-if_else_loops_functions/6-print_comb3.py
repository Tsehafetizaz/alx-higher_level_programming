#!/usr/bin/python3

# Loop through the first digit (0 to 8)
for first_digit in range(9):
    # Loop through the second digit (1 greater than the first digit to 9)
    for second_digit in range(first_digit + 1, 10):
        # Use an f-string to format and print the combination
        print(f"{first_digit}{second_digit}", end=", " if first_digit < 8 or second_digit < 9 else "\n")
