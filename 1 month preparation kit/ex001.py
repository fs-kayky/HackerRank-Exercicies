import math
import os
import random
import re
import sys

def plusMinus(arr, n):

    pos = []
    neg = []
    zero = []

    for i in range(n):
        if(arr[i] > 0):
            pos.append(arr[i])
        elif(arr[i] == 0):
            zero.append(arr[i])
        elif(arr[i]<0):
            neg.append(arr[i])

    print(f'{len(pos) / n:.6f}')
    print(f'{len(neg) / n:.6f}')
    print(f'{len(zero) / n:.6f}')
            




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)

