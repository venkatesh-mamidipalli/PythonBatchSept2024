#Palindrome 

input = input("Enter a value to check if it is a palindrome: ")

print(f"'{input}' is a palindrome." if input == input[::-1] else f"'{input}' is not a palindrome.")