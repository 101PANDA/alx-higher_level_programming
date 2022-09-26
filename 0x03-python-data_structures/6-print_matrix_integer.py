#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    if matrix == []:
        print()

    v_len = len(matrix)
    i = 0

    for q in range(v_len):
        h_len, j = len(matrix[i]), 0

        for w in range(h_len):

            if j != (h_len - 1):
                print("{:d}".format(matrix[i][j]), end=" ")

            if j == (h_len - 1):
                print("{:d}".format(matrix[i][j]))

            j += 1

        i += 1
