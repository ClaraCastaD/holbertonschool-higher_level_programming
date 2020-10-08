#!/usr/bin/python3
""" Function thst reads a txt file """


def read_file(filename=""):
    """ Open function """

    with open(filename, "r") as my_file:
        print(my_file.read(), end="")
    my_file.close()
