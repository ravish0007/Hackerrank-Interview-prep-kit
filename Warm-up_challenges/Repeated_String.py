import os

# Complete the repeatedString function below.


def repeatedString(string, n):

    quotient, remainder = divmod(n, len(string))
    total_a = quotient * string.count('a')
    if remainder:
        total_a = total_a + string[:remainder].count('a')
    return total_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
