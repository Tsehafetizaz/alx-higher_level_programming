#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    # Create a new matrix with the same size as the input matrix
    new_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Use a list comprehension to square each element in the row
        squared_row = [x ** 2 for x in row]
        # Add the squared row to the new matrix
        new_matrix.append(squared_row)

    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
     ]
new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
