#!/usr/bin/python3

input = input("Enter value ")

print(f"'{input}' is a palindrome." if input == input[::-1] else f"'{input}' is not a palindrome.")