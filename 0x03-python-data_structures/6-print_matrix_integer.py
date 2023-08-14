#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: the matrix to work with
    """
    if matrix:
        sep = " "
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == len(matrix[i]) - 1:
                    sep = ""
                print("{:d}".format(matrix[i][j]), end=sep)
                sep = " "
            print()
