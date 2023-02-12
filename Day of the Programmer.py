#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
   if(year>1918): 
    if((year%100!=0 and year%4==0) or year%400==0):
        return("{}.09.{}".format(12,year))
    else:
        return("{}.09.{}".format(13,year))
   if(year<1918):
    if(year%4==0):
         return("{}.09.{}".format(12,year))
    else:
        return("{}.09.{}".format(13,year))
   if(year==1918):
        return("{}.09.{}".format(26,year))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')
    fptr.close()
