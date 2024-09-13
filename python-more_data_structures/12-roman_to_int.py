#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    for i in range(len(roman_string)): #2
        if (i < len(roman_string) - 1 and nums[roman_string[i]] < nums[roman_string[i + 1]]):
            sum += nums[roman_string[i + 1]] - nums[roman_string[i]]
            i += 2
            continue
        else:
            sum += nums[roman_string[i]]
    return sum
