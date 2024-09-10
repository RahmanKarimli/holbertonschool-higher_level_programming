#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        tmp = []
        for j in i:
            tmp.append(j ** 2)
        new.append(tmp)
    return new
