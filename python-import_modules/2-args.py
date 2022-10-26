#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print('1 argument:\n1: {}'.format(argv[0]))
    elif len(argv) == 1:
        print('0 arguments.')
    else:
        print(f'{len(argv)} arguments:')
        for i in range(1, len(argv)):
            print(f'{len(argv)}: {argv[len(argv)-1]}')
