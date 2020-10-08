#!/usr/bin/python3
""" Function """


def read_lines(filename="", nb_lines=0):
    """read n lines of file"""

    i = 0
    with open(filename, "r") as my_file:
        for line in my_file:
            i += 1
            print(line, end="")
            if i == nb_lines:
                break
    my_file.close()
    return (i)
