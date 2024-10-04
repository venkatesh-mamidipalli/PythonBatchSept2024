#!/usr/bin/python3
"""
Purpose: Progress Status Bar Implementation

    Escape Sequences
        \t - tab space
        \n - new line
        \r - rare feed
"""

print("Venkatesh")
print("venka\tesh")
print("venkat\nesh")
print()


print("1234567890\rDOG")  # DOG4567890
print("abcdef\r123")  # 123def
print()


data_set = range(-100, 10_00_000)
data_set_length = len(data_set)


for loop_index, _ in enumerate(data_set):
    percent_completed = (loop_index / data_set_length) * 100
    percent_completed = round(percent_completed, 2)

    # print(f'\r{loop_index =} {data_set_length =} {percent_completed =}', end="")
    print(f"\r{percent_completed:5} completed", end="")
