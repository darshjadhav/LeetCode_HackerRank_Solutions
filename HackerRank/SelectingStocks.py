#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'selectStock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER saving
#  2. INTEGER_ARRAY currentValue
#  3. INTEGER_ARRAY futureValue
#

def selectStock(saving, currentValue, futureValue):
    # # Write your code here
    lenCurr = len(currentValue)
    stockDiff = [0] * lenCurr
    for i in range(0, lenCurr):
        stockDiff[i] = futureValue[i] - currentValue[i]

    comb = [[0 for _ in range(lenCurr)] for _ in range(saving+1)]
    for i in range(1, saving + 1):
        for j in range(0, lenCurr):
            if j == 0:
                if currentValue[j] <= i:
                    if  comb[i-1][j] < stockDiff[j]:
                        comb[i][j] = stockDiff[j]

                    else:
                        comb[i][j] = comb[i-1][j]
                else:
                    comb[i][j] = 0

            else:
                comb[i][j] = comb[i][j-1]

                if currentValue[j] < i:
                    if comb[i][j] < comb[i-currentValue[j]][j-1] + stockDiff[j]:
                        comb[i][j] = comb[i-currentValue[j]][j-1]+stockDiff[j]

                    if comb[i][j] < comb[i-currentValue[j]][j]:
                        comb[i][j] = comb[i-currentValue[j]][j]
    res = comb[saving][lenCurr-1]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    saving = int(input().strip())

    currentValue_count = int(input().strip())

    currentValue = []

    for _ in range(currentValue_count):
        currentValue_item = int(input().strip())
        currentValue.append(currentValue_item)

    futureValue_count = int(input().strip())

    futureValue = []

    for _ in range(futureValue_count):
        futureValue_item = int(input().strip())
        futureValue.append(futureValue_item)

    result = selectStock(saving, currentValue, futureValue)

    fptr.write(str(result) + '\n')

    fptr.close()
