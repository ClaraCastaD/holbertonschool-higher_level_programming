#!/usr/bin/python3
"""  Creating an empty class """


class BaseGeometry():
    """ Init class """
    pass

    def area(self):
        """ Public instance method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that
        validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
