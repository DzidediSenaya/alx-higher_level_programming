#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Perform lazy matrix multiplication using NumPy.

    Args:
        m_a (list): First matrix (list of lists)
        m_b (list): Second matrix (list of lists)

    Returns:
        list: Result of matrix multiplication

    Raises:
        ValueError: If m_a or m_b is not a list or a list of lists
        ValueError: If m_a or m_b is an empty list
        ValueError: If elements in m_a or m_b are not integers or floats
        ValueError: If m_a or m_b is not a rectangle (rows have different sizes)
        ValueError: If m_a and m_b cannot be multiplied
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("m_a and m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("m_a and m_b must be a list of lists")

    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a and m_b can't be empty")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a):
        raise ValueError("m_a should contain only integers or floats")

    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise ValueError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("Each row of m_a must be of the same size" or "Each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    np_a = np.array(m_a)
    np_b = np.array(m_b)
    result = np.dot(np_a, np_b)

    return result.tolist()
