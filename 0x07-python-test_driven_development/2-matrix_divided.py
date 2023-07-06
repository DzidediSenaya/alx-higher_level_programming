#!/usr/bin/python3
"""
Module for matrix division
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): The number to divide the matrix elements by

    Returns:
        list: A new matrix with elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If each row of the matrix doesn't have the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
