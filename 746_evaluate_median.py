#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/746

first_line  = input()
second_line = input()

# first_line  = '4'
# second_line = '5 3 4 7'

count   = int(first_line)
elements = list(map(int, second_line.split(' ')))

# XXX: This line is not working.
# elements_ordered_by_asc = list(set(elements))

elements_ordered_by_asc = sorted(elements)

# print(elements)
# print(elements_ordered_by_asc)

if count % 2 == 1:
    # print('Odd number is.')
    median_index = int(count/2)
    print(elements_ordered_by_asc[median_index])
else:
    # print('Even number is.')
    behind_index    = int(count / 2)
    ahead_index     = int(behind_index - 1)
    # print(behind_index, ahead_index)
    print((elements_ordered_by_asc[behind_index] + elements_ordered_by_asc[ahead_index]) / 2)
