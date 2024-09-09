#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp = [0, 0]
    la = len(tuple_a)
    lb = len(tuple_b)

    if (la > 0):
        tmp[0] = tuple_a[0]
    if (la > 1):
        tmp[1] = tuple_a[1]
    if (lb > 0):
        tmp[0] += tuple_b[0]
    if (lb > 1):
        tmp[1] += tuple_b[1]

    new = (tmp[0], tmp[1])
    return new
