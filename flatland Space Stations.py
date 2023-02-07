#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if(n==len(c)):
        return 0
    
    c.sort()
    maxi=max(c[0]-0,(n-1)-c[-1])
    for i in range(len(c)-1):
        mid=(c[i]+c[i+1])//2
        res=min(abs(c[i]-mid),abs(c[i+1]-mid))
        maxi=max(res,maxi)
    return maxi
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
