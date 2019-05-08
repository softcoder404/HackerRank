#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    negative_counter = 0
    postivite_counter = 0
    zero_counter = 0
    for x in range(len(arr)):
        if arr[x] < 1:
            if arr[x] != 0:
                negative_counter += 1
            else:
                zero_counter += 1
        else:
            postivite_counter += 1
    pos_res = postivite_counter /len(arr)
    neg_res = negative_counter /len(arr)
    zero_res =zero_counter /len(arr)
    print('%.6f'%pos_res)
    print('%.6f'%neg_res)
    print('%.6f'%zero_res)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
