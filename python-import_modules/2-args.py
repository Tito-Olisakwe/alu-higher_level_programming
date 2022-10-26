#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    lenght = len(argv) - 1
    if lenght == 1:
        print('1 argument:\n1: {}'.format(argv[0]))
    elif lenght == 0:
        print('0 arguments.')
    else:
        print(f'{lenght} arguments:')
        for i in range(1, len(argv)):
            print(f'{i}: {argv[i]}')
