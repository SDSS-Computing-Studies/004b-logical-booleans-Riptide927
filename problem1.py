"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is frue.
"""

#! python3

a = int(input("Give me a number\n"))
b = a / 6
c = b / 8

if  b % 1==0 and c % 1 != 0:
    print(a,"is frue")
else:
    print(a,"is not frue")