#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary is None or len(a_dictionary) == 0):
        return None
    big_v = list(a_dictionary.values())[0]
    big_k = list(a_dictionary.keys())[0]
    lst = list(a_dictionary.items())
    for k, v in lst:
        if (v > big_v):
            big_v = v
            big_k = k
    return big_k
