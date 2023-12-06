#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    integer_value = 0

    for i in range(len(roman_string)):

        if i + 1 < len(roman_string) and roman_numerals[roman_string[i]] < 
                                         roman_numerals[roman_string[i + 1]]:
            integer_value -= roman_numerals[roman_string[i]]
        else:
            integer_value += roman_numerals[roman_string[i]]

            return integer_value


if __name__ == "__main__":
    print("X = {}".format(roman_to_int("X")))
    print("VII = {}".format(roman_to_int("VII")))
    print("IX = {}".format(roman_to_int("IX")))
    print("LXXXVII = {}".format(roman_to_int("LXXXVII")))
    print("DCCVII = {}".format(roman_to_int("DCCVII")))
