# Program to find S.A and vol of a cylinder
# Date: 29/02/2024
# Name: Dennis Muhami

import math
r = float(input("Enter radius of cylinder(cm):"))
h = float(input("Enter height of cylinder(cm) :"))
d = 2*r

def cylinder_SA(surface_a):
    surface_a = ((2 * math.pi * r**2) + (math.pi * d * h))
    print("The surface are of the cylinder is {0} squared cm".format(surface_a))

cylinder_SA({0})

def cylinder_vol(volume):
    volume = (math.pi * r**2 * h)
    print("The volume of the cylinder is {0} cubed cm".format(volume))

cylinder_vol({0})
