#float
num1 = 100.5
num2 = 100.5
print(num1 is num2)  # False (different objects)
print(num1 == num2)  # True (same value)


#Strings
str1 = "hello"
str2 = "hello"
print(str1 is str2)  # True (same memory location, interned string)

str1 = "hello world!"
str2 = "hello world!"
print(str1 is str2)  # True (interned string for longer literals too)

str1 = "hello" + " world!"
str2 = "hello world!"
print(str1 is str2)  # False (concatenated string may not be interned)


#Tuples
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)
print(tup1 is tup2)  # True (since tuples are immutable, Python may reuse objects)


