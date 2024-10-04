#!/usr/bin/python3

us_dollar = 86
canadian_dollar = 50

print("us_dollar       = ", us_dollar)
print("canadian_dollar = ", canadian_dollar)
print()

print(f"us_dollar       = {us_dollar}")
print(f"canadian_dollar = {canadian_dollar}")
print()

print(f"{us_dollar      = }")
print(f"{canadian_dollar= }")
print()

print("us_dollar == canadian_dollar:", us_dollar == canadian_dollar)
print(f"{us_dollar == canadian_dollar = }")
print()

print(f"{us_dollar > canadian_dollar  = }")
print(f"{us_dollar >= canadian_dollar = }")
print(f"{us_dollar < canadian_dollar  = }")
print(f"{us_dollar <= canadian_dollar = }")
print(f"{us_dollar != canadian_dollar = }")
# print(f"{us_dollar <> canadian_dollar = }")  # works only in python 2.x

print()
print(f"{74 == 50 =}")
print(f"{74 != 50 =}")
print(f"{74 >  50 =}")
print(f"{74 >= 50 =}")
print(f"{74 <  50 =}")
print(f"{74 <= 50 =}")
print()


num1 = 34  # Assignment

num1 = 34
num2 = num1
# 34 = num2 # SyntaxError: cannot assign to literal

num1 == 34
34 == num1
34 == 34
34 == 67
print()

str1 = "abc"
str2 = "abc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")
print()

str1 = "abc"
str2 = "bc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")
