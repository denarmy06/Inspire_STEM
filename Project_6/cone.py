# Program to find S.A and vol of a cone
# Date: 29/02/2024
# Name: Dennis Muhami

import math 

r = float(input("Enter radius of cone :"))
h = float(input("Enter height of cone :"))
l = float(input("Enter slanting height of cone :"))

def cone_SA(surface_a):
    surface_a = ((math.pi * (r**2)) + (math.pi * r * l))
    print("The surface area of the cone is {0}".format(surface_a))

cone_SA({0})

def cone_vol(volume):
    volume = ((1/3) * math.pi * (r**2) * h)
    print("The volume of the cone is {0}".format(volume))

cone_vol({0})
