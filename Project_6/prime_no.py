# Program to write even numbers
# Date: 29/02/2024
# Name: Dennis Muhami

x = int(input("Enter starting point :"))
y = int(input("Enter ending point :"))

def prime_no(primes):
    for primes in range(x,y+1):
        if primes > 1:

            for j in range(2,primes):
                if primes%j == 0:
                    break
            else:
                print(primes)

prime_no(1)
