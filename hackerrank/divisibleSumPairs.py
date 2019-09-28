import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, arr):
    m = [0] * len(arr)
    for e in arr:
        m[e % k] += 1

    count = int(m[0] * (m[0] - 1)/2)
    for i in range(1, int(k/2) + 1):
        if i != k-1:
            count += m[i] * m[k - i]

    if k % 2 == 0:
        count += m[int(k/2)] * (m[int(k/2)]-1) / 2

    return count

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/divisible-sum-pairs-testcases/input/input00.txt", 'r')

    nk = filename.readline().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, filename.readline().rstrip().split()))

    result = divisibleSumPairs(n, k, arr)
    print(result)