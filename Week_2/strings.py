# Strings in python
# Date: 22/02/2024
# Name: Dennis Muhami

city = "nairobi"
print(city[0]) #n
print(city[1]) #a
print(city[2]) #i
print(city[3]) #r
print(city[4]) #o
print(city[5]) #b
print(city[6]) #i


# Convert to upper case

print(city)
print("\n") # Prints a new line
print(city.upper())

name = "DENNIS MUHAMI"
print(name)
print(name.lower()) # Converts string to lower case

town = "   Naivasha   "
print(town)
print("\t") # Prints new tab
print(town.strip())

# You can add two strings 

f_name = "Dennis"
s_name = "Muhami"

full_name = f_name + s_name
print(full_name)


# Replacing a character

fruit = "orangeo"
print(fruit.replace("o","y"))

subject = "Physical,Sciences"
print(subject.split(",")) 

age = 30
height = 1.2
print("I am {0} years old and {1} meters tall ".format(age,height))









