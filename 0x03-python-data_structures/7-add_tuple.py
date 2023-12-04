#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    sum_first_elements = tuple_a[0] + tuple_b[0]
    sum_second_elements = tuple_a[1] + tuple_b[1]

    return (sum_first_elements, sum_second_elements)

if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)
    print(add_tuple(tuple_a, (1, )))
    print(add_tuple(tuple_a, ()))
