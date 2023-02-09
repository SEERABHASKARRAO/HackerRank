#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # if(len(n)==1):
    #     return int(n)*k
    # else:
        n=list(map(int,n))
        while(len(n)!=1):
            sum1=sum(n)
            total=sum1*k
            k=1
            n=list(map(int,str(total)))
        else:
            return n[0]
        # superDigit(total,k)
    # Write your code here

if __name__ == '__main__':


    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    y=superDigit(n, k)
    print(y)
