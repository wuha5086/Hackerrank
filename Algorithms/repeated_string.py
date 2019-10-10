#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    def count_num_a(s):
        count = 0
        for i in s:
            if i == 'a':
                count += 1
        return count
    accurance = n//len(s)*count_num_a(s) + count_num_a(s[: n%len(s)])
    return accurance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
