#!/usr/bin/python3
"""
    Create 'say_my_name'  function.
"""


def say_my_name(first_name, last_name=""):
    """
        Write a function that prints My name is <first name> <last name>
        Prototype: def say_my_name(first_name, last_name=""):
        first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
