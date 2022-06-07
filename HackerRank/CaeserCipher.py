#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    while k > 26:
        k -= 26

    alphabet = string.ascii_lowercase[:]
    alphabetmap = alphabet[k:] + alphabet[:k]
    cipher = ""

    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                ind = alphabet.index(s[i].lower())
                cipher += alphabetmap[ind].upper()
            else:
                ind = alphabet.index(s[i])
                cipher += alphabetmap[ind]
        else:
            cipher += s[i]

    return cipher

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
