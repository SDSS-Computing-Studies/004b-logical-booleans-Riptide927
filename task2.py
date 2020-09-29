#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""
import math

n= int(input("Give me a number "))
s= math.sqrt(n)
c = round(n**1/3)

if c%1 == 0 and s%1 == 0:
    print(n,"is both a perfect square and a perfect cube.")
elif  s%1 ==0:
    print(n," is only a perfect square.")
elif c%1 == 0:
    print(n," is only a perfect cube.")
