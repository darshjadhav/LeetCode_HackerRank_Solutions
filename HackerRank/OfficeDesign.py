import math
import os
import random
import re
import sys

def getMaxColors(pricearr, money):
    test_max = 0
    max = 0
    test_price = 0
    count = 0
    i = count
    flag = False
    while(i < len(pricearr)):
        flag = True
        if (pricearr[i] + test_price <= money):
            test_price = test_price + pricearr[i]
            test_max = test_max + 1

        elif (pricearr[i] + test_price > money):
            count = count + 1
            i = count
            test_max = 0
            test_price = 0
            flag = False
        if flag:
            i = i + 1
        if test_max > max:
            max = test_max

    return max





if __name__ == "__main__":
    pricearr = [2,3,5,1,1,2,1]
    money = 7
    result = getMaxColors(pricearr, money)
    print("result: " + str(result))