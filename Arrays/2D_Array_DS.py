#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    data = []
    
    d = 0
    for i in range(4):
        for j in range(4):
            data.append(sum(arr[i][d:d+3]) + arr[i+1][d+1] + sum( arr[i+2][d:d+3]) )
            d+=1
        d = 0
    return max(data)











if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

