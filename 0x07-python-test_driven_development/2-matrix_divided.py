#!/usr/bin/python3

""" divides through a matix"""

def matrix_divided(matrix, div):
    if type(matrix) != list:
        mess = "matrix must be a matrix(list of lists)of integers/f\
loats"
        raise TypeError(mess)
    
