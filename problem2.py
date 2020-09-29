#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a = int(input("Give me a number\n"))
b = int(input("Give me a number\n"))
if a > b:
    i=a/b
    if i % 1==0:
        a= str(a)
        b= str(b)
        print(b + " is a factor of "+ a)
    else:
        a= str(a)
        b= str(b)
        print(b + " is not a factor of "+ a)
elif b > a:
    i=b/a
    if i % 1==0:
        a= str(a)
        b= str(b)
        print(a + " is a factor of "+ b)
    else:
        a= str(a)
        b= str(b)
        print(a + " is not a factor of "+ b)
