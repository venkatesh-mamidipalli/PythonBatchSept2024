#!/usr/bin/python3

choice = True
print("choice = ", choice, type(choice), id(choice))

choice = False
print("choice = ", choice, type(choice), id(choice))

# True = 'Venkat'
# cannot assign to True

true_name = "Venkat"

choice = "Venkat"
print("choice = ", choice, type(choice), id(choice))


print("id(True)     = ", id(True))
#print("id(true)     = ", id(true))

print("type(True)   =", type(True))
print("type(true)   =", type(true))
print()

print("True         = ", True)
print("True * 30    = ", True * 30)
print("True * 3.4   = ", True * 3.4) 

print("False        = ", False)
print("False * 30   = ", False * 30)