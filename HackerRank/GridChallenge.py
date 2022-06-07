#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    newgrid = []
    colgrid = []

    for i in range(0, len(grid)):
        sortedStr = "".join(sorted(grid[i]))
        colgrid.append(list(sortedStr))
        newgrid.append(sortedStr)

    outList = []
    for i in range(0, len(colgrid[0])):
        column = "".join([row[i] for row in colgrid])
        if column == "".join(sorted(column)):
            outList.append(True)
        else:
            outList.append(False)

    output = all(outList)
    if output:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
