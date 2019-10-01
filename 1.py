#Q1. WAP to find roots of a quadratic equation

import math
a=int(input("Enter coefficient of x^2:"))
b=int(input("Enter coefficient of x:"));
c=int(input("Enter value of constant in the quadratic equation:"))

d=b*b-4*a*c
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)

print("Roots of the equation are:")
print(r1)
print(r2)
