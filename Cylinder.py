# Program to calculate volume and surface are of a sphere
# Date: 20/02/2024
# Name: Dennis Muhami
import math

r = float(input("Enter radius of cylinder :"))
h = float(input("Enter height of cylinder :"))
d = 2*r

vol = (math.pi * r**2 * h)
surf_area = ((2 * math.pi * r**2) + (math.pi * d * h))

print("The volume of the cylinder is :",vol)
print("The surface area of the cylinder is :",surf_area)




