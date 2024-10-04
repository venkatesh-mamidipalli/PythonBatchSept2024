#!/usr/bin/python3

number = 34
print(f"{number             = }")
print(f"{number / 2         = }")
print(f"{number % 2         = }")
print(f"{number % 2 == 0    = }")

if number != 0:
    print(f"{number} is non-zero")

if number:
    print(f"{number} is non-zero")


if number % 2 == 0:
    print(f'{number} is Even')

if number % 2: # != 0:
    print(f'{number} is Odd')

# Rewriting with else
if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")


# rewriting
if number % 2:
    print(f"{number} is ODD")
else:
    print(f"{number} is EVEN")
