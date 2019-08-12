#!/bin/python3

import os

# Complete the rotLeft function below.


def rotLeft(a, d):

    '''from collections import deque
    # use deque its handy, double ended queue
    d = d % len(a)       # Reducing computation
    a = deque(a)
    a.rotate(-1 * d)
    return a'''

    d = d % len(a)
    a = a[d:] + a[:d]
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
