#!/usr/bin/python3
"""
    Create 'text_indentation' function.
"""


def text_indentation(text):
    """
        Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
        Prototype: def text_indentation(text):
        text must be a string, otherwise raise a TypeError exception with the message text must be a string
        There should be no space at the beginning or at the end of each printed line

    """
    if type(text) != str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
