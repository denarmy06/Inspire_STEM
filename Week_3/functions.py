# Date: 29/02/2024
# Name: Dennis Muhami

# FUNCTIONS : A block of code running together as a unit
# There are two types; 1.User defined  2.Built in


# Defining a function
def print_name():
    print("My name is Dennis Muhami")



# Calling the function
print_name()
print("\t")



def print_details(name, age, ID, gender):
    print("I am {0}, {1} years old. My ID number is {2} and gender is {3}".format(name, age, ID, gender))

print_details("Dennis Muhami", "18", "12734450", "Male")
print("\t")



def sum_nums(x,y):
    return x + y                     # Return key word

z = sum_nums(10,20)
print(z)
print("\t")


def prod_nums(k,j):
    return k * j

print(prod_nums(5,16))
print("\t")


            # HOW TO USE FOR LOOP INSIDE THE FUNCTION
def print_odds(first_no,last_no):
    for i in  range(first_no,last_no + 1,2):
        print(i)

print_odds(1,15)
