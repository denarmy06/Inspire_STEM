# Project to show employee records
# Date: 21/02/2024
# Name: Dennis Muhami

print("---EMPLOYEE REGISTER---")
print("  1.Dennis Muhami")
print("  2.John Kamau")
print("  3.Mercy Wanjira")
print("  ---  ")

name = input("Enter employee name :")

print("Name :", name)
if name == "Dennis Muhami":
    age = 28
    sal = 50000
    bon = 6000
    print("Age :",age)
    print("Salary :",sal)
    print("Bonus :",bon)
    print("Total :",sal + bon)

    print("\n")

    print("Due to new revision;")
    new_s = sal + (0.3*sal)
    new_b = bon - 5000
    tot_s = new_s + new_b

    print("New salary :",new_s)
    print("New bonus :",new_b)
    print("New total :",tot_s)
elif name == "John Kamau":
    age = 35
    sal = 75000
    bon = 10000
    print("Age :",age)
    print("Salary :",sal)
    print("Bonus :",bon)
    print("Total :",sal + bon)

    print("\n")

    print("Due to new revision;")
    new_s = sal + (0.3*sal)
    new_b = bon - 5000
    tot_s = new_s + new_b

    print("New salary :",new_s)
    print("New bonus :",new_b)
    print("New total :",tot_s)
elif name == "Mercy Wanjira":
    age = 31
    sal = 60000
    bon = 7500
    print("Age :",age)
    print("Salary :",sal)
    print("Bonus :",bon)
    print("Total :",sal + bon)

    print("\n")

    print("Due to new revision;")
    new_s = sal + (0.3*sal)
    new_b = bon - 5000
    tot_s = new_s + new_b

    print("New salary :",new_s)
    print("New bonus :",new_b)
    print("New total :",tot_s)
else:
    print("The named person is not registered in this company")

