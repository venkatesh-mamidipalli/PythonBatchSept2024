#!/usr/bin/python3

values = range(9)  # range(FINAL_VALUE) => range(0, 9, 1)
print(type(values), values)  # <class 'range'> range(0, 9)

# range(INITIAL_VALUE, FINAL_VALUE) => range(0, 9, 1)
values = range(0, 9)
print(type(values), values)  # <class 'range'> range(0,9)

# range(INITIAL_VALUE, FINAL_VALUE, STEP) => range(0, 9, 1)
values = range(0, 9, 1)
print(type(values), values)  # <class 'range'> range(0,9)


for each_ele in values:
    print(each_ele)


print(f"{list(values)  =}")
print(f"{tuple(values) =}")
print(f"{set(values)   =}")
print()


values2 = range(0, 9, 2)
print(list(values2))  # [0, 2, 4, 6, 8]

values2 = range(0, 9, -1)
print(list(values2))  # []

values2 = range(9, 0, -1)
print(list(values2))  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

values2 = range(9, -1, -1)
print(list(values2))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

values2 = range(9, -1, -3)
print(list(values2))  # [9, 6, 3, 0]
