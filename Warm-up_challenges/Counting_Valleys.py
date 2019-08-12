#!/bin/python3

import os

# Complete the countingValleys function below.


def countingValleys(n, s):

    level, valleys = 0, 0
    down_flag, up_flag = 0, 1

    for i in s:
        if i == 'U':
            level += 1
        else:
            level -= 1

        if level < 0 and up_flag:
            valleys += 1
            down_flag, up_flag = 1, 0

        elif level >= 0 and down_flag:
            down_flag, up_flag = 0, 1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
