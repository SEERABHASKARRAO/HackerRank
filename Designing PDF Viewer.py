#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word

def designerPdfViewer(h, word):
    s=list(word)
    maxi=-999
    for i in s:
        i=i.upper()
        maxi=max(maxi,h[ord(i)-65])
    return maxi*len(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
