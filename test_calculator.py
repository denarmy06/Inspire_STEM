# Program for calculator 

print("Select an operation you would like to perform")
print("    1. ADDITION")
print("    2. SUBTRACTION")
print("    3. MULTIPLICATION")
print("    4. DIVISION")

operation = input()

if operation == "1":
    num_1 = input("Enter first number :")
    num_2 = input("Enter second number :")
    print("The sum is :",float(num_1) + float(num_2))
elif operation == "2":
    num_1 = input("Enter first number :")
    num_2 = input("Enter second number :")
    print("The difference is :",float(num_1) - float(num_2))
elif operation == "3":
    num_1 = input("Enter first number :")
    num_2 = input("Enter second number :")
    print("The product is :",float(num_1) * float(num_2))
elif operation == "4":
    num_1 = input("Enter first number :")
    num_2 = input("Enter second number :")
    print("The quotient is :",float(num_1) / float(num_2))
else:
    print("Invalid operation")


