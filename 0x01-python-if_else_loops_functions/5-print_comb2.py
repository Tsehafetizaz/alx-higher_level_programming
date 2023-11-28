#!/usr/bin/python3

# Loop through numbers from 0 to 99
for number in range(100):
    # Use an f-string to format the numbers with two digits, separated by ", "
    print(f"{number:02}", end=", " if number < 99 else "\n")
