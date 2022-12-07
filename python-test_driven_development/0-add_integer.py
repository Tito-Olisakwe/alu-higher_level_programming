#!/usr/bin/python3
"""
    Create "add_integer" function.
"""


def add_integer(a, b=98):
    """
        Write a function that adds 2 integers.
        a and b must be integers or floats, otherwise raise a TypeError exception with 
        the message a must be an integer or b must be an integer. a and b must be first 
        cast to integers if they are float. Returns an integer: the addition of a and b
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
