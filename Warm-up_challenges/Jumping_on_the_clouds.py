#!/bin/python3

import os

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):

    jumps, i = 0, 0

    # Jumping two blocks, if 1 found, jumping back and jumping just a block

    while i < len(c)-1:
        i += 2
        jumps += 1
        if i >= len(c):          # managing over jumping
            break
        if c[i] == 1:
            i -= 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
