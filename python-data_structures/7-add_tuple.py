#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tmp = [0, 0, 0, 0]
    if (len(tuple_a) == 1):
        tmp[0] = tuple_a[0]
        tmp[2] = tuple_b[0]
        tmp[3] = tuple_b[1]

    if (len(tuple_b) == 1):
        tmp[0] = tuple_a[0]
        tmp[1] = tuple_a[1]
        tmp[2] = tuple_b[0]

    if (len(tuple_a) == 0):
        tmp[2] = tuple_b[0]
        tmp[3] = tuple_b[1]

    if (len(tuple_b) == 0):
        tmp[0] = tuple_a[0]
        tmp[1] = tuple_a[1]

    if (len(tuple_a) == 2 and len(tuple_b) == 2):
        tmp[0] = tuple_a[0]
        tmp[1] = tuple_a[1]
        tmp[2] = tuple_b[0]
        tmp[3] = tuple_b[1]
    new = (tmp[0] + tmp[2], tmp[1] + tmp[3])
    return new
