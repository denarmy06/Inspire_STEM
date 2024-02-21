# Program to calculate volume and surface area of a sphere
# Date: 20/02/2024
# Name: Dennis Muhami
import math

r = float(input("Enter the radius of the sphere :"))

vol = ((4/3) * math.pi * r**3)
surf_area = (4 * math.pi * r**2)

print("The volume of the sphere is :",vol)
print("The surface area of the sphere is :",surf_area)

