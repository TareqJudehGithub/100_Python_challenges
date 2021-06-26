"""
Challenge: Print the Length of a String

Description:
Write a Python program that prints the length of a string s.

"""
from typing import Sequence, List
from typing import Text


def string_length(my_param: Text) -> int:
    return len(my_param)


print(string_length('Hello, world!'))

print('\n')


# Leap year
def is_leap(param_year):
    leap = False

    if param_year % 400 == 0:
        leap = True
    elif param_year % 100 == 0:
        leap = False
    elif param_year % 4 == 0:
        leap = True
    return leap


year = int(1200)

print(is_leap(year))
print('\n')


# Print Function
# Example: n= 3     >>> 123
n = 3
result = ''
for i in range(1, n + 1):
    result += str(i)

print('\n')
print(result, end='\n')

print('Loops')
import math

n = 5
for i in range(n):
    print(i ** 2)








