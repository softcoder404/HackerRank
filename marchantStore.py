#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    color_type = []
    counter = 0
    pair = []
    result = 0
    if n == len(ar):
        for i in ar:
            color_type.append(i)
        color_type = list(dict.fromkeys(color_type))
        print('color type',color_type)
        for i in color_type:
            for j in range(len(ar)):
                if i == ar[j]:
                    counter += 1
                if j == len(ar)-1:
                    pair.append(int(counter/2))
                    counter = 0
        for i in pair:
            result += i
        return result
    else:
        return 'n doesn\'t match with array length'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
