#program for if-elif-else
# Date: 26/02/2024
# Name: Dennis Muhami

age = int(input("Enter age :"))

if age < 18 :
    print("You are not allowed to dive")

if age > 17.9 :
    print("You are allowed to dive")    

# Salary

salary = float(input("Enter salary amount :"))
if salary >= 30000 and salary <= 50000 :
    new_s = salary * 1.1
    print("Your new salary is :",new_s)

else:
    print("No changes to your salary have been made")

county = input("Enter home county :")
if county == "Nyeri" or county == "Kissi":
    print("You get a bursary")


grade = float(input("Enter grade :"))
if grade >= 84 and grade <=90:
    print("You win a calculator")
elif grade >=50 and grade <=83:
    print("you win a mathematical set")
elif grade > 90:
    print("Invalid entry")
else :
    print("You get nothing")
    

