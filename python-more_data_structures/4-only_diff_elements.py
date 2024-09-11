#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set_1
    for i in set_2:
        if (i not in new):
            new.add(i)
    return new
