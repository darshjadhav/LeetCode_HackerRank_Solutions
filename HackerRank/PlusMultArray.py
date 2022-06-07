#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'plusMult' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def plusMult(A):
    # Write your code here
    lenA = len(A)
    rEven = 0
    rOdd = 0
    evenSum = 0
    oddSum = 0
    
    for i in range(0, lenA):
        if i % 2 == 0:
            if rEven % 2 == 0:
                evenSum += A[i]
                rEven += 1
            else:
                evenSum *= A[i]
                rEven += 1
        else:
            if rOdd % 2 == 0:
                oddSum += A[i]
                rOdd += 1
            else:
                oddSum *= A[i]
                rOdd += 1
                
    rEven = evenSum % 2
    rOdd = oddSum % 2
    
    if rEven > rOdd:
        return "EVEN"
    elif rEven < rOdd:
        return "ODD"
    
    return "NEUTRAL"

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    A_count = int(input().strip())

    A = []

    for _ in range(A_count):
        A_item = int(input().strip())
        A.append(A_item)

    result = plusMult(A)

    fptr.write(result + '\n')

    fptr.close()
