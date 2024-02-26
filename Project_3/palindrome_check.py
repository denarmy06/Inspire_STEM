# Program to check for palindrome
# Date: 22/02/2024
# Name: Dennis Muhami


def is_palindrome(text):
    length = len(text)
    for i in range (0, length // 2):
        if (text[i] != text[length - i - 1]):
            return False
    return True

string_1 = "racecar"

print(is_palindrome(string_1))

string_2 = "dennis"

print(is_palindrome(string_2))
