# Program to calculate higher purchase
# Date: 21/02/2024
# Name: Dennis Muhami

cash_p = float(input("Enter item cash price :"))
dep = float(input("Enter deposit amount :"))
mon = float(input("Enter number of months :"))
inst = float(input("Enter instalment amount :"))

h_p = dep + (mon * inst)
tot_i = h_p - cash_p

print("The hire purchase prise is :",h_p)
print("The total intrest are :",tot_i)
