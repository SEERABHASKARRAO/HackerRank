import math
import os
import random
import re
import sys

def miniMaxSum(arr):
   n=len(arr)
   arr.sort()
   print(sum(arr[:n-1]),sum(arr[1:n]))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
