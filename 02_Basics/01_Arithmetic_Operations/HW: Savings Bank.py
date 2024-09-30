#!/usr/bin/python3

# Create a variable 'balance'
balance = 0
print("Initial Balance:", balance)

# Initial Deposit
initial_deposit = 1500
balance += initial_deposit
print("After Initial Deposit of 1500: Balance =", balance)

# Salary Credited
salary = 3300
balance += salary
print("After Salary Credited of 3300: Balance =", balance)

# Online Purchase
online_purchase = 33.33
balance -= online_purchase
print("After Online Purchase of 33.33: Balance =", balance)

# House Rent
house_rent = 1500
balance -= house_rent
print("After House Rent Paid of 1500: Balance =", balance)

# balance
print("Final Balance:", balance)