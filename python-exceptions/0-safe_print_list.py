#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for i in range(x):
            print(my_list[num], end="")
            num += 1
        print()
    except:
        print()
    return num
