#!/usr/bin/python3
""" Create class list """


class MyList(list):
    """ Init Class list """
    def print_sorted(self):
        """  Prints the list sorted """
        print(sorted(self))
