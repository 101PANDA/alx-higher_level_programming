#!/usr/bin/python3

"""gives the square of a matrix"""


def square_matrix_simple(matrix=[]):
    matrix_row = len(matrix)
    matrix_sqr = []

    """looping through the whole matrix to find the length of each row"""

    for i in range(0, matrix_row):
        if matrix_row == 0:
            break

        element = []
        element_len = len(matrix[i])

        """looping through individual elements and finding their square"""
        for x in range(0, element_len):
            element.append(matrix[i][x]**2)

        matrix_sqr.append(element)

    return matrix_sqr
