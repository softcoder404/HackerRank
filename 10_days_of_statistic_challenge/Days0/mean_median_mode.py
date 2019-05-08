# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.

   #calculating mean, median and mode

#Mean
def find_mean(my_list):
    n = len(my_list)
    total = 0
    for x in my_list:
        total += x

    mean = total / n
    print('%.1f'%mean)


#Median
def find_median(my_list):
    # write a function to check if an integer is odd or Even
    my_list.sort()
    def odd_or_even(n):
        if n%2 != 0:
            return 'odd'
        else:
             return 'even'
    list_len = len(my_list)
    if odd_or_even(list_len) == 'even':
        a = int(list_len / 2)
        b = int(a - 1)
        c = (my_list[a] + my_list[b]) / 2
        print('%.1f'%c)
    else:
        a = (list_len / 2) + 0.5 - 1
        a = int(a)
        print('%.1f'%my_list[a])


#mode
def find_min_mode(list_item):
    #sort out the list item by re-arranging and removing duplicate

    sorted_list = []
    for i in list_item:
        sorted_list.append(i) #copying the list item to sorted list
    sorted_list.sort() #sorting in ascending order
    sorted_list = list(dict.fromkeys(sorted_list)) #removing duplicate

    counter = 0 #declaring counter as global variable
    repeat = []
    index_buf = []
    mode_buf = []
    z = 0
    i = len(list_item) - 1
    for x in sorted_list:
        for y in range(len(list_item)):
            if x == list_item[y]:
                counter += 1
            if y == i:
                repeat.append(counter)
                counter = 0

    max_value = max(repeat)
    for x in range(len(repeat)):
        if repeat[x] == max_value:
            index_buf.append(x)
    for x in index_buf:
        mode_buf.append(sorted_list[x])
    mode_val = min(mode_buf)
    print(mode_val)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    find_mean(arr)
    find_median(arr)
    find_min_mode(arr)
