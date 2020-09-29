#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
a = int(input("Give me a number\n"))
if a < 0:
    print(a,"is not a positive integer")
elif a > 0:
    print(a,"is a positive integer.")
elif a ==0:
    print("your number is zero")