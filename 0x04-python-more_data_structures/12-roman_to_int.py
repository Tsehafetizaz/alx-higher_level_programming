#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    prev_value = 0

    for numeral in reversed(roman_string):
        int_val = roman_numerals.get(numeral, 0)
        if int_val < prev_value:
            integer_value -= int_val
        else:
            integer_value += int_val
        prev_value = int_val
    return integer_value


if __name__ == "__main__":
    print("X = {}".format(roman_to_int("X")))
    print("VII = {}".format(roman_to_int("VII")))
    print("IX = {}".format(roman_to_int("IX")))
    print("LXXXVII = {}".format(roman_to_int("LXXXVII")))
    print("DCCVII = {}".format(roman_to_int("DCCVII")))
