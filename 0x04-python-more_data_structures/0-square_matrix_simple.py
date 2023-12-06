#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda w: w**2, matrix[i]))

    return (new_matrix)


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
     ]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
