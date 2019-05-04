#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    def space(i):
     return ' ' * i
    for x in range(1,n+1):
        if x != n:
            s = space(n -x)
            h = '#' * (n - (n -x))
            print(s + h)
        else:
            print('#'*n)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
