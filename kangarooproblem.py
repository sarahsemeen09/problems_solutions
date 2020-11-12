#!/bin/python3

import math
import os
import random
import re
import sys

#The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
#The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
#You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. 
#If it is possible, return YES, otherwise return NO.
def kangaroo(x1, v1, x2, v2):
    sol = "NO"
    #if x1 is greater than x2 and v1 is greater than v2 then there is no chance of them meeting at one point at the same point
    if x1<x2 and v1<=v2:
        print(sol)
        #if x2 is greater than x1 and v2 is greater than v1 then there is no chance of them meeting at one point at the same point
    elif x1>x2 and v1>=v2:
        print(sol)
    else:
        #If x1 is greater than x2 then swap them so 
        #that the shorter distance is first
        if x1 > x2:
            swapX1X2(x1, x2, v1, v2)
        print("x1")
        #until x1 is still less than x2 there is scope of meeting at a point.
        #if x1 surpasses x2 then meeting after that point is not possible 
        while x1 < x2:
            x1 = x1+v1
            x2 = x2+v2
            if x1 == x2:
                print("Mini Yes")
                sol = "YES"
                break
            else:
                print("Mini No")
    return sol

def swapX1X2(x1, x2, v1, v2):
    #making sure that the lower number is the first kangaroo
    #swapping x1, x2 and v1, v2 if x2 >x2 i.e if the first 
    #kangaroo is farther away from 0 than the second kangaroo
    if x1 < x2:
        temp1 = x1
        x1 = x2
        x2 = temp1
        
        temp2 = v1
        v1 = v2
        v2 = temp2
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
