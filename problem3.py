#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a = int(input("Give me a number "))
b = int(input("Give me a number "))
c = int(input("Give me a number "))
if a >= b and a >= c:
    C = a
    B = b
    A = c
if b >= a and b >= c:
    C = b
    B = a
    A = c
if c >= b and c >= a:
    C = c
    B = b
    A = a
if B > A:
    an= str(A)
    bn= str(B)
    cn= str(C)
    if (A**2)+ (B**2) == (C**2):
        print(an + "," + bn +","+ cn + " form a Pythagorean triple")
    else:
        print(an + "," + bn +","+ cn + " do not form a Pythagorean triple")
elif A > B:
    A2 = B
    B2 = A
    an= str(A2)
    bn= str(B2)
    cn= str(C)
    if (A2**2)+ (B2**2) == (C**2):
        print(an + "," + bn +","+ cn + " form a Pythagorean triple")
    else:
        print(an + "," + bn +","+ cn + " do not form a Pythagorean triple")
