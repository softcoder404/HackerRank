# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import os
import random
import re
import sys

def weighted_mean(arr1,arr2):
    xw = 0
    sw = 0
    for i in range(len(arr1)):
        xw += (arr1[i] * arr2[i])
        sw += arr2[i]
    wm = xw / sw
    print('%.1f'%wm)


if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().rstrip().split()))
    w = list(map(int, input().rstrip().split()))
    weighted_mean(x,w)
