#!/usr/bin/python3

# Inputs
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))
t = float(input("Enter the time (t) in years: "))

# Simple Interest
A_simple = P * (1 + r * t)
print("Simple Interest Final Amount (A): %.2f" % A_simple)

# Number of times interest is compounded per year for compound interest
n = int(input("Enter the number of times the interest is compounded per year (n): "))

# Compound Interest
A_compound = P * (1 + r / n) ** (n * t)
print("Compound Interest Final Amount (A): %.2f" % A_compound)