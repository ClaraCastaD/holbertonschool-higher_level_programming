#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    sum = 0
    new_list = set(my_list)
    for integer in new_list:
        sum = integer + sum
    return sum
