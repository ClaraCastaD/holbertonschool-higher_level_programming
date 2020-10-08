
#!/usr/bin/python3
""" Function """


def write_file(filename="", text=""):
    """ Function that writes a string """

    with open(filename, "w") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
