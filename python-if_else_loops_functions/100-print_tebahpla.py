#!/usr/bin/python3
for i in range(97, 123, -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(ord(i)-32)), end="")
