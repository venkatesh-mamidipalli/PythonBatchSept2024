#!/usr/bin/python3

# Two Independent while loops

first = 0
while first < 5:
    first += 1
    print(f'{first = }')

second = 0
while second < 5:
    second += 1
    print(f'{second = }')

print()
# Second while loop under first while loop
MAX_TABLE = 10

first = 0
while first < MAX_TABLE:
    first += 1
    # print(f'{first = }')

    second = 0
    while second < MAX_TABLE:
        second += 1
        # print(f'\t{second = }')
        # print(first, '*', second, '=', first * second)
        # print(str(first) + ' * ' + str(second) + ' = ' + str(first * second))

        # old style string formatting
        # print('%d * %d = %d' % (first, second, first * second))
        # print('%2d * %2d = %3d' % (first, second, first * second))


        # New Style formatting
        # print('{} * {} = {}'.format(first, second, first * second))
        # print('{0} * {1} = {2}'.format(first, second, first * second))
        # print('{0:2} * {1:2} = {2:3}'.format(first, second, first * second))
        # print('{0:02} * {1:02} = {2:03}'.format(first, second, first * second))  # zero - padding
        # print('{:2} * {:2} = {:3}'.format(first, second, first * second))

        # F-strings
        # print(f'{first} * {second} = {first * second}')
        print(f"{first:2} * {second:2} = {first * second:3}")

    # print('----------')
    print('-' * 12)