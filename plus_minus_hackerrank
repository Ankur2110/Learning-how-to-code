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
    totalength = len(arr)
    positive_integer_count = 0
    negative_integer_count = 0
    zero_count = 0
    for item in arr:
        if item>0:
            positive_integer_count +=1
        elif item<0:
            negative_integer_count+=1
        else:
            zero_count +=1
    positive_ratio = round(positive_integer_count/totalength,6)
    negative_ratio = round(negative_integer_count/totalength,6)
    zero_ratio = round(zero_count/totalength,6)
    print(positive_ratio, negative_ratio, zero_ratio, sep="\n")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
