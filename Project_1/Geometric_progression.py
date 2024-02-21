# This is a program to solve for geometric progression
# Date: 20/02/2024
# Name: Dennis Muhami
import math

a = float(input("Enter first term :"))
r = float(input("Enter common ratio :"))
n = float(input("Enter the position of the term :"))

sol = (a * r**(n - 1))
sum = ((a * (r**n - 1))/(r - 1))

print("The value of the term is :",sol)
print("The sum of the terms is :",sum)

