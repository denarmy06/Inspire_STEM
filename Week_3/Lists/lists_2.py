# Date: 27/02/2024
# Name: Dennis Muhami

friends = ["Peter","Pius","Kadari","Maggie","Eliza"]
for friend in friends:
    print(friend)

print("\n")

enemies = friends[:]   # how to copy one list from another
print(enemies)
print("\n")

fruits = ["lemon","mango","guava","lime","strawberry","pineapple"]
print(fruits[0:3])

del fruits[0]
print(fruits)

squares = []  # Initializes an empty list
for x in range(0,11):
    squares.append(x**2)
    
print(squares)

