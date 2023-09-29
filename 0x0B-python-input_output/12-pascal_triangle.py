#!/usr/bin/python3

"""An Input and Output Module"""


def pascal_triangle(n):
    """returns a list of lists of integers

    Args:
        n: integer to use to form the pascal triangle

    Return:
        a list of lists of integers
        otherwise an empty list.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        row = []
        row.append(1)

        if len(triangle[i]) > 1:
            pre_row_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(pre_row_len):
                summation = triangle[i][j] + triangle[i][nxt]
                row.append(summation)
                nxt = nxt + 1

        row.append(1)
        triangle.append(row)
    return triangle
