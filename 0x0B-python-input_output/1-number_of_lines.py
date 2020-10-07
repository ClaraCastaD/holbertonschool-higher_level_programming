#!/usr/bin/python3
""" Function that returns n of lines """


def number_of_lines(filename=""):
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
