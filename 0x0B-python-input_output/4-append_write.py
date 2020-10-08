#!/usr/bin/python3
""" Function """


def append_write(filename="", text=""):
    """ Function that appends a string """

    with open(filename, "a") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
