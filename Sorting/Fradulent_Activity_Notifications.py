#!/bin/python3

import math
import os
import random
import re
import sys

from bisect import insort, bisect_left

def activityNotifications(expenditure, d):
    v = sorted(expenditure[: d])
    count = 0
    for i, current in enumerate(expenditure[d:]):
        de = expenditure[i]
        if d%2 == 0:
            if current >= v[d//2] + v[d//2-1]:
                count += 1
        elif current >= v[d//2]*2:
                count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
    return count

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

