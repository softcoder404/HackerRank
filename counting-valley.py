#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    up_hill = 0
    num_of_valley = 0

    for x in range(len(s)):
        if s[x] == 'U':
            up_hill += 1
            if up_hill == 0:
              num_of_valley += 1
        elif s[x] == 'D':
            up_hill -= 1


    return num_of_valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
