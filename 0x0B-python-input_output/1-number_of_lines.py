#!/usr/bin/python3
""" Function """


def number_of_lines(filename=""):
    """ Function that return n of lines"""

    i = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            i += 1
    my_file.close()
    return (i)
