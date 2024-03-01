# Program to find S.A and vol of a sphere
# Date: 29/02/2024
# Name: Dennis Muhami

import math

r = float(input("Enter the radius of the sphere :"))

def sphere_SA(surface_a):
    surface_a = (4 * math.pi * r**2)
    print("The surface area of the sphere is {0}".format(surface_a))

sphere_SA({0})

def sphere_vol(volume):
    volume = ((4/3) * math.pi * r**3)
    print("The volume of the sphere is {0}".format(volume))

sphere_vol({0})


