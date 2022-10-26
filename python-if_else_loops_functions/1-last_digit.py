#!/usr/bin/python3
from math import pi
import random
number = random.randint(-10000, 10000)
last_digit = int(repr(pi)[-1])
if last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number} is {last_digit} and is 0')
elif last_digit < 5 and last_digit != 0:
    print(
        f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
