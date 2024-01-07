def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists of float: New matrix with each element divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows of matrix are of different sizes,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) and
            all(isinstance(elem, (int, float)) for elem in row)
            for row in matrix):
        raise TypeError("matrix must be matrix (list of lists) of integers")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
