#!/usr/bin/python3
"""create"""
import json


def load_from_json_file(filename):
    """ Function that creates an object """
    with open(filename) as my_file:
        return (json.loads(my_file.read()))
