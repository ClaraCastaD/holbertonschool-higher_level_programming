#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) <= 0:
        return None
    biggest = list(a_dictionary.values())[0]
    key = list(a_dictionary.keys())[0]
    for i, j in a_dictionary.items():
        if j > biggest:
            biggest = j
            key = i
    return (key)
