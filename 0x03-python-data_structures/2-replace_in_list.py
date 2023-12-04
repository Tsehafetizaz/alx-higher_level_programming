#!/usr/bin/python3

def replace_in_list(my_list, idx, i):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = i
        return my_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    i = 9
    new_list = replace_in_list(my_list, idx, i)
    print(new_list)
    print(my_list)
