#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix

    Args:
        matrix: the matrix to work with

    Return:
        the list of squared data of the same length
    """
    if matrix:
        new_list = []
        for x in range(len(matrix)):
            new_list.append(list(map(lambda y: (y * y), matrix[x])))
        return new_list
