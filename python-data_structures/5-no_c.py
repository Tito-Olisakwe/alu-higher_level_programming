#!/usr/bin/python3
def no_c(my_string):
    copy_string = ''
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            continue
        copy_string = copy_string + my_string[i]
    my_string = copy_string
    return my_string
