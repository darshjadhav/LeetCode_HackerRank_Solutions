import math
import os
import random
import re
import sys


def doubleonmatch(arr, num):
    arr.sort()
    for i in range(0, len(arr)):
        if arr[i] == num:
            num*=2

    return num


if __name__ == '__main__':
    num = doubleonmatch(arr=[1, 2, 4, 11, 12, 8], num=2)
    print(num)
