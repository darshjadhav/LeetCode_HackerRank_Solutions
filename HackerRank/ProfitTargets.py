#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    pairCounts = 0
    sortedArr = sorted(stocksProfit)
    
    leftP = 0
    rightP = len(sortedArr) - 1
    
    while leftP < rightP:
        if sortedArr[leftP] + sortedArr[rightP] == target:
            while leftP < rightP and sortedArr[leftP] == sortedArr[leftP + 1]:
                leftP += 1
                
            while leftP < rightP and sortedArr[rightP] == sortedArr[rightP - 1]:
                rightP-=1
                
            pairCounts += 1
            leftP += 1
            rightP -= 1
            
        elif (sortedArr[leftP] + sortedArr[rightP] < target):
            leftP += 1
            
        else:
            rightP -= 1
    
    return pairCounts
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = []

    for _ in range(stocksProfit_count):
        stocksProfit_item = int(input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()
