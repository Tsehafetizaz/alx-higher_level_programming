#!/usr/bin/env python3

def remove_char_at(str, n):
    # Check if n is a valid index within the string
    if n >= 0 and n < len(str):
        # Use string slicing to remove the character at position n
        return str[:n] + str[n + 1:]
    else:
        # Return the original string if n is out of range
        return str

    if __name__ == "__main__":
        # Test cases
        print(remove_char_at("Best School", 3))
        print(remove_char_at("Chicago", 2))
        print(remove_char_at("C is fun!", 0))
        print(remove_char_at("School", 10))
        print(remove_char_at("Python", -2))
