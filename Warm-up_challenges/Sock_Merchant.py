#!/bin/python3

import os
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    unique_elements = set(ar)
    pair_dict = {i: ar.count(i) for i in unique_elements}  # Counter is good here
    total_pairs = sum(pair_dict[i]//2 for i in pair_dict)
    return total_pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
