#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    sq=math.sqrt(len(s))
    r=math.floor(sq)
    c=math.ceil(sq)
     
    while r*c<len(s):
        r+=1
        
    matrix=[[0 for i in range(c)]
     for j in range(r)]
    index=0;   
    j=0
   
    for i in range(len(s)):
        matrix[j][index]=s[i]
        index+=1
        if index==c:
            index=0
            j+=1
    z=""
   
    for i in range(c):
        for j in range(r):
            if matrix[j][i]!=0 :
                z+=matrix[j][i]
        z+=" "
    return z



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
