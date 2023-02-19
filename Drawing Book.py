#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, t):
    c1=1
    if(t==1):
        return 0
    p=[0]*(n+1)
    p2=[0]*(n+1)
    p[0]=0
    p[1]=0
    count=1
    for i in range(2,n+1,2):
       if((i+1)<=n):
        p[i],p[i+1]=count,count
        count+=1
    if(n%2==0):
      p2[n]=0
      count2=1
      for j in range(n-1,-1,-2):
         if((j-1)>=0):
            p2[j],p2[j-1]=count2,count2
            count2+=1
    else:
        p2[n]=0
        p2[n-1]=0
        count2=1
        for j in range(n-2,-1,-2):
          if((j-1)>=0):
            p2[j],p2[j-1]=count2,count2
            count2+=1
    return min(p[t],p2[t])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
