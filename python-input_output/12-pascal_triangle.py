#!/usr/bin/python3
"""python"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []
    matrix = [[1]]
    x = 0
    for k in range(n - 1):
        tmp = []
        j = 0
        tmp.append(1)
        for i in range(1, len(matrix[x])):
            tmp.append(matrix[x][j] + matrix[x][i])
            j += 1
        x += 1
        tmp.append(1)
        matrix.append(tmp)
    return matrix
