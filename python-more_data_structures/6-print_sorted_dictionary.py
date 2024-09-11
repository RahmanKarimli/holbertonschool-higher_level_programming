#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(sorted(a_dictionary.items()))
    for i in range(len(lst)):
        print(f"{lst[i][0]}: {lst[i][1]}")
