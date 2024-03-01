# Program to write even numbers
# Date: 29/02/2024
# Name: Dennis Muhami

def even_no(x,y):
    for i in range (x,y + 1,2):
        print(i)

x = int(input("Enter first number :"))
y = int(input("Enter second number :"))

if x %2 :
    even_no(x + 1,y)

else:
    even_no(x,y)





