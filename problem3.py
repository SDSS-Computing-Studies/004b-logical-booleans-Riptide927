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
an= str(a)
bn= str(b)
cn= str(c)
if a > b and a > c:
    c = a
    b = b
    a = c
if b > a and b > c:
    c = b
    b = a
    a = c
if (a**2)+ (b**2) == (c**2):
    print(an + "," + bn +","+ cn + " form a Pythagorean triple")
else:
    print(an + "," + bn +","+ cn + " do not form a Pythagorean triple")
