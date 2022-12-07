#!/usr/bin/python3
"""
    Create 'max_integer' function.
"""


def max_integer(list=[]):
    """
    Write unittests for the function def max_integer(list=[]):.
    Your test file should be inside a folder tests
    You have to use the unittest module
    Your test file should be python files (extension: .py)
    Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
    All tests you make must be passable by the function below

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
