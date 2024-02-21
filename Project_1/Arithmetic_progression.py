# This is a program to calculate arithmetic progretion
# Date: 20/02/2024
# Name: Dennis Muhami
import math

a = float(input("Enter first term :"))
d = float(input("Enter common difference :"))
n = float(input("Enter the position of the term :"))

sol = (a + (n - 1)*d) 
sum = ((n/2)*((2*a) + ((n - 1) * d)))

print("The value of the term is :",sol)
print("The sum of the terms are :",sum)


