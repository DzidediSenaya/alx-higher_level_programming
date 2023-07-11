#!/usr/bin/python3
"""
Module for technical interview prep
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows (n).

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
