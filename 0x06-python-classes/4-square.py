#!/usr/bin/python3
""" Class Square """


class Square():
    """ class Square """
    def __init__(self, size=0):
        """ init class Square """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self, area=0):
        """ Calculate area of the square """
        return(self.__size * self.__size)

    @property
    def size(self):
        """ Creating size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Creating area """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
