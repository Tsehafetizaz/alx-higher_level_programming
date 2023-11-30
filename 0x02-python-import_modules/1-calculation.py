#!/usr/bin/python3

a = 10
b = 5

if __name__ == "__main__":
        from calculator_1 import add, sub, mul, div

        result1 = add(a, b)
        print(f"{a} + {b} = {result1}")

        result2 = sub(a, b)
        print(f"{a} - {b} = {result2}")

        result3 = mul(a, b)
        print(f"{a} * {b} = {result3}")

        result4 = div(a, b)
        print(f"{a} / {b} = {result4}")
