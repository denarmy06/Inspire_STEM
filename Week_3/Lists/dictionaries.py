# Date: 27/02/2024
# Name: Dennis Muhami

my_laptop = {"Make":"Hp","Color":"Silver","Weight":"1.2kgs","Y.O.M":"2020"}
print(my_laptop["Make"])
print(my_laptop["Color"])
print(my_laptop["Y.O.M"])
print("\n")

my_laptop["Color"] = "Red"
my_laptop["Y.O.M"] = "2019"
print(my_laptop)
print("\n")

my_laptop["Size"] = "1200mm x 600mm"     # How to add
print(my_laptop)
print("\n")

del my_laptop["Color"]                   # How to delete
print(my_laptop)
print("\n")

bros_laptop = my_laptop.copy()           # How to copy
print(bros_laptop)

"""
for key,value in my_laptop.items():
    print(key)
    print(value)
    print("\t")
"""

