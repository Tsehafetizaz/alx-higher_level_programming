#!/usr/bin/python3
import sys

# Get the number of arguments (excluding the script name)
num_arguments = len(sys.argv) - 1  # Subtract 1 for the script name itself

# Get the list of arguments (excluding the script name)
arguments = sys.argv[1:]

if num_arguments == 0:
    print("0 arguments.")
elif num_arguments == 1:
    print("1 argument:")
else:
    print(f"{num_arguments} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(arguments, start=1):
        print(f"{i}: {arg}")
