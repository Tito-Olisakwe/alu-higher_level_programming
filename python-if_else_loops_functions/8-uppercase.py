#!/usr/bin/python3
def uppercase(str):
    upper_string = ''
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            upper_string = chr(ord(i)+32)
        else:
            upper_string = chr(ord(1))
        print('{}'.format(upper_string), end='')
