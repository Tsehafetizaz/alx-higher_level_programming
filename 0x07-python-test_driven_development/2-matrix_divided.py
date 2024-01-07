def matrix_divided(matrix, div):
    # Validate matrix as a list of lists of integers/floats
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Check if all rows are of the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div as a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division, ensuring each line remains under 80 characters
    return [
        [round(elem / div, 2) for elem in row]
        for row in matrix
    ]
