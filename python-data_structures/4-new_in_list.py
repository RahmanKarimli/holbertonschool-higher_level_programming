#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = []
    for i in my_list:
        tmp.append(i)
    if (idx < 0 or idx >= len(my_list)):
        return my_list
    tmp[idx] = element
    return tmp
