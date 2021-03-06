#!/bin/python3

import os
import sys

#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    H1=h1[::-1]
    H2=h2[::-1]
    H3=h3[::-1]

    sum_H1 = sum(H1)
    sum_H2 = sum(H2)
    sum_H3 = sum(H3)

    while not (sum_H1 == sum_H2 and sum_H2 == sum_H3):
        if sum_H1 > sum_H2 or sum_H1 > sum_H3:
            t = H1.pop()
            sum_H1 -= t
        if sum_H2 > sum_H1 or sum_H2 > sum_H3:
            t = H2.pop()
            sum_H2 -= t
        if sum_H3 > sum_H1 or sum_H3 > sum_H2:
            t = H3.pop()
            sum_H3 -= t
    
    return sum_H1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
