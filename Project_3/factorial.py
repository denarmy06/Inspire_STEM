# Program to show factorial
# Date: 22/02/2024
# Name: Dennis Muhami

factorial_no = 1
max_val = int(input("Enter the maximum value :"))

for i in range(1,max_val + 1):
    factorial_no = factorial_no * i
    print(factorial_no)

print("\n")

# Print even numbers
for i in range(0,11,2):
    print(i)      

# Print odd numbers
for i in range(1,12,2):
    print(i)          