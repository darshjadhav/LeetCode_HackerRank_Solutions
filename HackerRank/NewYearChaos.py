#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

# 1 2 3 4 5 6 7 8
# 1 2 3 5 4 6 7 8 (5-4)
# 1 2 5 3 4 6 7 8 (5-3)
# 1 2 5 3 4 7 6 8 (7-6)
# 1 2 5 3 7 4 6 8 (7-4)
# 1 2 5 3 7 4 8 6 (8-6)
# 1 2 5 3 7 8 4 6 (8-4)
# 1 2 5 3 7 8 6 4 (6-4)


# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 8 7 (8-7)
# 1 2 3 4 5 8 6 7 (8-6)
# 1 2 3 4
# 1 2 5 3 7 8 6 4


# 1 2 3 4 5
# 1 2 3 5 4
# 1 2 5 3 4
# 2 1 5 3 4


def minimumBribes(q):
    # Write your code here
    bribeVal = 0

    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                bribeVal += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == i+1:
                bribeVal += 2
                q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
            else:
                print("Too chaotic")
                return
    print(bribeVal)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
