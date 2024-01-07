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
    """
    return np.matmul(m_a, m_b)
