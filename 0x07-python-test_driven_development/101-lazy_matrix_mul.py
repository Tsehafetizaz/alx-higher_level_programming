#!/usr/bin/python3
"""
This module provides a function that multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The result of multiplying m_a by m_b using NumPy.

    Raises:
        TypeError: If m_a or m_b contains non-number or are not lists of lists.
    """
    # Check if m_a and m_b are lists of lists and contain only numbers
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in m_a):
        raise TypeError("m_a must be a list of lists of integers/floats")
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float)) for elem in row)
               for row in m_b):
        raise TypeError("m_b must be a list of lists of integers/floats")

    return np.matmul(m_a, m_b)
