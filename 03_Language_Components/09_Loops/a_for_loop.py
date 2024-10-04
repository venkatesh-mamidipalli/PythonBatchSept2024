#!/usr/bin/python3

# TypeError: 'int' object is not iterable
# TypeError: 'float' object is not iterable
# TypeError: 'NoneType' object is not iterable
# TypeError: 'bool' object is not iterable

# strings
for i in "Python":
    print(i)
print()

for each in str(1231.123):
    print(each, end=", ")
print()

for each in str(True):
    print(each, end=", ")
print()

for each in "None":
    print(each, end=", ")
print()

# =====================================================================================
print()

loop_count = 0
for each_char in "Python":
    print(loop_count, each_char)
    loop_count += 1

# enumerate() - builtin function to get the loop index
for each_char in "Python":
    print(each_char)

for each_pair in enumerate("Python"):
    print(each_pair)


# Unpacking

num1 = 111
num1 = 222, 333  # Asignment operation
num2, num3 = 222, 333  # UNpacking

# num4, num5 = 444
# TypeError: cannot unpack non-iterable int object


num4 = num5 = 444
print(
    f"""
    {type(num1) = } {num1 = }
    {type(num2) = } {num2 = }
    {type(num3) = } {num3 = }
"""
)
print()

for loop_index, each_chr in enumerate("Python"):
    # print(loop_index, each_chr)
    print(f"At position {loop_index}, character is {each_chr}")
print()

# To get the loop index with an offset
for loop_index, each_chr in enumerate("Python", -3):
    print(f"At position {loop_index:2}, character is {each_chr}")
print()

for loop_index, each_chr in enumerate("Python", 77):
    print(f"At position {loop_index:2}, character is {each_chr}")
print()

# lists
for each_ele in [11, 22, 33, 44, 55]:
    print(each_ele, end=", ")
print()

for each_ele in enumerate([11, 22, 33, 44, 55]):
    print(f"{each_ele[0]} ===> {each_ele[1]}")
print()

for loop_index, each_ele in enumerate([11, 22, 33, 44, 55]):
    print(f"{loop_index} ===> {each_ele}")
print()

for loop_index, each_ele in enumerate([11, 22, 33, 44, 55], -50):
    print(f"{loop_index} ===> {each_ele}")
print()
