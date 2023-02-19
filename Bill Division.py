import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
   sum1=0
   for i in range(len(bill)):
    if(i!=k):
        sum1+=bill[i]
   p=sum1//2
   if(p==b):
        print("Bon Appetit")
   else:
        print(abs(p-b))
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
