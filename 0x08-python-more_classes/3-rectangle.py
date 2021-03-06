#!/usr/bin/python3
""" Empty class Rectangle """


class Rectangle():
    """ Init class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """ height """
        return self.__height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ init width of Rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ init height of Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returning area of the rectangle """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Returning perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """ Print a Rectangle """
        rect = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                rect += "#" * self.__width
                rect += "\n"
            rect = rect[:-1]
        return rect
