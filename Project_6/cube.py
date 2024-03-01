# Program to find S.A and vol of a cube
# Date: 29/02/2024
# Name: Dennis Muhami

length = float(input("Enter length of one side of the cube :"))

def cube_SA(surface_a):
    surface_a = ((length**2) * 6)
    print("The surface are of the cube is {0}cm".format(surface_a))

cube_SA({0})

def cube_vol(volume):
    volume = (length**3)
    print("The volume of the cube is {0}cm".format(volume))

cube_vol({0})
