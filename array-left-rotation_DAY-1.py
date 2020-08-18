
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n,d = map(int,input().split())

    a = list(map(int, input().rstrip().split()))
    b=a[0:d]
    for i in range(d):
        a.pop(0)
    c=a+b
    print(" ".join(map(str,c)))
