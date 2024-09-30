#!/usr/bin/python3

feet = float(input("Enter the value in feet: "))
inches = feet * 12  # 1 foot = 12 inches
centimeters = inches * 2.54  # 1 inch = 2.54 centimeters

print("Value in feet: ", feet)
print("Value in inches: %.2f" % inches)
print("Value in centimeters: %.2f" % centimeters)