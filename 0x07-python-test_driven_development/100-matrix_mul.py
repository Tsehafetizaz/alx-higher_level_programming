#!/usr/bin/python3
"""
This module provides a function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        list of lists of int/float: The result of multiplying m_a by m_b.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats,
                   or if they are not rectangles,
                   or if they cannot be multiplied.
        ValueError: If m_a or m_b is empty.
    """
    def check_matrix(matrix, name):
        if not isinstance(matrix, list) or not all(isinstance(row, list)
                                                   for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if matrix == [] or any(row == [] for row in matrix):
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(elem, (int, float))
                   for row in matrix
                   for elem in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError(f"each row of {name} must be of the same size")

    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b))
            for col_b in zip(*m_b)] for row_a in m_a]
