#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    a.sort()
    counts = dict()
    for elem in a:
        if elem in counts.keys():
            counts[elem] += 1
        else:
            counts[elem] = 1

    for key, val in counts.items():
        if val == 1:
            uniqueElem = key



    return uniqueElem


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
