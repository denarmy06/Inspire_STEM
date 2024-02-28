# Code to change salary
# Date: 26/02/2024
# Name: Dennis Muhami

sal = int(input("Enter your salary :"))
if sal >= 100000 and sal < 120000 :
    new_s = sal * 1.3
    print("A 30% increase has been made to your salary")
    print("Your new salary is sh:",new_s)
elif sal >= 120000 and sal < 150000 :
    new_s = sal * 1.15
    print("A 15% increase has been made to your salary")
    print("Your new salary is sh:",new_s)
elif sal >= 150000 :
    new_s = sal * 1.05
    print("A 5% increase has been made to your salary")
    print("Your new salary is sh:",new_s)
else:
    print("No changes have been made to your salary")

