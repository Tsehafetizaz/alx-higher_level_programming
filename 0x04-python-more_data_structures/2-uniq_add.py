#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set()
    for i in my_list:
        unique.add(i)
    result = sum(unique)
    return result


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
