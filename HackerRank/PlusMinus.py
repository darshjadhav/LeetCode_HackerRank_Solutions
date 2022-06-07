#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here

    positiveRatio = sum(map(lambda x : x > 0, arr)) / len(arr)
    negativeRatio = sum(map(lambda x : x < 0, arr)) / len(arr)
    zeroRatio = sum(map(lambda x : x == 0, arr)) / len(arr)

    print(f"{positiveRatio:.6f}")
    print(f"{negativeRatio:.6f}")
    print(f"{zeroRatio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
