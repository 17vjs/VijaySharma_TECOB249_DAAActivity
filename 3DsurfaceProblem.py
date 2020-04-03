#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    #A=[[1 3 4][2 2 3][1 2 4]]
    area=0

    for i in range(len(A)):
        
        for j in range(len(A[i])):
            
            for z in range(A[i][j]):
                

                if i-1<0:
                    area+=1
                else: 
                    if A[i-1][j]<=z:
                        area+=1
                if i+1>=len(A):
                    area+=1
                else: 
                    if A[i+1][j]<=z:
                        area+=1
               
                if j-1<0:
                    area+=1
                else: 
                    if A[i][j-1]<=z:
                        area+=1 
                if j+1>=len(A[i]):
                    area+=1
                else: 
                    if A[i][j+1]<=z:
                        area+=1
                if z-1<0:
                    area+=1
                if z+1>=A[i][j]:
                    area+=1
        
                
    return area   
 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
