#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    l = [1 if x >0 else -1 for x in arr if x != 0]
    print("%.6f" % float(l.count(1)/n))
    print("%.6f" % float(l.count(-1)/n))
    print("%.6f" % float(abs(len(l)-n) /n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
